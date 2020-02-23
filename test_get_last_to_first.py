"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_02_one_person_one_friend_diff_last(self):
        param = {'Clare Dunphy': ['Michelle Tanner']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Tanner': ['Michelle']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_03_one_person_no_friends(self):
        param = {'Clare Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_04_mutual_friends(self):
        param = {'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
                 'Kimmy Gibbler': ['Rebecca Donaldson-Katsopolis']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Donaldson-Katsopolis': ['Rebecca'], 
                    'Gibbler': ['Kimmy']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_05_one_person_two_friends_diff_last(self):
        param = {'Danny R Tanner': ['Jesse Katsopolis', 'Joey Gladstone']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Gladstone': ['Joey'], 'Katsopolis': ['Jesse'], 
                    'Tanner': ['Danny R']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
    def test_06_two_people_mix(self):
        param = {'Luke Dunphy': ['Gloria Pritchett', 'Alex Dunphy'], 
                 'Cameron Tucker': ['Gloria Pritchett', 'Manny Delgado']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Delgado': ['Manny'], 'Dunphy': ['Alex', 'Luke'],
                    'Pritchett': ['Gloria'], 'Tucker': ['Cameron']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)          

    def test_07_P2F(self):
        P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
               'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
               'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
               'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                                  'Joey Gladstone']}
        actual = club_functions.get_last_to_first(P2F)
        expected = {'Katsopolis': ['Jesse'], 
                    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'], 
                    'Gladstone': ['Joey'], 'Donaldson-Katsopolis': ['Rebecca'], 
                    'Gibbler': ['Kimmy'], 'Tanner-Fuller': ['DJ']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_08_from_file(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado', 
                                   'Claire Dunphy'],
                 'Claire Dunphy': ['Phil Dunphy', 'Mitchell Pritchett', 
                                   'Jay Pritchett'],
                 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 
                                   'Luke Dunphy'],
                 'Mitchell Pritchett': ['Claire Dunphy', 'Cameron Tucker', 
                                        'Luke Dunphy'],
                 'Alex Dunphy': ['Luke Dunphy'],
                 'Cameron Tucker': ['Mitchell Pritchett', 'Gloria Pritchett'],
                 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
                 'Phil Dunphy':['Claire Dunphy', 'Luke Dunphy'],
                 'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],
                 'Gloria Pritchett': ['Jay Pritchett', 'Cameron Tucker', 
                                      'Manny Delgado'],
                 'Luke Dunphy': ['Manny Delgado', 'Alex Dunphy', 'Phil Dunphy', 
                                 'Mitchell Pritchett']
                 }
        actual = club_functions.get_last_to_first(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell'], 
                    'Dunphy': ['Alex', 'Claire', 'Haley Gwendolyn', 'Luke',
                               'Phil'], 'Delgado': ['Manny'], 
                    'Tucker': ['Cameron'], 'D-Money': ['Dylan'], 
                    'D-Cat': ['Chairman', 'Gilbert']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
if __name__ == '__main__':
    unittest.main(exit=False)
