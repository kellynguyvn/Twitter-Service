# Function to test the functions
from app import create_tweet, delete_tweet
import time


def tests():
    tweet_id, tweet_data = create_tweet(f"Hello, world!{time.time()}")
    if tweet_id:
        print(f"Tweet created: {tweet_data}")

        # Delete the tweet
        if delete_tweet(tweet_id):
            print(f"Tweet {tweet_id} deleted successfully.")
        else:
            print(f"Failed to delete tweet {tweet_id}.")
    else:
        print("Failed to create tweet.")


if __name__ == "__main__":
    tests()
