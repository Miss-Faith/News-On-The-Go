class News_Source:
    '''
    News_Source class to define News_Source
    '''

    def __init__(self,source,title,description,url,urlToImage,publishedAt):
        self.source =source
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt