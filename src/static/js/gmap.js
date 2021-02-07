function initMarkerDraggable(map, position) {

    const marker = new google.maps.Marker({
        position: position,
        draggable:true,
        map: map,
    });

    const contentString = 'You can move to fine tune the location';
    let infoWindow = new google.maps.InfoWindow({
        content: contentString,
    });
    infoWindow.open(map, marker);

    marker.addListener("drag", (mapsMouseEvent) => {
        // Close the current InfoWindow.
        infoWindow.close();
        // Create a new InfoWindow.
        infoWindow = new google.maps.InfoWindow({});
        infoWindow.setContent(
            JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
        );
        infoWindow.open(map, marker);

        var myObj = JSON.parse(JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2));
        document.getElementById("id_latitude").value = myObj.lat;
        document.getElementById("id_longitude").value = myObj.lng;

    });
}


function initMap() {
    initMapTemplate(-34.397, 150.644, "map");
}

function initMapTemplate(lat, long, tag_id = "map") {
    const map_center = new google.maps.LatLng(lat, long)

    const map = new google.maps.Map(document.getElementById(tag_id), {
        zoom: 14,
        center: map_center,
    });

    /*
    * Draggable marker
    */
    initMarkerDraggable(map, map_center)

    /*
    * Geocode helper
    */
   var geoCodeExists = document.getElementById("geocode");
   if (geoCodeExists) {
    const geocoder = new google.maps.Geocoder();
    document.getElementById("geocode").addEventListener("click", () => {
        geocodeAddress(geocoder, map);
    });
   }

}

function geocodeAddress(geocoder, resultsMap) {
    const address = document.getElementById("address").value;
    geocoder.geocode({ address: address }, (results, status) => {
        if (status === "OK") {

            /*
            * Draggable marker
            */
            resultsMap.setCenter(results[0].geometry.location);

            initMarkerDraggable(resultsMap, results[0].geometry.location)

        } else {
        alert(
            "Geocode was not successful for the following reason: " + status
        );
        }
    });
}


