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

#scriptName = os.path.splitext(os.path.basename(__file__))[0]
#scriptID   = ' '.join([scriptName,damask.version])

#parser = OptionParser(option_class=damask.extendableOption, usage='%prog options [file[s]]', description = """
#Histogram Plots.
#
#""", version = scriptID)

parser = argparse.ArgumentParser(description='Creating histograms')
parser.add_argument('file',nargs='+',help='filename where the data lies')
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
    print(np.shape(resolved_stress_slip))
    stacknum = index_end - index_start + 1

jet = PyPlot.get_cmap('jet')
colors = iter(jet(np.linspace(0,1,stacknum)))

fig1,stacks=PyPlot.subplots(stacknum,1,sharex='all',sharey='all')
fig1.set_figheight(10)

for p in range(stacknum):
    stacks[p].hist(resolved_stress_slip[:,p],edgecolor='black',label=str(p+1),color=next(colors))
    stacks[p].legend()

axes = PyPlot.gca()
axes.set_ylim([0,len(resolved_stress_slip)])

PyPlot.yticks(np.arange(0,len(resolved_stress_slip),50))

#stacks[1].hist(resolved_stress_slip[:,1],edgecolor='black')
#    PyPlot.hist(resolved_stress_slip[:,0],edgecolor='black')
#    PyPlot.title("Resolved Shear Stress distribution")
#    PyPlot.xlabel(r'$\tau$')
fig1.tight_layout()
fig1.savefig('example.png')

