const form = document.getElementById('submissionForm');
const statusDiv = document.getElementById('status');
const submitBtn = document.getElementById('submitBtn');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;

    // Reset status
    statusDiv.className = '';
    statusDiv.innerText = 'Submitting...';
    statusDiv.style.display = 'block';
    submitBtn.disabled = true;

    try {
        const response = await fetch('http://13.60.172.199:8000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, phone }),
        });

        const data = await response.json();

        if (response.ok) {
            statusDiv.innerText = 'Success! Data saved to database.';
            statusDiv.className = 'status-success';
            form.reset();
        } else {
            statusDiv.innerText = `Error: ${data.detail || 'Failed to submit'}`;
            statusDiv.className = 'status-error';
        }
    } catch (error) {
        statusDiv.innerText = 'Error: Connection failed. Is the backend running?';
        statusDiv.className = 'status-error';
        console.error('Fetch error:', error);
    } finally {
        submitBtn.disabled = false;
    }
});
