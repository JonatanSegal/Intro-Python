class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self.__make
    @make.setter
    def make(self, make):
        if type(make) == str:
            self.__make = make
        else:
            print('Maker is not a string')

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def bhp(self):
        return self.__bhp
    @bhp.setter
    def bhp(self, bhp):
        if type(bhp) == int:
            self.__bhp = bhp
        else:
            print('Break horsepower is not a number')

    @property
    def mph(self):
        return self.__mph
    @mph.setter
    def mph(self, mph):
        if type(mph) == int:
            self.__mph = mph
        else:
            print('Mph is not a number')
