"""
Script written to add a new results_alleles.tsv allele profile to the Salmonella enterica database
(sent_curr_db.csv)
"""

##Load modules
import pandas as pd
import os
import argparse
import time

##Variables used in script
date = time.strftime("%Y%m%d)
db_dir = '~/cg_mlst/working_cgmlst_db/'

##Load database and allele profile to be added
os.chdir(args.in_alpro)
if args.in_alpro ends.with('csv'):
	in_alle = pd.read_csv(args.in_alpro)
else:
	in_alle = pd.read_table(args.in_alpro)

db_alle = pd.read_csv(db_dir+'curr_db.csv')

##Concat allele profiles for new db
new_db = pd.concat([in_alle,db_alle],ignore_index=True)

##Save new db
new_db.to_csv(db_dir+'curr_db_'+date+'csv')



