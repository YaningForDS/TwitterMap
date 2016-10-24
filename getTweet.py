from sys import stdout
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from elasticsearch import Elasticsearch
import json
import time
import certifi


class TwittMapListener(StreamListener):


    def on_data(self, data):
        try:
            received_data = json.loads(data)
            decode_geo = received_data['geo']['coordinates']
            print json.dumps({'lat':decode_geo[0],'lng':decode_geo[1]})
            if decode_geo:
                tweet = {
                    'user': received_data['user']['screen_name'],
                    'text': received_data['text'],
                    'geo': decode_geo,
                }
                print tweet
                ##tweet_id = received_data['id_str']
                postURL = 'http://search-twittermap-gbp4jwsnk7jh23j5vrg6fc76da.us-west-2.es.amazonaws.com/tweeter/tweet'
                r = requests.post(postURL,json = tweet)
            stdout.flush()

        except:
            pass
        return True
    def on_error(self, status):
        print status


if __name__ == '__main__':

        es = Elasticsearch()
        ls = TwittMapListener()

        auth = OAuthHandler("5TMjXH2lj0lmbY9c9kOppDNZ2", "VFyJRCCs9ZUhSdX00P9JnmilphRWx5zf4p5a70mIvhhPRbTQRI")
        auth.set_access_token("789846826098814976-iJwCeojyx8V0e4zVb2HikywjwkjYbp6", "jMJRW6F1RVooCwhyEeKQxW4SRquyY6eKDPHFAUAAydOqq")

        stream = Stream(auth, ls)
        # stream.filter(locations=[-180, -90, 180, 90], async=False)
        stream.filter(track=['love','Trump','Lufy','Like','Food','China','America','hate','Burger','Fries'])


