# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:49:21 2019

@author: f.gallardo
Create heatmaps =)
"""

import os,sys
import numpy as np
import matplotlib
import argparse
import matplotlib.pyplot as plt

#Change directory (put the adress of wherever your example.txt is)
#In doing so, copy adress as text then substitute \ for \\
        # TODO: Make this directories and file more general as you can do multiple files        
parser = argparse.ArgumentParser()

parser.add_argument('path',nargs='+',
                     help='path to the file')
parser.add_argument('file',nargs='+',
                     help='file containing the data')

options = parser.parse_args()

os.chdir(options.path[0])

#check the file type of the file (to decide the numpy handling)
if os.path.splitext(options.file[0])[1] == '.txt':
        data = np.loadtxt(options.file[0],skiprows=0) 
elif os.path.splitext(options.file[0])[1] == '.csv':
        data = np.genfromtxt(options.file[0], delimiter=',')
else:
        sys.exit("Wrong file format of the data file")

hardness=[float(i) for i in H] # list of strings ('43.21') to floaters (43.21)
numberInMatrix=list(range(2000))  # 0,1,2,3...1999

#turn data into 2D array: 100 (yaxis) x 20(xaxis) #TODO: How is this grid size known? Is it described anywhere in the file?
#Otherwise we can pass it as an argument at the start
#this will plot the heatmap column by column (if that makes sense)
dddata=np.column_stack((hardness[0:99],hardness[100:199],\
                             hardness[200:299],hardness[300:399],\
                             hardness[400:499],hardness[500:599],\
                             hardness[600:699],hardness[700:799],\
                             hardness[800:899],hardness[900:999],\
                             hardness[1000:1099],hardness[1100:1199],\
                             hardness[1200:1299],hardness[1300:1399],\
                             hardness[1400:1499],hardness[1500:1599],\
                             hardness[1600:1699],hardness[1700:1799],\
                             hardness[1800:1899],hardness[1900:1999])) #replace with reshape if the size of map known

def heatmap(dddata, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array
    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(dddata, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Let the horizontal axes labeling appear on top, if down then just delete lines below
    #ax.tick_params(top=True, bottom=False,
                  # labeltop=True, labelbottom=False)
    
    # Turn spines off and create white grid. NO IDEA WHAT THIS IS for the moment...
    for edge, spine in ax.spines.items():
        spine.set_visible(False)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    
    return im, cbar


fig, ax = plt.subplots()
im, cbar = heatmap(dddata, ax=ax,
                   cmap="Reds", cbarlabel="Hardness(GPa")

#cmap= a lot of options, look at https://matplotlib.org/users/colormaps.html

fig.tight_layout()
ax.set_title("Title")
plt.savefig('HeatMap.eps')

#taken from https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py
