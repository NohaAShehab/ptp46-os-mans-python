
""
""" 1- import module """

"1.1 import module"
# import inputs_module
#
# print(inputs_module.ask_for_string("erer"))
### *************
# import iti.math_module
# print(iti.math_module.sum_num(32,23))

" alias module name "
# import  inputs_module as myin
# print(myin.ask_for_int("hello"))

# import iti.math_module as mm
# print(mm.sum_num(32,23))




""" 1- import part of the module  """

# from inputs_module import  ask_for_int
# from iti.math_module import  sum_num

# print(ask_for_int())
# print(sum_num(33,33))



"""
    main ?? --> in the module
    when you import module or part of the module --> if there are called blocks inside the imported 
    one it will be called automatically. 

"""

# import inputs_module
#
# from inputs_module import ask_for_string
#
# print(ask_for_string())


""" package with __init__ """

# import  os_track # will run content of __init__

# from os_track.validations import  validate_int
#
# print(validate_int(213213))

# from os_track import  validate_int
#
# print(validate_int(13213))

# import os_track

# import iti

from os_track import say_hello
say_hello()


from iti.math_module import sum_num



