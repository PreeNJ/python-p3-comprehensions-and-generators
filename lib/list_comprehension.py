#!/usr/bin/env python3

#def return_evens(num_list):
    #pass

#def make_exclamation(sentence_list):
    #pass
#!/usr/bin/env python3

def return_evens(num_list):
    """
    Given a sequence of integers, return a new list containing only the even ones.
    """
    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    """
    Given a list of strings, return a new list where each string has '!' appended.
    """
    return [s + "!" for s in sentence_list]
