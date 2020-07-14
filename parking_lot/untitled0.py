# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:48:33 2020

@author: Manoj varma
"""


class Person:
  def __init__(self,name,age):
      self.name=name
      self.age=age      
        
  def func(self):
  	  print("my name is "+self.name)
p=Person("man",12)
p.func()