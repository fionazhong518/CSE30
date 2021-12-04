# ----- TWO Ways of Calling Library ---- #
import example_library #namespace
example_library.foo() # need to call namespace everytime

# importing local namespace
from example_library import *
print(foo())
# NOTE: if you are calling two libraries that contains the same name of program
##      use the FIRST method to avoid problems!!
'''
It is possible to download and install other libraries. There are libraries that work with the web, complex numbers, databases, and more.

Pygame: The library used to create games.
http://www.pygame.org/docs/
wxPython: Create GUI programs, with windows, menus, and more.
http://www.wxpython.org/
pydot: Generate complex directed and non-directed graphs
http://code.google.com/p/pydot/
NumPy: Sophisticated library for working with matrices.
http://numpy.scipy.org/
A wonderful list of Python libraries and links to installers for them is available here:
http://www.lfd.uci.edu/~gohlke/pythonlibs/
'''
# Example of using Matplotlib -- TO DRAW GRAPH VERY VERY USEFUL!
# Installing collected packages: numpy, pyparsing, python-dateutil, pillow, kiwisolver, cycler, matplotlib
"""
Line chart with four values.
The x-axis defaults to start at zero.
"""
import matplotlib.pyplot as plt
# just ignore the yellow line it will work anyway

# Single line graph
x = [1,2,3,4]
y1 = [1, 3, 8, 4]
# two different series on the same graph
y2 = [2,2,3,3]

# Annotating a graph
plt.annotate('Here',
             xy = (2, 3),
             xycoords = 'data',
             xytext = (-40, 20),
             textcoords = 'offset points',
             arrowprops = dict(arrowstyle="->",
                               connectionstyle="arc,angleA=0,armA=30,rad=10"),
             )
# In human word: annotate "HERE" at point (2,3), text is sized with width of 40, height of 20
#                pointing the offset point, arrow is like ->, and pointing direction is -| (adjusting angles)


plt.plot(x,y1, label = "Series 1")
plt.plot(x,y2, label = "Series 2")


"""
This shows how to set line style and markers.
# First character: Line style
# One of '-', '--',  '-.', ':', 'None', ' ', ”
 
# Second character: color
# http://matplotlib.org/1.4.2/api/colors_api.html
 
# Third character: marker shape
# http://matplotlib.org/1.4.2/api/markers_api.html

"""
plt.plot(x, y1, '-ro')
plt.plot(x, y2, '--g^')

# Add a legend to the graph
##              location = upper center, has a shadow, extra-large font size
legend = plt.legend(loc = 'upper center', shadow = True, fontsize = 'x-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.ylabel('Element Value')
plt.xlabel('Element Number')
 
plt.show()