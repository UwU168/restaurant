
# Sample run

# Enter name of restaurant: Taco Bell
# Enter type of restaurant(Italian, Fast food, Pizza, etc): fast food
# Enter a rating from 1-5: 3

# Name             Type        Rating      
# ----------       -----       -----      
# taco bell       fast food      3         

# Goodbye!

import valid as v


class Restaurant:
    __name__ = ""
    __type__ = ""
    __rating__ = 0
    
    # constructor method
    def __init__(self, n, t, r):
        self.__name__ = n
        self.__type__ = t
        self.__rating__ = r

    def get_name(self):
      return self.__name__

    def get_type(self):
      return self.__type__

    def get_rating(self):
      return self.__rating__

    def set_name(self, n):
      self.__name__ = n

    def set_type(self, t):
      self.__type__ = t

    def set_rating(self, r):
      self.__rating__ = r
    
      
    # Add the getter (accessor) methods


    # Add the setter (mutator) methods

        
def main():
    name = ""
    type = ""
    rating = 0
    

    name = v.get_string("Enter name of restaurant: ")
    type = v.get_string("Enter type of restaurant(Italian, Fast food, Pizza, etc): ")
    rating = get_rating()

    restaurant = Restaurant(name, type, rating)
    print_restaurant(restaurant) 

    
def print_restaurant(restaurant):
    print("\n{: <20} {: <20} {: <20}".format("Name", 
                                           "Type", 
                                           "Rating"))
                                            
    print("{: <20} {: <20} {: <20}".format("-------", 
                                           "-------", 
                                           "-------"))
    print("{: <20} {: <20} {: <20}".format(restaurant.get_name(),
                                          restaurant.get_type(),
                                          restaurant.get_rating()))





    # ask user to enter a new name for the restaurant
  
    name = v.get_string("\nEnter a new name: ") 
    restaurant.set_name(name)
    # ask user to enter a new type for the restaurant
    type = v.get_string("Enter a new type: ")
    restaurant.set_type(type)
    # ask user to enter a new rating for the restaurant
    rating = get_rating()
    restaurant.set_rating(rating)
    print_restaurant(restaurant)
    print("\nGoodbye!")






  
def get_rating():
  rating = 0
  rating = v.get_integer("Enter a rating from 1-5: ")
  if rating <1 or rating > 5:
    print("Invalid input.")
    rating = v.get_integer("Enter a rating from 1-5: ")
  else:
    return rating


def get_name():
  name = ""
  name = name = v.get_string("Enter name of restaurant: ")
  return name


def get_type():
  type = ""
  type = v.get_string("Enter type of restaurant(Italian, Fast food, Pizza, etc): ")
  return type


          
main()