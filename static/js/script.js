//Create leaflet map object
var map = L.map('map', {
	center: [44.5282, -89.56],
	zoom:15
	});

	var mbAttr = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>';
    mbUr4 = "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";

var OSM = L.tileLayer(mbUr4, {attribution: mbAttr}).addTo(map);
