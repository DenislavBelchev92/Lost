let last_marker = null

function initMarker(map, position, is_draggable = true, is_form = 1) {

    /* Delete last marker so map has always only one marker*/
    if (last_marker) {
        last_marker.setMap(null)
    }
    const marker = new google.maps.Marker({
        position: position,
        draggable: is_draggable,
        map: map,
    });
    last_marker = marker

        const contentString = 'You can move to fine tune the location';
        let infoWindow = new google.maps.InfoWindow({
            content: contentString,
        });
        infoWindow.open(map, marker);

    
    if (is_form) {
        var positionObj = JSON.parse(JSON.stringify(position.toJSON(), null, 2));
        document.getElementById("id_latitude").value = positionObj.lat;
        document.getElementById("id_longitude").value = positionObj.lng;    
    }

        marker.addListener("drag", (mapsMouseEvent) => {
            // Close the current InfoWindow.
            infoWindow.close();
            // Create a new InfoWindow.
            infoWindow = new google.maps.InfoWindow({});
            infoWindow.setContent(
                JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
            );
            infoWindow.open(map, marker);
            if (is_form) {
                positionObj = JSON.parse(JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2));
                document.getElementById("id_latitude").value = positionObj.lat;
                document.getElementById("id_longitude").value = positionObj.lng;
            }

        });
}

function initMapTemplate(lat, long, tag_id = "map", draggable = true, is_form = true) {
    const map_center = new google.maps.LatLng(lat, long)

    const map = new google.maps.Map(document.getElementById(tag_id), {
        zoom: 14,
        center: map_center,
    });

    /*
    * Draggable marker
    */
    initMarker(map, map_center, draggable, is_form)

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

            initMarker(resultsMap, results[0].geometry.location , true, true)

        } else {
            alert(
                "Geocode was not successful for the following reason: " + status
        );
        }
    });
}


