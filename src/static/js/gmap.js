let last_marker = null

function initMarker(map, marker_info, is_draggable = true, is_form = 1, unique = true) {
    /* Delete last marker so map has always only one marker*/
    if (unique) {
        if (last_marker) {
            last_marker.setMap(null)
        }
    }
    position = marker_info.LatLong
    beacon_id = marker_info.id

    var marker = new google.maps.Marker({
        position: position,
        draggable: is_draggable,
        map: map,
    });
    last_marker = marker

    if (is_form) {
        var positionObj = JSON.parse(JSON.stringify(position.toJSON(), null, 2));
        document.getElementById("id_latitude").value = positionObj.lat;
        document.getElementById("id_longitude").value = positionObj.lng;    

        let infoWindow

        const contentString = 'You can move to fine tune the location';
        infoWindow = new google.maps.InfoWindow({
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
            if (is_form) {
                positionObj = JSON.parse(JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2));
                document.getElementById("id_latitude").value = positionObj.lat;
                document.getElementById("id_longitude").value = positionObj.lng;
            }
        });
    }

    return marker

}

function initMapTemplate(markers, tag_id = "map", draggable = true, is_form = true, with_single_marker = true, zoom = 14) {
    var map_center
    if (Array.isArray(markers)) {
        map_center = markers[2].LatLong
    } else {
        map_center = markers.LatLong
    }

    map = new google.maps.Map(document.getElementById(tag_id), {
        zoom: zoom,
        center: map_center,
    });

    var marker;

    if (Array.isArray(markers)) {
        for (const marker_info of markers) {
            marker = initMarker(map, marker_info, draggable, is_form, false)
            google.maps.event.addListener(marker, 'click', (function (marker) {
                return function() {
                    document.getElementById(marker_info.id).style.color = "blue";
                }
             }) (marker) );
        }
    } else {
        initMarker(map, markers, draggable, is_form, with_single_marker)
    }

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

    return map

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
