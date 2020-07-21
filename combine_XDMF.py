#!/usr/bin/env python3
# -*- coding: UTF-8 no BOM -*-

import os
import re
import numpy as np

prefix_name = 'After_CA_1_stand_'

with open('After_CA_1_stand_timeseries1.xdmf','w') as f:
  
  # initial start of the file
  f.write('<?xml version="1.0"?>\n')
  f.write('<!DOCTYPE Xdmf SYSTEM "Xdmf.dtd"[]>\n')
  f.write('<Xdmf xmlns:xi="http://www.w3.org/2003/XInclude" Version="2.2">\n')
  f.write(' <Domain>\n')
  f.write('  <Grid Name="CellTime" GridType="Collection" CollectionType="Temporal">\n')

  # the parts from other files
  for i in np.arange(10,110,10):   #need to change the range as per the available time steps
    f.write('  <!-- *************** {} START OF ImageDataContainer *************** -->\n'.format(i))
    with open(prefix_name + '{}.xdmf'.format(i),'r') as g:
      data = g.readlines()
    start_idx = [i for i, item in enumerate(data) if re.search('<Grid', item)]
    end_idx   = [i for i, item in enumerate(data) if re.search('</Grid', item)]
    
    for line in range(start_idx[0],end_idx[0] + 1):
      f.write('  ' + data[line])# + '\n')

    f.write('  <!-- ***************{} END OF ImageDataContainer *************** -->\n'.format(i))
  f.write('  </Grid>\n')
  f.write(' </Domain>\n')
  f.write('</Xdmf>\n')

    
    

