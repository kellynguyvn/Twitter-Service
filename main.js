let lastTweetId = null;

async function createTweet() {
    const tweetText = document.getElementById("tweetText").value;
    const response = await fetch("http://localhost:8000/create_tweet", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: tweetText }),
    });

    const data = await response.json();
    const messageElement = document.getElementById("message");

    if (response.status === 201) {
        lastTweetId = data.id;
        messageElement.textContent = `Tweet ${lastTweetId} created successfully.`;
    } else {
        messageElement.textContent = "Failed to create tweet.";
    }
}

async function deleteTweet() {
    if (!lastTweetId) {
        alert("No tweet to delete.");
        return;
    }

    const response = await fetch(`http://localhost:8000/delete_tweet/${lastTweetId}`, {
        method: "DELETE",
    });

    const messageElement = document.getElementById("message");

    if (response.status === 200) {
        messageElement.textContent = `Tweet ${lastTweetId} deleted successfully.`;
        lastTweetId = null;
    } else {
        messageElement.textContent = "Failed to delete tweet.";
    }
}
