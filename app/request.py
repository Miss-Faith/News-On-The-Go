import urllib.request,json
from .models import Source

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