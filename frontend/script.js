fetch('http://middleware:5000/hello')
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('message').innerText = 'Failed to load message.';
    });
