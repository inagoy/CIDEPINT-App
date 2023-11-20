var marker, map; // Declare marker in the outer scope

function viewAddMap(mapID) {
	if (map !== undefined) {
		map.remove();
	}
	map = L.map(mapID).setView([-34.9223, -57.9546], 12);
	L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
		maxZoom: 19,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
	}).addTo(map);

	map.on("click", function (e) {
		addMarker(e);
		document.getElementById("inputCoordinates").value = JSON.stringify(marker.getLatLng());
	});
}

function viewEditMap(coordinates = null) {
	if (map !== undefined) {
		map.remove();
	}
	console.log("coordinates", coordinates);
	map = L.map("editMap");
	if (coordinates) {
		map.setView([coordinates.lat, coordinates.lng], 12);
		marker = L.marker([coordinates.lat, coordinates.lng]).addTo(map);
	} else {
		map.setView([-34.9223, -57.9546], 12);
	}

	L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
		maxZoom: 19,
		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
	}).addTo(map);

	map.on("click", function (e) {
		addMarker(e);
		document.getElementById("inputCoordinatesEdit").value = JSON.stringify(marker.getLatLng());
	});
}

function addMarker(e) {
	if (marker !== undefined) {
		map.removeLayer(marker);
	}
	marker = new L.marker(e.latlng).addTo(map);
}

function removeMarker() {
	if (marker !== undefined) {
		map.removeLayer(marker);
		document.getElementById("inputCoordinates").value = "";
	}
}

function loadMap(coordinates) {
	if (map !== undefined) {
		map.remove();
	}
	console.log(coordinates);
	map = L.map("viewMap").setView([coordinates.lat, coordinates.lng], 12);
	L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
		maxZoom: 20,
	}).addTo(map);
	marker = L.marker([coordinates.lat, coordinates.lng]).addTo(map);
}
