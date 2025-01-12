# import inspect
#
# import requests

#
# help(requests)
# print(requests.__cake__)
# print(requests.__url__)
#
#
#
#
# class SomeClass:
#     def __init__(self):
#         self.attr_1 = 50
#
#     def some_class_method(self, value):
#         self.attr_1 = value
#         print(self.attr_1)
#
#
# some_obj = SomeClass()
#
# pprint(dir(some_obj))
# # hasattr()
# print(hasattr(some_obj, 'attr_1'))
# #getattr()
# print(getattr(some_obj, 'attr_1'))
#
# print(help(getattr))
#
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests))

import sys
from pprint import pprint

#
# pprint(dir(sys))
# print(help(sys))
#
# #путь к интерпретатору python
# print(sys.version)

pprint(dir(__builtins__))

