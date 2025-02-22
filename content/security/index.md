Title: ASF Security Team
license: https://www.apache.org/licenses/LICENSE-2.0

# The Apache Security Team #

The Apache Security Team exists to provide help and advice to Apache
projects on security issues and to provide co-ordination of the handling of
security vulnerabilities. 

# Reporting a vulnerability #

We strongly encourage the reporting of potential security vulnerabilities to one of
our private security mailing lists first, before disclosing them in a
public forum.

A [list of security contacts for Apache projects](projects.html) is
available. If you can't find a project specific security e-mail address and
you have an undisclosed security vulnerability to report then please use
the general security address below.

**Please note that the security contacts should only be used for
reporting undisclosed security vulnerabilities in Apache projects and
managing the process of fixing such vulnerabilities. We cannot accept
regular bug reports or other security related queries at these addresses.
All mail sent to these addresses that does not relate to an undisclosed
security problem in an Apache project will be ignored.** 

**Also note that the security team handles vulnerabilities in Apache projects,
not running ASF services.  All reports of vulnerabilities in ASF
services should be sent to root@apache.org only.**

The general security mailing list address is:
[security@apache.org](mailto:security@apache.org). This is a private
mailing list.

Please send one plain-text email for each vulnerability you are reporting.  We may
ask you to resubmit your report if you send it as an image, movie, HTML, or
PDF attachment when it could just as easily be described with plain text.

Encrypted submissions are not required or preferred as it will take us much
longer to respond to these reports.  There is no team key for security@apache.org
instead you can use the OpenPGP keys of the
following subset of members of the Apache Security Team.
Note that this is
not a complete list of Apache Security Team members and that you should not
contact these members individually about security issues.

- Mark Cox - 5B25 45DA B219 95F4 088C  EFAA 36CE E4DE B00C FE33 -
[pgp.mit.edu](http://pool.sks-keyservers.net:11371/pks/lookup?op=index&search=0x36CEE4DEB00CFE33) 
- Bill Rowe - B1B9 6F45 DFBD CCF9 7401 9235 193F 180A B55D 9977 -
[pgp.mit.edu](http://pgp.mit.edu:11371/pks/lookup?search=0xB55D9977&op=index) 
- Mark Thomas - A9C5 DF4D 22E9 9998 D987 5A51 10C0 1C5A 2F60 59E7 -
[pgp.mit.edu](http://pgp.mit.edu:11371/pks/lookup?search=0x2F6059E7&op=index) 
- Yann Ylavic - 8935 9267 45E1 CE7E 3ED7  48F6 EC99 EE26 7EB5 F61A -
[pgp.mit.edu](http://pgp.mit.edu:11371/pks/lookup?search=0x7EB5F61A&op=index) 

The public keys for all of the above can also be obtained [in a single file](KEYS.txt).

# Vulnerability Information #

Information on the published vulnerabilities for an Apache project can
usually be found on the project's web pages. For convenience a [list of
security information pages for Apache projects](projects.html) is
available. If you can't find the information you are looking for on the
project's web site, you should ask your question on the project's user
mailing list. The security contacts **should not be used to ask questions
about** :

- how to configure the package securely;

- if a published vulnerability applies to specific versions of the Apache
packages you are using;

- if a published vulnerability applies to the configuration of the Apache
packages you are using;

- obtaining further information on a published vulnerability;

- the availability of patches and/or new releases to address a published
vulnerability.

The relevant project's users list is the place to ask such questions. Any
such questions sent to the Apache Security Team or to a project security
team will be ignored.

# Vulnerability handling #

An overview of the vulnerability handling process is:

- The reporter reports the vulnerability privately to Apache.

- The appropriate project's security team works privately with the reporter
to resolve the vulnerability.

- A new release of the Apache package concerned is made that includes the
fix.

- The vulnerability is publically announced.

A [more detailed description of the process](committers.html) has been
written for committers. Reporters of security vulnerabilities may also find
it useful.

