let last_marker = null
let previousHighlightedBeaconID = null
let previousHighlightedBeaconExtraInfoID = null
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
/**
 * 
 * @param {*} markers 
 * @param {*} tag_id 
 * @param {*} draggable 
 * @param {*} is_form 
 * @param {*} with_single_marker 
 * @param {*} zoom 
 * @returns 
 */
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
                    var extra_info_id = marker_info.id.replace("beacon", "extra_info");

                    if (previousHighlightedBeaconID == null) {
                        uncollapsedArray = document.getElementsByClassName("in");
                        if (uncollapsedArray.length>1) {
                            previousHighlightedBeaconExtraInfoID = document.getElementsByClassName("in")[1].id;
                            previousHighlightedBeaconID = marker_info.id.replace("extra_info", "beacon");
                        }
                    }

                    if (previousHighlightedBeaconID != null) {
                        document.getElementById(previousHighlightedBeaconID).setAttribute("aria-expanded", "false");
                        document.getElementById(previousHighlightedBeaconID).classList.add("collapsed");
                        document.getElementById(previousHighlightedBeaconExtraInfoID).style.height="0%";
                        document.getElementById(previousHighlightedBeaconExtraInfoID).classList.remove("in");
                        document.getElementById(previousHighlightedBeaconExtraInfoID).setAttribute("aria-expanded", "false");

                    }

                    document.getElementById(marker_info.id).classList.remove("collapsed");
                    document.getElementById(marker_info.id).setAttribute("aria-expanded", "true");
                    document.getElementById(extra_info_id).style.height="100%";
                    document.getElementById(extra_info_id).classList.add("in");
                    document.getElementById(extra_info_id).setAttribute("aria-expanded", "true");

                    previousHighlightedBeaconID = marker_info.id
                    previousHighlightedBeaconExtraInfoID = extra_info_id

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
