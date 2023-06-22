#!/usr/bin/env python

##Load modules
import pandas as pd
import os
import argparse
import time

##Create arguments
parser = argparse.ArgumentParser(description="Script written to add a new results_alleles.tsv allele profile to the Salmonella enterica database (sent_curr_db.csv)")
parser.add_argument(
	'-id', '--input_directory',
	dest='in_dir',
	help="Directory where results_alleles.tsv is kept",
	required=True
		)
parser.add_argument(
	'-sdb','--strain_db',
	dest='str_db',
	help="Strain db to update and path to",
	required=True
		)
parser.add_argument(
	'-dbd','--db_dir',
	dest='db_dir',
	help="Directory with strain db",
	required=True
		)

args = parser.parse_args()

##Variables used in script
date = time.strftime('%Y%m%d')
in_file = args.in_dir+'results_alleles.tsv'

##Load database and allele profile to be added
in_alle = pd.read_table(in_file)
db_alle = pd.read_csv(args.str_db)

##Concat allele profiles for new db
new_db = pd.concat([in_alle,db_alle],ignore_index=True)

##Save new db
new_db.to_csv(db_dir+'curr_db_'+date+'csv')

if __name__ == '__main__':
	


