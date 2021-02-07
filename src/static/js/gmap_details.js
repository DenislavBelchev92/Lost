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
    });
}

function initMap() {
    const map_center = new google.maps.LatLng(-34.397, 150.644 )

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: map_center,
    });

    /*
    * Geocode helper
    */
    const geocoder = new google.maps.Geocoder();
    document.getElementById("geocode").addEventListener("click", () => {
        geocodeAddress(geocoder, map);
    });

    /*
    * Draggable marker
    */
    initMarkerDraggable(map, map_center)
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


