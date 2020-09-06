"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Prints out a list of items"""

    for item in items:
        print(item)    
      


def get_all_evens(nums):
   
   even_nums = []

   for idx in nums:
        if idx % 2 == 0:
            even_nums.append(nnums[idx])

    return even_nums

def get_odd_indices(items):
    
    result = []

    for idx in items:
        if idx % 2 != 0:
            result.append(items[idx])

    return result




def print_as_numbered_list(items):
    
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1
    
#Not using enumerate here because it prints out as 
#an enumerated list of tuples. This format matches JS example.


def get_range(start, stop):
    
    nums = []

    while num == start:
        if num < stop:
            num +=1
            nums.append(num)


def censor_vowels(word):
    chars = []

    for letter in word:
        if 'aeiou' in letter:
            chars.append(*)


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
