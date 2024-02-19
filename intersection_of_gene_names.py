#!/usr/bin/env python
"""
Sree Poojitha Paruchuri
assignment4
intersection_of_gene_names.py
"""
from argparse import ArgumentParser
from assignment4.io_utils import get_filehandle

# Add command line options
PARSER = ArgumentParser(description="Provide two gene lists (ignore header line), find intersection")
PARSER.add_argument('-i1', '--infile1', help='Gene list 1 to open', required=True)
PARSER.add_argument('-i2', '--infile2', help='Gene list 2 to open', required=True)
ARGS = PARSER.parse_args()

# Open files with error handling and read the files
FILE1 = get_filehandle(ARGS.infile1, "r")
FILE2 = get_filehandle(ARGS.infile2, "r")
OUTPUT = get_filehandle("OUTPUT/intersection_output.txt", "w")

# Write the given genes in the file
CHAR21_GENES = set(line.strip().split("\t")[0] for line in FILE1.readlines()[1:])
HUGO_GENES = set(line.strip().split("\t")[0] for line in FILE2.readlines()[1:])
SEQUENCE = CHAR21_GENES.intersection(HUGO_GENES)
OUTPUT.write("\n".join(sorted(SEQUENCE)))

# Print CHAR21_GENES, HUGO_GENES, and length of SEQUENCE
print(f"Number of sequence gene names in {ARGS.infile1}: {len(CHAR21_GENES)}")
print(f"Number of sequence gene names in {ARGS.infile2}: {len(HUGO_GENES)}")
print("Number of common gene symbols found: ", len(SEQUENCE))
print("Output stored in OUTPUT/intersection_output.txt")
