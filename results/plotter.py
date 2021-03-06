'''
    plotter.py

    visualises one of the .csv files in the results folder that
    have been generated by the main.py code.
'''
import numpy as np
import matplotlib.pyplot as plt
import os

# Get available files for plotting
path_to_results = os.path.dirname(os.path.abspath(__file__))
filelist = os.listdir(path_to_results)
filelist.remove('plotter.py')

# Prompt for specific file
print('Which of the following files do you want to plot? \n', filelist, '\n')
file_to_plot = input('Filename = ')

# Plot
if file_to_plot not in filelist:
    raise ValueError('File not available. Provide full filename.csv')
elif file_to_plot == 'hiddenstate.csv': 
    hiddenstate = np.genfromtxt('results/'+file_to_plot, delimiter = ',')
    plt.plot(hiddenstate)
    plt.yticks([0,1])
    plt.ylabel('On or off')
    plt.xlabel('dt')
    plt.title('Hidden state')
else:
    input_ = np.genfromtxt('results/'+file_to_plot, delimiter = ',')
    plt.hist(input_, bins=100, edgecolor='black')
    plt.xlabel('pA')
    plt.ylabel('Frequency')
    plt.title(file_to_plot.strip('.csv'))

plt.show()