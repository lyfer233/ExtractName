import json
import re

import requests
from xml.dom.minidom import parseString


def extract_xml(str_xml):
    # take str into domtree
    dom_tree = parseString(str_xml)
    collection = dom_tree.documentElement
    # find node
    annotation = collection.getElementsByTagName("annotation")
    with open("gene_name.csv", "a") as xml_opt:
        for tmp in annotation:
            name_node = tmp.getElementsByTagName("text")[0]
            xml_opt.write(name_node.childNodes[0].data + "\n")


def extract_json(str_json):
    with open("gene_name.csv", "a") as json_opt:
        # take json into python obj
        data = json.loads(str_json)
        passages = data['passages']
        for obj in passages:
            tmp = obj['annotations']
            for information in tmp:
                now_infons = information['infons']
                if now_infons['type'] == 'Gene':
                    json_opt.write(information['text'] + "\n")


def extract_pubtator(str_pubtator):
    pattern = re.compile(r'([\-|\w]+.)Gene')
    result = pattern.findall(str_pubtator)
    with open("gene_name.csv", "a") as tator_opt:
        for my_str in result:
            tator_opt.write(str(my_str).rstrip() + "\n")


def process_file(file_format, file_type, process_list):
    for process_id in process_list:
        url = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/{}?{}={}&concepts=gene". \
            format(file_format, file_type, process_id)
        file = requests.get(url).text
        if file_format == "pubtator":
            extract_pubtator(file)
        elif file_format == "biocxml":
            extract_xml(file)
        elif file_format == "biocjson":
            extract_json(file)

    print("extract all gene in documents!!!")


def process_string():
    my_str = input("Please enter the article numbers you want to retrieve, separated by commas: ")
    return my_str.split(",")


if __name__ == "__main__":
    # Input the format
    file_format = input("Input your need file format! 'tator' or 'xml' or 'json': ")
    if file_format != 'tator' and file_format != 'xml' and file_format != 'json':
        raise ValueError("Input error, please your input!")
    format_convert = {
        "tator": "pubtator",
        "xml": "biocxml",
        "json": "biocjson",
    }

    # Input the type
    tator_type = input("Input the type! 'pmids' or 'pmcids': ")
    if tator_type != 'pmids' and tator_type != 'pmcids':
        raise ValueError("Input error, please your input!")

    # Input the string to storage list
    my_list = process_string()
    assert type(my_list) == type([])
    print(my_list)

    if file_format == 'tator' and tator_type == 'pmcids':
        raise ValueError("pmcids can only be used to retrieve publications in biocxml or biocjson formats!!!")
    # Start processing the file
    process_file(format_convert[file_format], tator_type, my_list)
