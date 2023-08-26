document.getElementById('journalForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission
    
    const entryTitle = document.getElementById('entryTitle').value;
    const entryContent = document.getElementById('entryContent').value;
    const attachment = document.getElementById('attachment').files[0];
    const reminder = document.getElementById('reminder').value;

    const formData = new FormData();
    formData.append('title', entryTitle);
    formData.append('content', entryContent);
    formData.append('attachment', attachment);
    formData.append('reminder', reminder);
    
    // Send data to the backend
    fetch('/save-entry', {
        method: 'POST',
        body: JSON.stringify({ title: entryTitle, content: entryContent, attachment, reminder }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Handle response from the server
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
