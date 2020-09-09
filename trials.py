"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Prints out a list of items"""

    for item in items:
        print(item)    
      

def get_all_evens(nums):
    """Prints out a list of all even numbers"""
    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

def get_odd_indices(items):
    """Prints out a list of odd indexed items"""
    
    result = []

    for item in items:
        if items.index(item) % 2 != 0:
            result.append(item)

    return result


def print_as_numbered_list(items):
    """Prints out a numbered list"""
    
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1
    
#Not using enumerate here because it prints out as 
#an enumerated list of tuples. This format matches JS example.


def get_range(start, stop):
    """Prints out array of numbers in a certain range"""
    
    nums = []

    while start <= stop:
        nums.append(start)
        start += 1
    
    return nums


def censor_vowels(word):
    """Prints out string where vowels are replaced with a '*' """
    
    chars = []


    for letter in word:
        if letter in "aeiou":
            chars.append("*")

        else:
            chars.append(letter)

    joined_letters = "".join(chars)
    
    return joined_letters


def snake_to_camel(string):
    """Prints out a string from snake case to camel case"""

    words = string.split()

    return words[0] + "".join(words[1].title() for word in words[1: ])


def longest_word_length(words):
    """Prints out the longest word length in a list of words"""
   
    for word in words:
        longest = len(words[0])

        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    """Prints out string without repeating characters"""

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return "".join(result)
 

def has_balanced_parens(string):
    """Returns true if all parentheses in a string are balanced"""
    
    parens = 0

    for char in string:
        if char == "(":
            parens += 1

        elif char == ")":
            parens -= 1

    if parens < 0 or parens > 0:
        return False

    else:
        return True


def compress(string):
    """Prints out compressed version of string"""

    compressed = []
    current_char = ''
    char_count = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)

            if char_count > 1:
                compressed.append(str(char_count))

            current_char = char
            char_count = 0

        char_count += 1
    
    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)


