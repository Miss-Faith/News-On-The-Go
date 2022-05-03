class Source:
    '''
    Source class to define News Source
    '''

    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Article:

    all_articles = []

    def __init__(self,source_id,source_name,author,title,description,url,urlToImage):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage

    def save_article(self):
        Article.all_articles.append(self)