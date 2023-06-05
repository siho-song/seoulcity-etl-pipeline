function redirectToService() {
    var hotspotElement = document.getElementById("hotspot-select").value;
    var serviceElement = document.getElementById("service-select").value;
    var url = `http://localhost:5000/${hotspotElement}/${serviceElement}`;
    console.log(url)
    window.location.href = url;
}