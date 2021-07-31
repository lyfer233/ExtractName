# What these file?
To extract the gene name using API in PubTator:
- *PubTator_read.py* is reading gene name from "Export Annotations".
- *PubTator_submit.py* is transforme pdf into json,then submit json to API.
- *PubTator_retrieve.py* is retrieve what has handled json by a session number.
- *pdf_file* was used storage your upload pdf.
# How to use it?

## Export Annotations
1. run it in command line
```
python PubTator_retrieve.py
```
2. Input your need format, type, identifiers in order
3. then gene name output in the *gene_name.csv*

## Submit your pdf
1. Taking your all pdf into *pdf_file*" **(this step is important)**
2. run it in command line
```
python PubTator_submit.py
```
3. All successful submit was storage into *SessionNumber.txt*

## Retrieve your upload file

1. run it in command line
```
python PubTator_retrieve.py
```
2. All gene name was taked into the *gene_name.csv*
