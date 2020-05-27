from django.test import TestCase

# Create your tests here.

class UselessTestCase(TestCase):
    ##runs each subclass of TestCase in isolation
    def setUp(self):
        ##set up the test here
        return
    def test_pointless(self):
        ##by default, the unittest constructs 
        #the testing suite with all functions that begin with test
        self.assertEqual(1,1)