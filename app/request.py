import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None

# Getting the source base url
source_url = None

# Getting the search base url
search_url = None

def configure_request(app):
    global api_key,source_url,search_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_SOURCE_API_URL']
    search_url = app.config['NEWS_SEARCH_API_URL']

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = source_url.format(api_key)
    #print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
            #print(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        if name:
            source_object = Source(id,name,description,url,category)
            source_results.append(source_object)

    return source_results

def get_article(id):
    get_search_url  = search_url.format(id,api_key)
    print(get_search_url)
    with urllib.request.urlopen(get_search_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_article_results(article_results_list)

    return article_results

def process_article_results(article_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        articles_results: A list of source objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')

        if url:
            article_object = Article(id,name,author,title,description,url,urlToImage)
            article_results.append(article_object)

    return article_results
