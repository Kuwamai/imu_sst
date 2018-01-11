var ros = new ROSLIB.Ros({ url : 'ws://' + location.hostname + ':9000' });

ros.on('connection', function() {console.log('websocket: connected');});
ros.on('error', function(error) {console.log('websocket error: ', error); });
ros.on('close', function() {console.log('websocket: closed');});

var data = [{
	y: [],
	type: 'lines',
	line: {color: '#80CAF6'}
}];

var options = {
	  title: 'Anomaly score'
};

Plotly.plot('graph', data, options);

var ls = new ROSLIB.Topic({
	ros : ros,
	name : '/anomaly_score',
	messageType : 'std_msgs/Float64'
});

var array = [];

ls.subscribe(function(message) {
	str = JSON.stringify(message.data);
	document.getElementById("imu_sst").innerHTML = str;
	console.log(str);

	array.push(message.data);
});

var interval = setInterval(function() {
	Plotly.extendTraces('graph', {
	y: [array]
	}, [0])
	
	array = [];

}, 100);
