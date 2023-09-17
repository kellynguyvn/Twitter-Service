document.addEventListener('DOMContentLoaded', function() {
    // Populate accounts when the page loads
    fetch('/api/getAccounts')
    .then(response => response.json())
    .then(data => {
        const accountSelect = document.getElementById('accountSelect');
        data.forEach(account => {
            const option = document.createElement('option');
            option.value = account;
            option.text = account;
            accountSelect.appendChild(option);
        });
    });
});

function createTweet() {
    const tweetText = document.getElementById('tweetText').value;
    const selectedAccount = document.getElementById('accountSelect').value;

    fetch('/api/createTweet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            tweetText: tweetText,
            account: selectedAccount
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            appendTweetToList(data.tweetId, tweetText);
        } else {
            alert('Failed to create tweet.');
        }
    });
}

function appendTweetToList(tweetId, tweetContent) {
    const listItem = document.createElement('li');
    listItem.innerHTML = `Tweet ID: ${tweetId}, Content: ${tweetContent} <button onclick="deleteTweet(${tweetId})">Delete</button>`;
    document.getElementById('tweetList').appendChild(listItem);
}

function deleteTweet(tweetId) {
    const selectedAccount = document.getElementById('accountSelect').value;

    fetch(`/api/deleteTweet/${tweetId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ account: selectedAccount })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Logic to remove the tweet from the list
        } else {
            alert('Failed to delete tweet.');
        }
    });
}
