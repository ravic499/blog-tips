"""Module to explain Encapsulation in Python
"""
class SeeMe():
    """Class grouping the public, private varaibles and methods
    """
    def __init__(self):
    """Constructor
    """
    self.see_me = 'See Me' # public variable
    self._still_see_me = 'Still See Me !' # private varaible
    self.__cant_see_me = 'Cant See Me !!' # strictly private

    def can_see_me(self):
    """Public Method
    """
    return 'Can See Me'

    def __cant_see_me_method(self):
    """Private Method
    """
    return 'Cant See Me !!'

"""
Output:

check = SeeMe()

print(check.see_me)
See Me

print(check._still_see_me)
Still See Me

print(check.__cant_see_me)
#AttributeError: 'SeeMee' object has no attribute '__cant_see_me'

check.can_see_me()
Can See Me

check.__cant_see_me_method()
#AttributeError: 'SeeMee' object has no attribute '__cant_see_me_method'
"""

# Getters and Setters, Name Mangling - Explained
class Circle():
    """Class to calculate area of a circle
    """
    def __init__(self):
        """Constructor
        """
        self.__radius = 3

    def get_radius(self):
        """To get radius of a circle
        """
        return self.__radius

    def set_radius(self, radius):
        """To set radius of a circle
        """
        self.__radius = radius

    def calculate_area(self):
        """To calculate area of a circle 
        """
        return 3.14 * self.__radius * self.__radius

"""
Output

c = Circle()

# Name Mangling
print(_Circle__radius)
3

# Getters and Setters
c.get_radius()
3

c.calculate_area()
28.26

c.set_radius(4)

c.get_radius()
4

c.calculate_area()
50.24
"""
