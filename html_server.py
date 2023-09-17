from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
from twitter_api import TwitterAPI

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    twitter = TwitterAPI()  # Create instance of your TwitterAPI class

    def do_POST(self):
        if self.path == "/create_tweet":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            tweet_id, tweet_data = self.twitter.create_tweet(data["text"])  # Use your TwitterAPI class
            
            self.send_response(201 if tweet_id else 400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if tweet_id:
                self.wfile.write(json.dumps({"id": tweet_id}).encode())
            else:
                self.wfile.write(json.dumps({"error": "Failed to create tweet"}).encode())
    
    def do_DELETE(self):
        if "/delete_tweet/" in self.path:
            tweet_id = self.path.split("/")[-1]
            
            success = self.twitter.delete_tweet(tweet_id)  # Use your TwitterAPI class
            
            self.send_response(200 if success else 400)
            self.end_headers()
            
            if success:
                self.wfile.write(b"Tweet deleted successfully.")
            else:
                self.wfile.write(b"Failed to delete tweet.")

if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
