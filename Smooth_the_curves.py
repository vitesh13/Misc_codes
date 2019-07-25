#!/usr/bin/env python3
# -*- coding: UTF-8 no BOM -*-


import os,sys
import numpy as np
from optparse import OptionParser
import argparse
import damask
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as PyPlot
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter as savgol

class Smooth():
    def __init__(self,dataset,window,order,deriv):
        self.window = window
        self.order  = order
        self.deriv  = deriv

    def get_smoothed(self):
        smoothed_data = savgol(dataset, window, order,deriv_order)
        return smoothed_data

class num_first_deriv():
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

    def first_derivative(self):
        df = np.diff(self.Y)/np.diff(self.X)
        return df

class interpolation():
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    
    def interpolate_(self):
        f = interp1d(self.X,self.Y)
        return f
   

