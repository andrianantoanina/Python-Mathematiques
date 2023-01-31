import matplotlib.pyplot as plt # Import the matplotlib module
from matplotlib import style # Optionally you dont need to use style
style.use('ggplot') # Just for style

x = [10, 20, 30, 40, 50] # Get points to plot on graph

plt.plot(x) # We want to plot x on our graph
plt.show()
