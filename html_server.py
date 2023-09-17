from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
from twitter_api import TwitterAPI

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    twitter = TwitterAPI()

    def _send_response(self, content):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(content).encode())

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/api/getAccounts':
            accounts = ["Account1", "Account2"]  # Replace with real account data
            self._send_response(accounts)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/api/createTweet':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            tweet_id, _ = self.twitter.create_tweet(data['tweetText'])
            if tweet_id:
                self._send_response({"success": True, "tweetId": tweet_id})
            else:
                self.send_error(400)

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/api/deleteTweet'):
            query = parse_qs(parsed_path.query)
            tweet_id = int(query.get('tweetId')[0])
            if self.twitter.delete_tweet(tweet_id):
                self._send_response({"success": True})
            else:
                self.send_error(400)
        else:
            self.send_error(404)

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
