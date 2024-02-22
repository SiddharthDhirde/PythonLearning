print("This is my_program file, in which we are going to import module and packages!")

# Module
# A Module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py appended. 
# Within a module, you can define functions, classes, and variables, and also include runnable code.

# Here we created a my_module file and imported in my_program file. 
# So here my_module file is called module for my_program file.

import my_module

# Accessing constant from my module file
print("Constant from my_module file: ", my_module.my_module_const)
# Accessing function from my module file
print("Function from my_module file: ", my_module.my_module_func())


print("\n"*3)


# Package
# A package is a way of organizing related modules into a single directory hierarchy. 
# A package can contain one or more modules, as well as subpackages (i.e., nested packages), allowing for a hierarchical structure to organize code.
# A Python package is represented as a directory containing a special file called __init__.py. 
# This file can be empty or can contain Python code that initializes the package. The presence of the __init__.py file is what distinguishes a directory as a Python package.


from MainPackage import main_script

# Accessing constant from main_script file
print("Constant from main_script file which is in Main Package: ", main_script.main_package_const)
# Accessing function from main_script file
print("Function from main_script file which is in Main Package: ", main_script.main_package_function())

print()

# SubPackage
from MainPackage.SubPackage.sub_script import *
# from MainPackage.SubPackage.sub_script import sub_script_const, sub_script_func

# Accessing constant from sub_script file which is in MainPackage/SubPackage
print("Constant from sub_script file which is in MainPackage/SubPackage: ", sub_script_const)

# Accessing function from sub_script file which is in MainPackage/SubPackage
print("Function from sub_script file which is in MainPackage/SubPackage: ", sub_script_func())
