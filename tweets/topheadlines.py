from __future__ import print_function

from datetime import datetime
import os
from twython import Twython
from newsapi import NewsApiClient
import json
import boto3


def tweet_top_head_lines(event, context):
    event_string = json.dumps(event)
    data = json.loads(event_string)
    source_name = data['source']

    # calling the method to read the twitter secret from S3
    secret_bag = read_twitter_secrets_from_s3(bucket_name=os.environ['AUTO_RETWEET_BUCKET'],
                                              file_name=os.environ['FILE_NAME'],
                                              region_name=os.environ['S3_REGION'])

    news_api = NewsApiClient(api_key=secret_bag['newsapi_api_key'])

    # /v2/top-headlines
    top_headlines = news_api.get_top_headlines(sources=source_name,
                                               language='en',
                                               page_size=1)
    headlines_list = ['FROM MY PERSONAL BOT ASSISTANT : Courtesy :' + source_name + '\n']
    for head_line in top_headlines["articles"]:
        headlines_list.append(str(head_line['url'])+'\n')

    if len(top_headlines["articles"]) > 0:
        app_key = secret_bag['consumer_key']
        app_secret = secret_bag['consumer_secret']
        oauth_token = secret_bag['oauth_token']
        oauth_token_secret = secret_bag['oauth_token_secret']

        twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
        twitter.update_status(status=' '.join(map(str, headlines_list)))
        lambda_return_status = "BOT FINISHED SENDING THE TOP HEADLINES " + str(datetime.now())
    else:
        lambda_return_status = "NO UPDATED HEADLINES FROM NEWS API WHEN ATTEMPTED AT " +str(datetime.now())

    return lambda_return_status


def read_twitter_secrets_from_s3(bucket_name=None, file_name=None, region_name=None):
    s3client = boto3.client('s3', region_name=region_name)
    # Create a file object using the bucket and object key.
    fileobj = s3client.get_object(Bucket=bucket_name, Key=file_name)
    # open the file object and read it into the variable filedata.
    filedata = fileobj['Body'].read()
    # file data will be a binary stream.  We have to decode it
    contents = filedata.decode('utf-8')
    # return the json object
    return json.loads(contents)
