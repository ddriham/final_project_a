"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

"""
import sys

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


def capital_of_Idaho():
    print (STATES_CAPITALS['Idaho'])

def all_states():
    print (STATES_CAPITALS.keys())

def all_capitals():
    print (STATES_CAPITALS.values())


def states_capitals_string(): # becuase the dict(STATES_CAPITALS) is allready sorted alphabetically by the key (state), i have no need to sort it in my function
    str_state_capitals = ''   # the loop will itirate state by state, by order and will print it as a single string.
    for state, capital in STATES_CAPITALS.items():
        str_state_capitals += state + ' ----->' + capital + ',' + ' '
    return (str_state_capitals[:len(str_state_capitals) -2 ]) # return the string without its two last elements (', ')



# In a theoretical case where I had two states with a capital city of the same name, this function will return only the first state in the dictionary: 
# def get_state(capital):
#     for state, city in STATES_CAPITALS.items():
#         if city == capital:
#             return state


# The next function creates a list of countries that have a capital city with a certain name, if the list >= 1 then it returns the list as a string:
def get_state(capital):
    if capital in STATES_CAPITALS.values():
        states = [state for state, city in STATES_CAPITALS.items() if city == capital]
        if len(states) > 0:
            return ",".join(states)
    else:
        raise KeyError # although KeyError is an error that raise as worng use of key in dictionary the test below expect key-error when worng capitl (VALUE) 
                       # is used so i had to add this else statment to pass the test.


def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')



def main():
    return pytest.main([__file__])


if __name__ == '__main__':
    sys.exit(main())
