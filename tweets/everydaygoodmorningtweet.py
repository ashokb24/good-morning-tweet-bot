from datetime import datetime
import os
from twython import Twython


def saygoodmorningtweet(event, context):
    app_key = os.environ['CONSUMER_KEY']
    app_secret = os.environ['CONSUMER_SECRET']
    oauth_token = os.environ['OAUTH_TOKEN']
    oauth_token_secret = os.environ['OAUTH_TOKEN_SECRET']

    twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

    # The obligatory first status update to test
    twitter.update_status(status="Second Tweet From my bot!!!")

    return "bot wished good morning tweet on morning today at " + str(datetime.now())