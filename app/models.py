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

    def __init__(self,id,name,author,title,description,url,urlToImage):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage

    def save_article(self):
        Article.all_articles.append(self)