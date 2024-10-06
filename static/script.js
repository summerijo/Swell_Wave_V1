const ctx = document.getElementById('swellWaveChart').getContext('2d');

// In this part, show only the specified location part
fetch('/data')
    .then(response => response.json())
    .then(data => {
        const timestamps = data.map(entry => new Date(entry.timestamp).toLocaleString());
        const swellWaveHeights = data.map(entry => entry.swell_wave_height);

        // Get the latitude and longitude from the first data entry
        const latitude = data.length > 0 ? data[0].latitude : 'N/A';
        const longitude = data.length > 0 ? data[0].longitude : 'N/A';

        // Display the latitude and longitude in the designated HTML elements
        document.getElementById('latitude').innerText = `Latitude: ${latitude}`;
        document.getElementById('longitude').innerText = `Longitude: ${longitude}`;
        
        const swellWaveChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamps,
                datasets: [{
                    label: 'Swell Wave Height',
                    data: swellWaveHeights,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    fill: true,
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Timestamp',
                            font: {
                                size: 12 // Adjust the font size of the x-axis title
                            }
                        },
                        ticks: {
                            font: {
                                size: 10 // Adjust the font size of the x-axis ticks
                            }
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Swell Wave Height (m)',
                            font: {
                                size: 10 // Adjust the font size of the y-axis title
                            }
                        },
                        ticks: {
                            font: {
                                size: 10 // Adjust the font size of the y-axis ticks
                            }
                        }
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching data:', error));
