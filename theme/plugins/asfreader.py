#!/usr/bin/python -B
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
#
# asfreader.py -- Pelican plugin that processes ezt template Markdown through ezt and  then GitHub Flavored Markdown.
#

import sys
import io
import os
import traceback

import ezt

import pelican.plugins.signals
import pelican.readers
import pelican.settings

GFMReader = sys.modules['pelican-gfm.gfm'].GFMReader


class ASFTemplateReader(ezt.Reader):
  """Enables inserts relative to the template we loaded."""

  def __init__(self, source_path, text):
    self.source_dir, self.fname = os.path.split(source_path)
    self.text = text

  def read_other(self, relative):
    return ezt._FileReader(os.path.join(self.source_dir, relative))

  def filename(self):
    return self.fname


class ASFReader(GFMReader):
    """GFM-flavored Reader for the Pelican system that adds ASF data and ezt
    generation prior to processing the GFM
    """

    def add_data(self, metadata):
        "Mix in ASF data as metadata"

        asf_metadata = self.settings.get('ASF_DATA', { }).get('metadata')
        if asf_metadata:
            metadata.update(asf_metadata)
            # if self.settings.get('ASF_DATA', { }).get('debug'):
            #    print("metadata: %s" % metadata)

    def read(self, source_path):
        "Read metadata and content, process content as ezt template, then render into HTML."
        try:
          # read content with embedded ezt - use GFMReader
          text, metadata = super().read_source(source_path)
          assert text
          assert metadata
          # supplement metadata with ASFData if available
          self.add_data(metadata)
          # prepare text as an ezt template
          # compress_whitespace=0 is required as blank lines and indentation have meaning in markdown.
          template = ezt.Template(compress_whitespace=0)
          reader = ASFTemplateReader(source_path, text)
          template.parse(reader, base_format=ezt.FORMAT_HTML)
          assert template
          # generate content from ezt template with metadata
          fp = io.StringIO()
          template.generate(fp, metadata)
          # Render the markdown into HTML
          content = super().render(fp.getvalue().encode('utf-8')).decode('utf-8')
          assert content
        except:
          traceback.print_exc()
          raise

        return content, metadata


# The following are required or ezmd files are not read instead they are static.
# For direct subclasses of BaseReader like GFMReader the following two
# callables are optional if the class includes enabled=True and file_extenaions.
def add_readers(readers):
    readers.reader_classes['ezmd'] = ASFReader


def register():
    pelican.plugins.signals.readers_init.connect(add_readers)
