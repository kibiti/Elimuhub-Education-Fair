# Islamic Center Venue Map

```html
<!DOCTYPE html>
<html>
<head>
  <title>ElimuHub Fair Map</title>
  <script src='https://api.mapbox.com/mapbox-gl-js/v2.9.1/mapbox-gl.js'></script>
  <link href='https://api.mapbox.com/mapbox-gl-js/v2.9.1/mapbox-gl.css' rel='stylesheet' />
  <style>
    #map { position: absolute; top: 0; bottom: 0; width: 100%; }
  </style>
</head>
<body>
  <div id="map"></div>
  
  <script>
    mapboxgl.accessToken = 'YOUR_MAPBOX_TOKEN';
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [36.8219, -1.2921], // Nairobi Coords
      zoom: 16
    });
    
    // Add institution booths
    const booths = [
      {name: 'Al-Azhar', lng: 36.820, lat: -1.291},
      {name: 'IIUM', lng: 36.822, lat: -1.293},
      {name: 'Darul Uloom', lng: 36.824, lat: -1.290}
    ];
    
    booths.forEach(booth => {
      new mapboxgl.Marker()
        .setLngLat([booth.lng, booth.lat])
        .setPopup(new mapboxgl.Popup().setHTML(`<b>\${booth.name}</b>`))
        .addTo(map);
    });
  </script>
</body>
</html>
