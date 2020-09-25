import unittest
from flask import current_app
from app import create_app
from app.models import Pizza,Toppings,Size,Flavor


class PizzaTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pizza class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pizza = Pizza(1234, 'Python Must Be Crazy','A thrilling new Python Flavor)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pizza, Pizza))
