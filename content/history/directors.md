Title: ASF History Project - Directors Timeline
license: https://www.apache.org/licenses/LICENSE-2.0

<div id="timeline-tooltip" style="height: 900px;"></div>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript" src="data/directors.js"></script>
<script type="text/javascript">
  // see https://developers.google.com/chart/interactive/docs/gallery/timeline
  google.charts.load('current',  {'packages':['timeline']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart()  {
    var container = document.getElementById('timeline-tooltip');
    var chart = new google.visualization.Timeline(container);
    var dataTable = director_data();
    var options =  {
          timeline:  { showRowLabels: false }
          };

    chart.draw(dataTable, options);
  }
</script>
