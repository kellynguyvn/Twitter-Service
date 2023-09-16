from twitter_api import TwitterAPI

# Execute the main function
if __name__ == "__main__":
    twitter = TwitterAPI()
    tweet_id, tweet_data = twitter.create_tweet("Hello, world!")
    if tweet_id:
        print(f"Tweet created: {tweet_data}")

        # Delete the tweet
        if twitter.delete_tweet(tweet_id):
            print(f"Tweet {tweet_id} deleted successfully.")
        else:
            print(f"Failed to delete tweet {tweet_id}.")
    else:
        print("Failed to create tweet.")
