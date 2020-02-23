""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions 

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []
        
    if value not in key_to_values[key]:
        key_to_values[key].append(value)


# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from profiles_file.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.
    """
    individuals = [[]]
    sublist = 0
    content = profiles_file.readlines()
    for i in content:
        if i != '\n':
            individuals[sublist].append(i)
        else:
            sublist += 1
            individuals.append([])
    return sort_profile(individuals)

#helper function
def sort_profile(individuals: List[List[str]]) -> Tuple[Dict[str, List[str]],
                                                        Dict[str, List[str]]]:
    """
    Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary by sorting the str in individuals.
    
    >>> sort_profile([['Dunphy, Alex\n', 'Orchestra\n', 
                     'Chess Club\n', 'Dunphy, Luke\n'], 
                     ['Scrooge, McDuck\n']])
    ({'Alex Dunphy': ['Luke Dunphy']},
     {'Alex Dunphy':['Orchestra', 'Chess Club']})
    """
    person_to_friends = {}
    person_to_clubs = {}
    for i in individuals:
        if len(i) > 1:
            for j in range(1, len(i)):
                if ',' in i[j]:
                    update_dict(name_formatting(i[0]), name_formatting(i[j]), 
                                person_to_friends)
                else:
                    update_dict(name_formatting(i[0]), i[j].rstrip(),\
                                person_to_clubs)
    for person in person_to_friends:
        person_to_friends[person].sort()
    for person in person_to_clubs:
        person_to_clubs[person].sort()    
    return (person_to_friends, person_to_clubs)

# A helper function that helps converting the names into correct format
def name_formatting(name: str) -> str:
    """
    Return a str in the form of 'first name last name' by converting
    name, which is in the form of "last name, first name'.
    
    Pre-condition: The last name is non-empty and only consist of one word, and
    the first name is also non-empty but consist of one or more words separated 
    by space.
    
    >>> name_formatting('Mandela, Nelson')
    'Nelson Mandela'
    >>> name_formatting('Gandhi, Mohandas K.')
    'Mohandas K. Gandhi'
    """
    
    first_name = name.rstrip()[name.find(',') + 2 : ]
    last_name = name[ : name.find(',')]
    return first_name + ' ' + last_name


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    """
    
    total = 0.0
    if len(person_to_clubs) == 0:
        return total
    for person in person_to_clubs:
        total += len(person_to_clubs[person])
    return total/len(person_to_clubs)


def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    """
    
    last_to_first = {}
    for person in person_to_friends:
        update_dict(person[person.rfind(' ') + 1: ],\
                    person[ :person.rfind(' ')], last_to_first)
        for i in person_to_friends[person]:
            update_dict(i[i.rfind(' ') + 1: ], i[ :i.rfind(' ')], last_to_first)
    for last_name in last_to_first:
        last_to_first[last_name].sort()
    return last_to_first


def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value. The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    """
    
    inverted_key_value = {}
    for key in key_to_value:
        if type(key_to_value[key]) == list:
            for i in key_to_value[key]:
                update_dict(i, key, inverted_key_value)
        else:
            update_dict(key_to_value[key], key, inverted_key_value)
    for i in inverted_key_value:
        inverted_key_value[i].sort()
    return inverted_key_value


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    """
    
    clubs_of_friends = []
    if person not in person_to_friends:
        return []
    for friends in person_to_friends[person]:
        if friends in person_to_clubs:
            for clubs in person_to_clubs[friends]:
                if (person not in person_to_clubs) or \
                    (clubs not in person_to_clubs[person]):
                    clubs_of_friends.append(clubs)
    clubs_of_friends.sort()
    return clubs_of_friends


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """
    
    club_to_person = invert_and_sort(person_to_clubs)
    recommendation = []
    for club in club_to_person:
        if club in get_clubs_of_friends(person_to_friends, person_to_clubs,\
                                        person) or \
           person not in club_to_person[club]:
            score = 0
            score += first_way(person_to_friends, person_to_clubs, \
                               club_to_person, person, club)
            score += second_way(person_to_clubs, club_to_person, person, club)
            if score > 0:
                recommendation.append((club, score))
    sorting(recommendation)
    return recommendation


def first_way(person_to_friends: Dict[str, List[str]],
              person_to_clubs: Dict[str, List[str]],
              club_to_person: Dict[str, List[str]], person: str, 
              club: str) -> int:
    """Return an int representing the score gained by the counting the number
    of friends of person in club by going through person_to_friends and 
    person_to_clubs.
    
    >>>first_way(P2F, P2C, "Jesse Katsopolis", 'Comics R Us')
    1
    
    """
    score = 0
    if club in get_clubs_of_friends(person_to_friends, person_to_clubs,\
                                        person):
        for member in club_to_person[club]:
            if person in person_to_friends and \
               member in person_to_friends[person]:
                score += 1
    
    return score


def second_way(person_to_clubs: Dict[str, List[str]], 
               club_to_person: Dict[str, List[str]], 
               person: str, club: str) -> int:
    """Return an int representing the score gained by another way, which is
    adding one point for every member of club that is in at least 
    one different club with person after searchinging through person_to_friends 
    and person_to_clubs.
    
    >>>second_way(P2F, P2C, 'Stephanie J Tanner', 'Smash Club')
    0
    
    """
    score = 0
    if person not in person_to_clubs:
        return score
    for member in club_to_person[club]:
        for diff_clubs in person_to_clubs[member]:
            if diff_clubs != club and diff_clubs in person_to_clubs[person]:
                score += 1
    return score

def sorting(recommendation: List[Tuple[str, int]]) -> None:
    """Sort items in recommendation from highest to lowest score. If multiple 
    clubs have the same score, they should be sorted alphabetically 
    (by the clubs' names).
    
    >>>recommendation = [('Smash Club', 1), ('Rock N Rollers', 2),\
                         ('Comet Club', 1)]
    >>>sorting(recommendation)
    >>>recommendation
    [('Rock N Rollers', 2),('Comet Club', 1), ('Smash Club', 1)]
    
    """
    
    for tup in range(len(recommendation)):
        score = recommendation[tup][1]
        alpha = recommendation[tup][0]
        for j in range(tup + 1, len(recommendation)):
            if recommendation[j][1] > score or \
               (recommendation[j][1] == score and recommendation[j][0] < alpha):
                recommendation[j], recommendation[tup] = recommendation[tup], \
                    recommendation[j]
        
        
if __name__ == '__main__':
    pass
    #import doctest
    #doctest.testmod()
