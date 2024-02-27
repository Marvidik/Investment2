document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('accesspanel').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Retrieve form data
        const username = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Prepare data for sending to the backend as a dictionary
        const requestData = {
            username: username,
            password: password
        };

        // Fetch API to send the form data to your backend API
        fetch('http://127.0.0.1:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Store tokens and user information in localStorage or sessionStorage
            localStorage.setItem('token', data.token);
            localStorage.setItem('user', JSON.stringify(data.user));

            // Redirect to another page
            window.location.href = 'exchange.html'; // Replace 'next_page.html' with the URL of the page you want to redirect to
        })
        .catch(error => {
            // Handle error
            console.error('There was a problem with your fetch operation:', error);
            // Display an error message or do something else as per your requirement
        });
    });
});
