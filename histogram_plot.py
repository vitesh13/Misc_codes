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

parser = argparse.ArgumentParser(description='Creating histograms')
parser.add_argument('file',nargs='+',help='filename where the data lies')
parser.add_argument('-n',nargs='+',type=bool,help='create a normalised histogram',default=False)
args = parser.parse_args()

#args.file would contain the list of file names

for i in args.file:
    with open(i,'r') as f:
        data = f.readlines()

    header = int(data[0].split()[0])
    index_start  = data[header].split().index('1_resolvedstress_slip')
    index_end    = data[header].split().index('6_resolvedstress_slip')
    #index_per_slip = data[header].split().index('basal_tau')
    resolved_stress_slip = np.loadtxt(i,skiprows=header+1,usecols=np.arange(index_start,index_end+1))
    resolved_stress_slip = resolved_stress_slip/(1E6)
    print(np.shape(resolved_stress_slip))
    stacknum = index_end - index_start + 1

color_map = PyPlot.get_cmap('gist_ncar')
colors = iter(color_map(np.linspace(0,1,np.shape(resolved_stress_slip)[1])))

fig1,stacks=PyPlot.subplots(stacknum,1,sharex='all',sharey='all')
fig1.set_figheight(10)

for p in range(stacknum):
    dataname = data[header].split()[index_start + p]
    stacks[p].hist(resolved_stress_slip[:,p],edgecolor='black',label=dataname,color=next(colors))
    stacks[p].legend()

axes = PyPlot.gca()
axes.set_ylim([0,len(resolved_stress_slip)])

#PyPlot.yticks(np.arange(0,len(resolved_stress_slip),50))
axes.yaxis.set_major_locator(ticker.MultipleLocator(50))   #TODO: make ticks inside
axes.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
axes.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))

fig1.suptitle("Resolved Shear Stress distribution",verticalalignment="top",fontsize=22)
PyPlot.xlabel(r'$\tau (MPa)$',fontsize=18)
fig1.tight_layout()
fig1.savefig('example.png')

