# What these file?
To extract the gene name using API in PubTator, **PubTatorRead.py** is reading gene name from "Export Annotations".

# How to use it?

## Export Annotations
Input your need format, type, identifiers, then gene name output in the "gene_name.csv"

## Process Raw Text
Suppose we have only pdf format.Then we transform pdf into json in Firstly.
### PDF to JSON
1. Download and install https://github.com/modesty/pdf2json tools.
2. run it in command line
```
pdf2json -f [input directory or pdf file] -o [output directory]
```
3. Using extract_text.py to extract text into json.

### Submit JSON to PubTator
