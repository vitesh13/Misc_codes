# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:49:21 2019

@author: f.gallardo
Create heatmaps =)
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Change directory (put the adress of wherever your example.txt is)
#In doing so, copy adress as text then substitute \ for \\
os.chdir("L:\\f.gallardo\\RobinJentner\\PythonHeatMaps\\Nanoindentation\\85577_100x20_Matrix\\txt Files")

#open and read file
F= open("85577_All_Parameters.csv", "r") 

#declaring variables with values that will be eliminated *not important*
A=[0]; B=[0]; C=[0]; Depth_max=[0]; Lasting_Depth=[0]; coefs_mean_dev=[0]; 
max_radius=[0]; pos_max_radius=[0]; E_Modulus=[0]; H=[0]

#read each line of .txt
for line in F:  
  #Let's split the line into an array called "data" using the " " as a separator (using a blanck space as a separator):
  data = line.split(",")
  #and let's extract the data:
  A.append(data[0]);
  B.append(data[1]);
  C.append(data[2]);
  Depth_max.append(data[3]);
  Lasting_Depth.append(data[4]);
  coefs_mean_dev.append(data[5]);
  max_radius.append(data[6]);
  pos_max_radius.append(data[7]);
  E_Modulus.append(data[8]);
  H.append(data[9]);

#eliminating data that we introduced at lines 22-23 and then the header of .txt, so we keep 
#only the numerical values we need. *Again, not important*
#whatever.pop(0) deletes the value at index 0(first one then) of whatever array
A.pop(0);              A.pop(0);                  
B.pop(0);              B.pop(0);
C.pop(0);              C.pop(0);
Depth_max.pop(0);      Depth_max.pop(0);
Lasting_Depth.pop(0);  Lasting_Depth.pop(0);
coefs_mean_dev.pop(0); coefs_mean_dev.pop(0);
max_radius.pop(0);     max_radius.pop(0);
pos_max_radius.pop(0); pos_max_radius.pop(0);
E_Modulus.pop(0);      E_Modulus.pop(0);
H.pop(0);              H.pop(0);

#It is good practice to close the file at the end to free up resources   
F.close()

hardness=[float(i) for i in H] # list of strings ('43.21') to floaters (43.21)
numberInMatrix=list(range(2000))  # 0,1,2,3...1999

#turn data into 2D array: 100 (yaxis) x 20(xaxis)
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
                             hardness[1800:1899],hardness[1900:1999]))

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
