"""
Module to explain Python's generator objects and yield keyword

Define a generator with a yield keyword, it as to add in a place
where the generator returns an intermediate result to the caller
and waits for the next invocation occurs.
"""


def search(keyword, filename):
    """To search for a given keyword in the given file

    Args:
        keyword  (str): Expected keyword
        filename (str): Actual file to search
    """
    print('Generator started')
    with open(filename, 'r') as fo:
        # Looping through the file line by line
        for line in fo.readlines():
            if keyword in line:
                # If keyword found, yield it
                yield line

"""
Let us search for a keyword called 'game' in the file 
'generator_and_yield.txt' and see how the generator 
actually works
"""
the_generator = search('game', 'generator_and_yield.txt')

"""
See nothing happened, this is because generator function used to
return the generator object to the caller, similar to a constructor

To make it actually search for a keyword, we must access it with the
next method
"""
print(next(the_generator))

# Let's try out for next match
print(next(the_generator))
