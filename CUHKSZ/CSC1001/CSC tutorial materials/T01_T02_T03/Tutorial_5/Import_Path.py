import sys
# Update the path of the module you expected to export
sys.path.append('C:/Users/win10/Desktop/CSC1001_20/Tutorial_5/path/')

# Import all functions from MyTriangle_1 module
from MyTriangle_1 import isValid

if isValid(1,2,3):
    print('Yes')
else:
    print('No')


### Or you could import the module as a whole
##import MyTriangle_1
##
##if MyTriangle_1.isValid(2,2,3):
##    print('Yes')
##else:
##    print('No')
