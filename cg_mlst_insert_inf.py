#!/usr/bin/env python

"""
Script written to take the novel_alleles.fasta output file from chewBBACA and
insert each novel allele into their respective schema with a 'inf_' mark. So that
novel alleles are maked int he schema, as chewBBACA currently doesnt mark novel
alleles
"""

##Import modules
from Bio import SeqIO
import os
import argparse

##Open novel_alleles.fasta
##load fasta sequence (AlignIO.parse returns a MSA as an interator, to get
#access to seperate sequences it has to be saved into a list)


##Some code found online that I should be able to change into what I want
fasta_file = args.in_fas  # Input fasta file
id_file =  args.in_id # Input novel allele ID
loci_dir = args.schem_dir # Output fasta file which allele is sent to

id_df = pd.read_csv(id_file)
id_df['fas_id'] = id_df.Locus + '_' + id_df['Novel Allele'].apply(str)
wanted = sorted(set(id_df['fas_id']))

#fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')  #if I want to iterate through fasta sequences at a later date
fasta_dict = SeqIO.index('novel_alleles.fasta', 'fasta') #Create a dictionary out of the fasta so that is can be indexed for a particular sequence

end = False
for alle in wanted:
	fas_out = alle.rsplit('_', 1)[0] #remove unique allele number to use to send to the out fasta file
	with open(loci_dir+fas_out+'.fasta', "a") as f:
		curr_seq = fasta_dict[alle]
		curr_seq.id = fas_out + '_inf_' + curr_seq.id[curr_seq.id.rindex('_')+1:]
		SeqIO.write([curr_seq], f, "fasta")
