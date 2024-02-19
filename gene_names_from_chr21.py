#!/usr/bin/env python
"""
Sree Poojitha Paruchuri
assignment4
gene_names_from_chr21.py
"""

from argparse import ArgumentParser
from assignment4.io_utils import get_filehandle


def main():
    """ BUSINESS LOGIC """
    parser = ArgumentParser(description="Open chr21_genes.txt, "
                                        "and ask the user to enter a gene name")
    parser.add_argument('-i', '--infile',
                        help='Path to file to open', required=True)
    args = parser.parse_args()

    # get gene names from chr21 file
    c21 = get_filehandle(args.infile, "r")
    char21_genes = {}
    for line in c21.readlines()[1:]:
        elements = line.strip().split("\t")
        char21_genes.update({elements[0].lower(): "".join(elements[1:])})

    while True:
        gene_name = input("Enter gene name of interest. Type quit to exit: ")
        if gene_name.lower() in ["quit", "exit"]:
            print("Thanks for querying the data.")
            break

        if gene_name.lower() in char21_genes.keys():
            print(f"{gene_name} found! Here is the description:\n"
                  f"{char21_genes[gene_name.lower()]}\n")
        else:
            print("Not a valid gene name.")


if __name__ == "__main__":
    main()
