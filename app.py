
from flask import Flask, render_template, request, jsonify
import twitter_api

twitter_api = twitter_api.TwitterAPI()

app = Flask(__name__)

# In-memory storage to store tweets
# Each tweet is a dictionary with 'id' and 'content' keys
tweets = []


# Serve the index.html file


@app.route("/")
def index():
    print(tweets)
    return render_template("index.html", tweets=tweets)

# Endpoint for creating a tweet


@app.route("/create", methods=['POST'])
def create_tweet():
    global twitter_api, tweets
    tweetText = request.form.get('tweetText')
    tweet_id, new_tweet = twitter_api.create_tweet_api(tweetText)
    tweets.append({"id": tweet_id, "content": tweetText})
    return index()

# Endpoint for deleting a tweet


@app.route("/delete/<int:tweet_id>", methods=['POST'])
def delete_tweet(tweet_id):
    global twitter_api, tweets
    id = str(tweet_id)
    deleted = twitter_api.delete_tweet_api(id)
    if not deleted:
        return jsonify({"message": f"Unable to delete tweet with ID: {tweet_id}"}), 400

    # delete tweet from in-memory storage
    for tweet in tweets:
        if str(tweet['id']) == id:
            tweets.remove(tweet)
            break

    return index()


if __name__ == "__main__":
    app.run(debug=True)
