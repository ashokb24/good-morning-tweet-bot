# top-headline-tweet-bot

Automated Tweet Bot:

# Description:
This project has been created to automate some of the user context twitter tasks such as tweeting, re-tweeting, direct messages to a specific twitter user. The project is in the budding stage and the vision is to extend the project at the regular intervals.

# Solution Overview
The project is hosted on AWS Cloud infra in the form of serverless components. Automated tweet bot is a stateless software bot which meant to handle the below functionalities on behalf of the twitter user thereby reducing the work of twitter user spending time in opening the twitter app from his mobile app/ desktop application. There is a need to build a autoamted tweet bot so that it can be scheduled to invoke the twitter api on a daily basis at a specified time

# Use-Case Constraints
- Solution to be build in AWS Cloud
- Solution to be serverless
- Solution can use any open source library wherever applicable.

# Modules planned
- TopHeadLines Serverless service

# TopHeadLines Serverless Service
TopHeadLines Serverless service aims to retrieve a top headline from a configurable source name ( Eg: the-times-of-india) . For more information on the sources refer, https://newsapi.org/s/india-news-api
Service runs for every 30 mins and retrieve the top headline from a given news source.
newsapi provides a list of sources which newsapi.org supports and you can get the source information from newsapi python libary using the below code.

![Image description](images/SolutionV2.JPG)

Libraries and frameworks used
1. twython - open source python library to connect with Twitter
2. newsapi - open source python library to connect with newsapi.org
3. serverless framework - open source framework used to deploy and manage the serverless component ( in this case aws lambda )

# Using twython to integrate with twitter
- You should have a valid twitter account
- Register your twitter account with twitter developer portal (https://developer.twitter.com)
- Set up a twitter app in developer api portal. This step will give you the below credentials.
    1. Consumer Credentials: Below two secrets are sufficient in order to retrieve the twitter data
        a. Consumer Key 
        b. Consumer Key Secret
     2. API Secret & API Secret Token : The below two and the consumer credentials are required in order to tweet, re-tweet and wherever posting the data to twitter is concerned.
        a. API Secret
        b. API Secret Token
- I have written a separate Python project(https://github.com/ashokb24/s3-bucket-creator) to write these secrets to my own S3 bucket. Briefly, this project can
    1. Create a S3 Bucket
    2. Upload a file to a given path with AES-256 encryption
 
 Note: Whilst I will come up with a dedicated jenkins for my usage, I have used boto3 python package in this project to interact with S3 service.
- When you are calling the twitter endpoints, make sure you give priority for each end points Rate Limiting. Please refer the api reference of update_status rate limit. (https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update)
- For tweet and re-tweet including 300 requests per 3 hour window.
Python code to retrevies the secrets from S3
```python
    s3client = boto3.client('s3', region_name=region_name)
    fileobj = s3client.get_object(Bucket=bucket_name, Key=file_name)
    filedata = fileobj['Body'].read()
    contents = filedata.decode('utf-8')
```
Code to call Twython package to tweet a post
```python
        twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
        twitter.update_status(status='hi, myfirst tweet through twython')
```
# Using newsapi to integrate with newsapi.org
- Register to newsapi.org website and create an account
- Create an API Key to access the end points of newsapi.org.
- Install the newsapi python library using pip install command and mention the package name in requirements.txt so that serverless framework download the required package.
- See the below code snippet to call the newsapi. For more information on newsapi python library, refer https://github.com/mattlisiv/newsapi-python
- newsapi for developer profile, has a cap of 500 requests per day. So plan accordingly as per your needs.
```
    news_api = NewsApiClient(api_key=api_key=secret_bag['newsapi_api_key'])
    top_headlines = news_api.get_top_headlines(sources=source_name,
                                               language='en',
                                               page_size=1)
```


# Results
![Image description](images/Results.JPG)
