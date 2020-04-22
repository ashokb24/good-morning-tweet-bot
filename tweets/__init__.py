from newsapi import NewsApiClient

source_name = 'the-times-of-india'
news_api = NewsApiClient(api_key='48acc486dc144de5a7213adeecbb97da')

# /v2/top-headlines
top_headlines = news_api.get_top_headlines(sources=source_name,
                                       language='en',
                                       page_size=1)
headlines_list = ['FROM MY PERSONAL BOT ASSISTANT : Courtesy :' + source_name + '\n']
for head_line in top_headlines["articles"]:
    headlines_list.append(str(head_line['url'])+'\n')

if len(top_headlines["articles"]) > 0:
    print(headlines_list)
    print('update twitter status')