from __future__ import print_function

from datetime import datetime
import os
from twython import Twython
from newsapi import NewsApiClient
import json


def tweet_top_head_lines(event, context):
    event_string = json.dumps(event)
    data = json.loads(event_string)
    source_name = data['source']

    news_api = NewsApiClient(api_key=os.environ['NEWSAPI_API_KEY'])

    # /v2/top-headlines
    top_headlines = news_api.get_top_headlines(sources=source_name,
                                               language='en',
                                               page_size=1)
    headlines_list = ['FROM MY PERSONAL BOT ASSISTANT : Courtesy :' + source_name + '\n']
    for head_line in top_headlines["articles"]:
        headlines_list.append(str(head_line['url'])+'\n')

    app_key = os.environ['CONSUMER_KEY']
    app_secret = os.environ['CONSUMER_SECRET']
    oauth_token = os.environ['OAUTH_TOKEN']
    oauth_token_secret = os.environ['OAUTH_TOKEN_SECRET']

    twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

    twitter.update_status(status=' '.join(map(str, headlines_list)))

    return "BOT FINISHED SENDING THE TOP HEADLINES " + str(datetime.now())
