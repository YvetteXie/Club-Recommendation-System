"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_friend(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_02_one_person_empty(self):
        param = {'Alex Dunphy': []}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)
    
    def test_03_one_person_one_club(self):
        param = {'Alex Dunphy': ['Orchestra']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)
        
    def test_04_one_person_multiple_clubs(self):
        param = {'Alex Dunphy': ['Orchestra', 'Chess Club', 'Smash Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)

    def test_05_two_people_two_clubs_each(self):
        param = {'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
                 'Joey Gladstone': ['Comics R Us', 'Parent Council']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)
        
    def test_06_two_people_different_numbers_of_clubs(self):
        param = {'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
                 'Michelle Tanner': ['Comet Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)
                                                    
    def test_07_three_people_four_clubs(self):
        param = {'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
                 'Michelle Tanner': ['Comet Club'], 
                 'Danny R Tanner': ['Parent Council']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.3333333333333333
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)
        
    def test_08_P2C(self):
        P2C = {'Michelle Tanner': ['Comet Club'],
               'Danny R Tanner': ['Parent Council'],
               'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
               'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
               'Joey Gladstone': ['Comics R Us', 'Parent Council']}
        actual = club_functions.get_average_club_count(P2C)
        expected = 1.6
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)
    
    def test_09_from_file(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'], 
                 'Manny Delgado': ['Chess Club'], 
                 'Mitchell Pritchett': ['Law Association'], 
                 'Alex Dunphy': ['Chess Club', 'Orchestra'], 
                 'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'], 
                 'Phil Dunphy': ['Real Estate Association'], 
                 'Gloria Pritchett': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.2857142857142858
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual,expected,msg=msg)

        
if __name__ == '__main__':
    unittest.main(exit=False)
