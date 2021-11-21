

function geol(){
    navigator.geolocation.getCurrentPosition(showlocation)
}

function showlocation(loc){
    let x = `Latitude is ${loc.coords.latitude}, Longitude is ${loc.coords.longitude}`
    document.getElementById("loc").innerHTML = x
    var lat = loc.coords.latitude
    var long = loc.coords.longitude
    


    function initMap() {
        const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: { lat:lat, lng: long },
        });

        const geocoder = new google.maps.Geocoder();
        const infowindow = new google.maps.InfoWindow();
    
        document.getElementById("submit").addEventListener("click", () => {
        geocodeLatLng(geocoder, map, infowindow);
        });
    }
    
    function geocodeLatLng(geocoder, map, infowindow) {
        const input = "lat,long";
        const latlngStr = input.split(",", 2);
        const latlng = {
        lat: parseFloat(latlngStr[0]),
        lng: parseFloat(latlngStr[1]),
        };
    
        geocoder
        .geocode({ location: latlng })
        .then((response) => {
            if (response.results[0]) {
            map.setZoom(11);
    
            const marker = new google.maps.Marker({
                position: latlng,
                map: map,
            });
    
            infowindow.setContent(response.results[0].formatted_address);
            infowindow.open(map, marker);
            } else {
            window.alert("No results found");
            }
        })
        .catch((e) => window.alert("Geocoder failed due to: " + e));
    }
}