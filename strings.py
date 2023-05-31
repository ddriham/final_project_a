"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest

the_string = 'monty pythons flying circus'
def no_duplicates(a_string):
    sort_monty = sorted(the_string)
    without_duplicates = ''
    for char in sort_monty:
        if char not in without_duplicates:
            without_duplicates += char
    return without_duplicates

print(no_duplicates(the_string))   


def reversed_words(a_string): # using list comprehension make a list of the string with split and returns the list backward using list slicing. one liner :)
    to_a_reversed_list = [item for item in a_string.split(' ')[::-1]] 
    return to_a_reversed_list

print (reversed_words(the_string))



def four_char_strings(a_string):
    result = []
    for i in range(0, len(the_string), 4):
        substring = the_string[i:i+4]
        result.append(substring)
    return result

print (four_char_strings(the_string))


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main([__file__])


if __name__ == '__main__':
    main()

