# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:11:01 2016
@author: ellisrj2
"""

import pandas
import csv
import os
import numpy

genes = []
probes = []

flags2 = []
flags3 = []
flags4 = []
flags5 = []
#flags6 = []
#flags7 = []

gene_list = [gene.rstrip('\n') for gene in open('pfc_ctd_cocaine.txt')]
gene_list = [gene.upper() for gene in gene_list]

df = pandas.read_csv('Probes.csv', skipinitialspace=True, engine='python')

for gene in gene_list:
    indices = [i for i, x in enumerate(df['gene_symbol']) if x==gene]
    for idx in indices:
        probes.append(df['probe_id'][idx])
        genes.append(gene)
      
df_microarray = pandas.read_csv('PACall.csv', skipinitialspace=True, engine='python')
column_names = list(df_microarray.columns.values)

pfc_columns = [column_name for column_name in column_names if 'inferior frontal' in column_name]

flags = numpy.zeros((len(probes),len(pfc_columns)))

for i in range(len(probes)):
    indices = [p for p, x in enumerate(df_microarray['probe_id']) if x==probes[i]]
    for idx in indices:
        for j in range(len(pfc_columns)):
            flags[i][j] = int(df_microarray[pfc_columns[j]][idx])

#rows = zip(genes, probes, flags, flags2)

path = os.getcwd()
idx_of_last_letters = max(path.rfind(i) for i in "abcdefghijklmnopqrstuvwxyz")

numpy.savetxt('pfc_ctd_expression' + '_' + path[idx_of_last_letters+1:] + '.csv', flags, delimiter=",")

#with open('striatum_ctd_expression' + '_' + path[idx_of_last_letters+1:] + '.csv', 'wb') as thefile:
#    writer = csv.writer(thefile)
#    writer.writerow(['Gene', 'Probe', 'left', 'right'])
#    for row in rows:
#        writer.writerow(row)
