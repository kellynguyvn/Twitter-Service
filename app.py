from requests_oauthlib import OAuth1Session
import json

# Load API keys and tokens from JSON file
with open('secrets.json', 'r') as f:
    secrets = json.load(f)

API_KEY = secrets['API_KEY']
API_SECRET_KEY = secrets['API_SECRET_KEY']
ACCESS_TOKEN = secrets['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = secrets['ACCESS_TOKEN_SECRET']

# Create an OAuth1 session
twitter = OAuth1Session(API_KEY,
                        client_secret=API_SECRET_KEY,
                        resource_owner_key=ACCESS_TOKEN,
                        resource_owner_secret=ACCESS_TOKEN_SECRET)

# URLs for tweet actions
tweet_url = "https://api.twitter.com/2/tweets"
delete_url_template = "https://api.twitter.com/2/tweets/{id}"


# Function to create a tweet
def create_tweet(text):
    headers = {'Content-type': 'application/json'}
    payload = {"text": text}
    response = twitter.post(tweet_url, headers=headers,
                            json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    if response.status_code == 201:
        tweet_data = response.json()
        return tweet_data['data']['id'], tweet_data
    else:
        return None, response.json()


# Function to delete a tweet
def delete_tweet(tweet_id):
    delete_url = delete_url_template.format(id=tweet_id)
    response = twitter.delete(delete_url)
    if response.status_code == 204:
        return True
    else:
        return False, response.json()


# Main function
def main():
    print("Hello, world! This is a Twitter bot.")


# Execute the main function
if __name__ == "__main__":
    main()
