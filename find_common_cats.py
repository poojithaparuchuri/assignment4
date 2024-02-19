#!/usr/bin/env python
"""
Sree Poojitha Paruchuri
assignment4
find_common_cats.py
"""
from argparse import ArgumentParser
from assignment4.io_utils import get_filehandle

# add command line options
parser = ArgumentParser(description="Combine on gene name and count the category occurrence")
parser.add_argument('-i1', '--infile1',
                    help='Path to the gene description file to open', required=True)
parser.add_argument('-i2', '--infile2',
                    help='Path to the gene category to open', required=True)
args = parser.parse_args()

# open files with error handling
infile_1 = get_filehandle(args.infile1, "r")
infile_2 = get_filehandle(args.infile2, "r")

# process data
sets = {}
for line in infile_1.readlines()[1:]:
    seq = line.strip().split("\t")
    sets.setdefault(seq[-1], []).append(seq[0])

category_infile_2 = {}
for line in infile_2.readlines():
    data = line.strip().split("\t")
    category_infile_2[data[0]] = data[1]

# write to a file using a with statement
with get_filehandle("OUTPUT/categories.txt", "w") as output_file:
    # sort the dictionary
    categories = dict(sorted(sets.items(), key=lambda x: x[0].lower()))
    category_number = 1.1
    for a, c in categories.items():
        if a in category_infile_2:
            occurrence_count = len(c)
            description = f"{category_number:.1f}\t<Occurrence Here>\tGenes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase)."
            output_file.write(f"{description}\n")
            category_number += 1.0  # Increment by 1.0 for each category
