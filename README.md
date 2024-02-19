SREE POOJITHA PARUCHURI
ASSIGNMENT-4


# gene_names_from_chr21.py
# Overview:
Based on the information from chr21.genes.txt file, the user provides an input gene symbols and produces gene descriptions. 

## Descrption:
1) Created a command which takes the user input and provides gene description if given by the user, which provides the information about the gene if present in the input file.
2) If the given information is incorrect a notification popsup as "Not a valid gene name".  
3) argparse is used to pass the arguments to obtain command-line functions.
4) Imported from argparse import ArgumentParser and from assignment4.io_utils import get_filehandle.
   ```bash
   python gene_names_from_chr21.py -h
   python gene_names_from_chr21.py -i chr21_genes.txt
   ```

# find_common_cats.py
# Overview:
This program counts the number of genes in all lists from the given chr21.genes.txt and print the output having categories in ascending order to the output file.

## Descrption:
1) argparse is used to pass the arguments to obtain command-line functions.
2) Imported from argparse import ArgumentParser and from assignment4.io_utils import get_filehandle.
3) Created a command to accept 2 input files which are 2 text files.This creates an output file named as categories.txt.
   ```bash
   python find_common_cats.py -h
   python find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
   ```

# intersection_of_gene_names.py
# Overview:
This program is created to find the common genes between chr21.genes.txt file and hugo_genes.txt file.

## Description:
1) Imported from argparse import ArgumentParser and from assignment4.io_utils import get_filehandle.
2) argparse is used to pass the arguments to obtain command-line functions.
3) Created a command which accepts two user inputs which are the two text files and gives us an output of only unique genes which are not replicated in the provided text files.
4) An output has been created under the name of intersection output.txt.
   ```bash
   python intersection_of_gene_names.py -h
   python intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
   
   ```


