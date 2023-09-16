from requests_oauthlib import OAuth1Session
import json

class TwitterAPI:
    def __init__(self):
        self.API_KEY, self.API_SECRET_KEY, self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET = [None] * 4
        self.load_secrets()
        # URLs for tweet actions
        self.tweet_url = "https://api.twitter.com/2/tweets"
        self.delete_url_template = "https://api.twitter.com/2/tweets/{id}"
        self.twitter = self.create_oauth_session()

    def load_secrets(self)->None:
        # Load API keys and tokens from JSON file
        with open('secrets.json', 'r') as f:
            secrets = json.load(f)
            self.API_KEY = secrets['API_KEY']
            self.API_SECRET_KEY = secrets['API_SECRET_KEY']
            self.ACCESS_TOKEN = secrets['ACCESS_TOKEN']
            self.ACCESS_TOKEN_SECRET = secrets['ACCESS_TOKEN_SECRET']
        
    def create_oauth_session(self)->OAuth1Session:
        # Create an OAuth1 session
        twitter = OAuth1Session(self.API_KEY,
                        client_secret=self.API_SECRET_KEY,
                        resource_owner_key=self.ACCESS_TOKEN,
                        resource_owner_secret=self.ACCESS_TOKEN_SECRET)
        return twitter
        
    # Function to create a tweet
    def create_tweet(self,text): 
        headers = {'Content-type': 'application/json'}
        payload = {"text": text}
        response = self.twitter.post(self.tweet_url, headers=headers,
                                json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        if response.status_code == 201:
            tweet_data = response.json()
            return tweet_data['data']['id'], tweet_data
        else:
            return None, response.json()


    # Function to delete a tweet
    def delete_tweet(self,tweet_id):
        delete_url = self.delete_url_template.format(id=tweet_id)
        response = self.twitter.delete(delete_url)
        if response.status_code == 200:
            return True
        else:
            return False
