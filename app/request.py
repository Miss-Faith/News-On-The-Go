import urllib.request,json
from .models import Source

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_SOURCE_API_BASE_URL']
    search_url = app.config['NEWS_SEARCH_API_BASE_URL']

def get_Source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(api_key)
# print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results

  def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = movie_item.get('description')
        url = movie_item.get('url')
        category = movie_item.get('category')

        if poster:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results