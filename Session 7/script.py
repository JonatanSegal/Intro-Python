#Session 7 Encapsulation

#Class definition same as java class with getters and setters
#Classes always start with capital letter
class P:
    def __init__(self, name, alias):
        self.name = name #Public variable
        self.__alias = alias # __ makes it act as private

#2 methods used to change self.name from a public variable to a property
#Act as getter and setter to encapsulate Class P
# __ indicates private
    #@ = annotation, decorater
    @property #Getter
    def name(self):
    #Changed the name of name so it's a variable instead of a property
        return self.__name
    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            print('nonono')
