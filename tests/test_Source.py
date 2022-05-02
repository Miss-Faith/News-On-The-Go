import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("","WISHTV.com","Monday's business headlines - WISH TV Indianapolis, IN","INDIANAPOLIS (WISH) — Heres a look at Mondays business headlines […]","https://www.wishtv.com/news/business/mondays-business-headlines-187/","https://www.wishtv.com/wp-content/uploads/2022/05/GettyImages-1239968068.jpg","2022-05-02T13:41:58Z")

    def test_instance(self):
        '''
        Test to check creation of new article Source instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()