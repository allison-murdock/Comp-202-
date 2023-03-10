#ALLISON MURDOCK
#MCGILL ID 261009978

#EXERCISE #2
def same_chars(my_string):
    ''' (str) -> bool
    Check whether all characters in my_string are eqaul.
    If they are all equal, return True. If not, return False
    >>> same_chars('hhhh')
    True
    >>> same_chars('ready')
    False
    >>> same_chars('zzZZ')
    False
    '''
    for char in my_string:
        if not char == my_string[0]:
            return False
    return True
# Check if the input itself is valid regardless dictionary

def valid_inputs(s):
    ''' (str) -> bool
    Check whether inputs are valid regardless dictionary
    >>> valid_inputs("222 33 777")
    True
    >>> valid_inputs(" 222 33 777 ")
    False
    >>> valid_inputs("2 22    333 777")
    False
    >>> valid_inputs("222 332 QwQ")
    False
    '''
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for ele in (s.split()):
        for char in ele:
            if not char in digit:
                return False
    if s[0] == ' ' or s[len(s) - 1] == ' ': # Check if input begins or ends with space characters
        return False
    if not len(s.split()) == len(s.split(' ')): # Check if input contains two or more consecutive space characters
        return False
    return True

def get_txt_msg(s, d):
    ''' (str, dict<int, str>)
    >>> map_one = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], 5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], 8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z'], 0: [' ']}
    >>> code = '222 666 3 444 66 4 0 444 7777 0 333 88 66'
    >>> msg = get_txt_msg(code, map_one)
    >>> msg
    'coding is fun'
    >>> map_two = {1: ['no', 'a', 'the'],2: ['child', 'senior','lady', 'man'], 3: ['eats', 'is', 'has'], 4: ['an', 'one', 'two'], 5: ["spaceship", "island"], 0: [' ']}
    >>> password = "1 0 2222 0 33 0 4 0 55"
    >>> get_txt_msg(password, map_two)
    'no man is an island'
    >>> d = {2 : ['A', 'B', 'c'], 7 : ['p', 'q', 'r', 'S']}
    >>> get_txt_msg('222 2 777', d)
    'cAr'
    '''
    if not valid_inputs(s):
        raise ValueError("Invalid input string")
    txt = ''
    for i, e in enumerate (s.split()):
        if not same_chars(e.split()):
            raise ValueError("Invalid input string")
        else:
            list_choice = d[int(e[0])] # The first str of s represent the key. list_choice extracts the object ['no', 'a', 'the'] based on the key given
            txt += list_choice[len(e)-1] # Use len() to check the number of occurrence after the first str. The idx will be the len - 1
    return txt