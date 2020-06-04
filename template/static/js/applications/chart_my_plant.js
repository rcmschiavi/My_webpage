var listData = null;

function callChart(dataValues){
    listData = dataValues;
    google.charts.load('current', {'packages':['line', 'corechart']});
    google.charts.setOnLoadCallback(drawChart);
}

function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('timeofday', 'Time of Day');
    data.addColumn('number', 'Temperature');
    data.addColumn('number', 'Humidity');
    data.addColumn('number', 'Moisture');
    data.addRows(listData);

    var options = {
      title: 'Average Temperatures and Daylight in Iceland Throughout the Year',
    width: 900,
    height: 500,
    hAxis: {
          title: 'Time of Day',
          format: 'h:mm a',
          viewWindow: {
            min: [-1, 30, 0],
            max: [23, 30, 0]
          }},
    series: {
    0: {axis: 'Temperature'},
    1: {axis: 'Humidity'},
    2: {axis: 'Moisture'}
    },
    axes: {
    y: {
      Temperature: {label: '°C'},
      Humidity: {label: '% rel'},
      Moisture: {label: '[ ]'}
    }
    }
    };

    var chart = new google.charts.Line(document.getElementById('chart_div'));

    chart.draw(data, options);
}
