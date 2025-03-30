navigator.geolocation.getCurrentPosition(pos => {
    const userLat = pos.coords.latitude;
    const userLng = pos.coords.longitude;

    const map = L.map('map').setView([userLat, userLng], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    L.marker([userLat, userLng]).addTo(map)
      .bindPopup("You are here").openPopup();

    fetch('/get_shelters', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ latitude: userLat, longitude: userLng })
    })
    .then(res => res.json())
    .then(data => {
        data.forEach(shelter => {
            L.marker([shelter.lat, shelter.lng])
              .addTo(map)
              .bindPopup(shelter.name);
        });
    });
});
