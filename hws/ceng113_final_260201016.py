# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:21:03 2021

@author: fatih
"""

    

class Population:
    def __init__(self,size,name):
        self.growth_rate = 1
        self.size = size
        self.name = name
        print(self.name,"population of size",self.size)
    def set_growth_rate(self,a):
        self.growth_rate = a
        print("growth rate is set to",a)
    def calc_growth(self,year):
        if year > 1:
            return self.size * self.growth_rate + self.calc_growth(year-1)
        else:
            return self.size
    
    def grow(self,year):
        if year > 1:
            self.size = self.size * self.growth_rate
            self.grow(year  - 1 )
        else:
            self.size = self.growth_rate * self.size
    def shrink(self,num):
        self.size -= num
my_pop = Population(100,"bear")
my_pop.set_growth_rate(2)
print(my_pop.calc_growth(5))
my_pop.grow(3)
my_pop.shrink(300)









