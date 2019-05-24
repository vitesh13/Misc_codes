#!/usr/bin/env python3
# -*- coding: UTF-8 no BOM -*-


import os,sys
import numpy as np
from optparse import OptionParser
import damask
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as PyPlot
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties
fig1=PyPlot.figure()
scriptName = os.path.splitext(os.path.basename(__file__))[0]
scriptID   = ' '.join([scriptName,damask.version])

def Graph(A,B,x_label,y_label,x_unit,y_unit,color):
  X= np.array(len(A))
  X=A
  Y= np.array(len(B))
  Y=B
  color=color
  if(x_unit == "none"):
   X_label = "$" + x_label +"$"
  else :
   X_label = "$" + x_label +"$" + " " + "(" + "$" + x_unit + "$" + ")"
  if(y_unit == "none"):
   Y_label = "$" + y_label + "$"
  else :
   Y_label = "$" + y_label + "$" + " " +  "(" + "$" + y_unit + "$" + ")"
  
  if(y_unit=="MPa"):
   PyPlot.grid(axis='y',color='k',linestyle='-',linewidth=0.2)
   PyPlot.xlabel(X_label,fontsize = 20)
   PyPlot.ylabel(Y_label,fontsize = 20)
   PyPlot.plot(X,Y,color = color)
   PyPlot.yticks(np.arange(min(Y),max(Y)+1,4),fontsize=4) 
 
 
  else :
   PyPlot.xlabel(X_label,fontsize = 20)
   PyPlot.ylabel(Y_label,fontsize = 20)
   PyPlot.plot(X,Y,color = color)
   
  
  

  


parser = OptionParser(option_class=damask.extendableOption, usage='%prog options [file[s]]', description = """
Plots.

""", version = scriptID)

parser.add_option('-l','--label',
                  dest = 'labels', metavar = '<string LIST>',
                  action = 'extend',
                  help = '(list of) columns to be plotted with [x], [y] in that order')

parser.add_option('-a','--axis',
                  dest = 'axis', metavar = '<string LIST>',
                  action = 'extend',
                  help = '(list of) axis label of the columns to be plotted')


parser.add_option('-u','--units',
                  dest = 'units', metavar = '<string LIST>',
                  action = 'extend',
                  help = '(list of) units of the columns to be plotted')

parser.add_option('--legends',
                  dest = 'legends', metavar = '<string LIST>',
                  action = 'extend',
                  help = '(list of) legends of the columns to be plotted')

parser.add_option('-t','--title',
                  dest = 'title', metavar = '<string>',
                  action = 'extend',
                  help = 'Title of the plot')
parser.add_option('-c','--colors',
                  dest = 'colors', metavar = '<string>',
                  action = 'extend',
                  help = 'Color of the plot')
(options,filenames) = parser.parse_args()
print(filenames)

if options.labels is None:
 parser.error('no columns/lables specified.')
if(len(options.labels)!=2 ):
  parser.error('number of columns cannot be more than 2')

if filenames== []:    filenames = [None]

for name in filenames:
     try:   table = damask.ASCIItable(name = name, buffered =False,readonly=True)
   
     except: continue
     damask.util.report(scriptName,name)
 
     table.head_read()

     table.data_readArray(options.labels[0])
     A=table.data
     
     X=np.array(len(A))
     X=A
     table.data_readArray(options.labels[1])
     A=table.data
     Y=np.array(len(A))
     Y=A
     table.close()
     Graph(X,Y,options.axis[0],options.axis[1],options.units[0],options.units[1],options.colors[0])
fig1.tight_layout()
if options.legends is None:
 PyPlot.legend()
else:
 PyPlot.legend(options.legends,fontsize= 8 ,loc=3)
if options.title is None:
 PyPlot.title(" ")
else :
 PyPlot.title( options.title ,fontsize = 12)
fig1.savefig(options.labels[1] + '_' + options.labels[0]+'.png')
