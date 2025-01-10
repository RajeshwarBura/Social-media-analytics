document.getElementById('analyze-btn').addEventListener('click', async function () {
    const postType = document.getElementById('post-type').value;
    const engagementDataContainer = document.getElementById('engagement-data');

    // Send a request to your hosted backend
    const response = await fetch(`https://socialscope-frontend.onrender.com/analyze?postType=${postType}`);
    const data = await response.json();

    // Display the results
    if (data.error) {
        engagementDataContainer.innerHTML = `<p style="color: red;">${data.error}</p>`;
    } else {
        engagementDataContainer.innerHTML = `
            <p><strong>Average Likes:</strong> ${data.average_likes}</p>
            <p><strong>Average Shares:</strong> ${data.average_shares}</p>
            <p><strong>Average Comments:</strong> ${data.average_comments}</p>
            <p><strong>Insight:</strong> ${data.insight}</p>
        `;
    }
});
