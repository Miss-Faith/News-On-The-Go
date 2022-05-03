import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("cnn","CNN","Rocío Muñoz-Ledo","Gustavo Petro suspende campaña en el eje cafetero por razones de seguridad","En Colombia, el candidato presidencial Gustavo Petro suspendió las actividades de este martes y miércoles en Quindío y Risaralda por seguridad","https://cnnespanol.cnn.com/2022/05/02/colombia-petro-suspende-campana-eje-cafetero-razones-seguridad-orix/","https://cnnespanol.cnn.com/wp-content/uploads/2022/05/gustavo-petro.jpg?quality=100&strip=info")

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))

    def test_save_article(self):
        '''
        Test to check if instance variables are saved
        '''
        self.new_article.save_article()
        self.assertTrue(len(Article.all_articles),1)


if __name__ == '__main__':
    unittest.main()