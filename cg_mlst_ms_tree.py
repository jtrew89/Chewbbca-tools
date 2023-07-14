#!/usr/bin/env python
"""
mstree clusters will be based off of shared core genomic alleles. So, isolates
will only be comapred on shared cgmlst profiles. If loci are missing, they will be
omitted. Input will be a list of isolates to be an ms tree from. The script will
extract the allele profiles for those isolates.
"""

##Import modules
import pandas as pd
import argparse
import time
from tqdm import tqdm
import subprocess

##Set arguments
parser = argparse.ArgumentParser(description='Script written to take a list of isolates and run reportree MSTREE2 with metadata file for isolates')
parser.add_argument(
	'-pdb', '--profile_db', dest='pro_db',
	help='Alelle profile db with isolates you wish analysed (Include path)',
	required=True
	)
parser.add_argument(
	'-i', '--input_isolates', dest='in_iso',
	help="List of isolates to be analysed (single column, with 'Isolates' as header)",
	required=True
	)
parser.add_argument(
	'-od', '--output_dir', dest='out_dir',
	help='Directory to output results',
	required=True
	)
parser.add_argument(
	'-mst', '--mst_medium', dest='mst',
	help='Path to mst analytical tool (currently, this only uses ReporTree)',
	required=False
	)

args = parser.parse_args()

##Load files used in analysis
alle_db = pd.read_csv(args.pro_db, low_memory=False)
isolates = list(pd.read_table(args.in_iso)['Isolates'])

##Variables used in script
iso_profs = pd.DataFrame()

##Replace acronyms from chewbac output and treat as missing data '0'
alle_db.replace(
	[
	'INF-','LNF',
	'PLNF', 'PLOT3',
	'PLOT5', 'LOTSC',
	'NIPHEM', 'NIPH',
	'PAMA', 'ALM', 'ASM'
	],
	[
	'', '0','0','0','0','0',
	'0','0','0','0','0'
	],
	inplace=True, regex=True
		)

##Pull profiles for each isolate from input isolates list
for isolate in tqdm(isolates):
	iso_prof = alle_db[alle_db['FILE'] == isolate]
	iso_profs = iso_profs.append(iso_prof,ignore_index=True)

iso_profs.to_csv(args.out_dir+'iso_profs.csv',index=False)
