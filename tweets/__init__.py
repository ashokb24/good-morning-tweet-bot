from __future__ import print_function

from twython import Twython
from newsapi import NewsApiClient
from datetime import datetime

# data = ['Ashok' , 'punya']
# print(*data, sep=' ')
# print(' '.join(map(str, data)))



APP_KEY = 'LEWS4xJBnxU4ADye1RjYfdaun'  # Customer Key here
APP_SECRET = '7sl4AuezLZKajlWf3A0kSyEv4hB9Mi4rJM6mA8QVfORf31nlha'  # Customer secret here
OAUTH_TOKEN = '840889837-uxyFan2Rxhw0PJK6XR2R1Mj4aI2udRUCazbPGfYI'  # Access Token here
OAUTH_TOKEN_SECRET = 'b05lANLr183Oez0WhN7hcXGQy1Wr9dTOq2AFrIVoCcKkt'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# Init
newsapi = NewsApiClient(api_key='48acc486dc144de5a7213adeecbb97da')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources='the-times-of-india',
                                              language='en',
                                              page_size=3)
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources='the-times-of-india',
                                          language='en',
                                          page_size=2)
print(top_headlines)
headlines_list = ['TOP HEADLINES : Courtesy : TOI \n']
for head_line in top_headlines["articles"]:
    # headlines_list.append(str(head_line['title']).lstrip(',').rstrip(',')+'\n')
    headlines_list.append(str(head_line['url'])+'\n')

print(headlines_list)
twitter.update_status(status=' '.join(map(str, headlines_list)))

#twitter.update_status(status=headlist_list)
# /v2/sources
# sources = newsapi.get_sources()
#
# # print(sources)