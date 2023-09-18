#File Written By: Neel Desai
# Path: test_backend.py
import unittest
import json
from twitter_api import TwitterAPI


class TestSecrets(unittest.TestCase):
    def test_secrets_file_exists(self):
        #test case to chek if the secrets file exists
        try:
            with open('secrets.json', 'r') as f:
                secrets = json.load(f)
            assert secrets is not None
        except FileNotFoundError:
            self.fail("File not found.")
        except:
            #some unexpected error
            self.fail("Unknown error.")

    def test_secrets_file_format(self):
        #test case to check if the secrets file is in json format
        try:
            with open('secrets.json', 'r') as f:
                secrets = json.load(f)
            assert type(secrets) == dict
        except FileNotFoundError:
            self.fail("File not found.")
        except:
            #some unexpected error
            self.fail("Unknown error.")
    
    def test_secrets_file_keys(self):
        #test case to check if the secrets file has all the required keys
        try:
            with open('secrets.json', 'r') as f:
                secrets = json.load(f)
            assert 'API_KEY' in secrets
            assert 'API_SECRET_KEY' in secrets
            assert 'ACCESS_TOKEN' in secrets
            assert 'ACCESS_TOKEN_SECRET' in secrets
        except FileNotFoundError:
            self.fail("File not found.")
        except:
            #some unexpected error
            self.fail("Unknown error.")
    
    def test_secrets_file_values(self):
        #test case to check if the secrets file has all the required values
        try:
            with open('secrets.json', 'r') as f:
                secrets = json.load(f)
            assert secrets['API_KEY'] is not None
            assert secrets['API_SECRET_KEY'] is not None
            assert secrets['ACCESS_TOKEN'] is not None
            assert secrets['ACCESS_TOKEN_SECRET'] is not None
        except FileNotFoundError:
            self.fail("File not found.")
        except:
            self.fail("One of the key has value none")
    
    def test_twitter_api(self):
        #test case to check if the twitter api is created successfully
        try:
            twitter = TwitterAPI()
            assert twitter is not None
        except:
            self.fail("Unknown error.")
    
    def test_tweet_create(self):
        #test case to check if the tweet is created successfully
        try:
            twitter = TwitterAPI()
            tweet_id, tweet_data = twitter.create_tweet_api("Hello, world!")
            assert tweet_id is not None
            #write this tweet_id to a file
            with open('test_tweet_id.txt', 'w') as f:
                f.write(str(tweet_id))
            
        except:
            self.fail("Unknown error.")
    
    def test_tweet_delete(self):
        #test case to check if the tweet is deleted successfully
        try:
            twitter = TwitterAPI()
            #read the tweet_id from the file
            with open('test_tweet_id.txt', 'r') as f:
                tweet_id = f.read()
            assert tweet_id is not None
            # Delete the tweet
            delete_status=twitter.delete_tweet_api(tweet_id)
            print(delete_status)
            if delete_status:
                print(f"Tweet {tweet_id} deleted successfully.")
            assert delete_status is True
        except:
            self.fail("Unknown error.")

if __name__ == '__main__':
    unittest.main()