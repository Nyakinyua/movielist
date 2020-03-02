import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class that tests the behaviour o the movie class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
    self.new_movie = Movie(i234,'Python101','A thrilling encounter in python','image.jpg',8.9,12345)
    
    def test_instance(self):
        sel.assertTrue(isinstance(self.new_movie,Movie))
        
    
if __name__ == '__main__':
    unittest.main()