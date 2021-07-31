import json
import os
from urllib.parse import unquote

import requests
from unidecode import unidecode


def pdf2json():
    if not os.path.isdir("json_file"):
        os.mkdir("json_file")
    # running pdf2json command
    os.system("pdf2json -f pdf_file -o json_file")


def extract_text():
    if not os.path.isdir("submit_json"):
        os.mkdir("submit_json")
    path = "json_file"
    json_path = os.listdir(path)
    for json_name in json_path:
        # extract text from json
        extract_text = ""
        with open(os.getcwd() + "/json_file/" + json_name, "r") as f:
            process_json = json.load(f)
            formImage = process_json['formImage']
            Pages = formImage['Pages']
            for page in Pages:
                Texts = page['Texts']
                for text in Texts:
                    R = text['R'][0]
                    extract_text += R['T']

        # Saving the file
        with open(os.getcwd() + "/submit_json/" + "submit_{}".format(json_name), "w", encoding='utf-8') as p:
            p.write("{\"text\":\"")
            p.write(unquote(str(extract_text)))
            p.write("\"}")


def submit_json():
    submit_json_path = os.listdir("submit_json")
    with open("SessionNumber.txt", "a") as outputfile:
        for submit_json_name in submit_json_path:
            # load text
            input_json = ""
            with open(os.getcwd() + "/submit_json/" + submit_json_name, "r", encoding='utf-8') as f:
                for line in f:
                    line = unidecode(line)
                    input_json = input_json + line

                # submit request
                r = requests.post(
                    "https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/submit/Gene",
                    data=input_json.encode('utf-8'))
                if r.status_code != 200:
                    print("[Error]: HTTP code " + str(r.status_code))
                else:
                    SessionNumber = r.text
                    print("Thanks for your submission. The session number is : " + SessionNumber + "\n")
                    outputfile.write(SessionNumber + "\t" + submit_json_name + "\n")


if __name__ == "__main__":
    pdf2json()
    extract_text()
    submit_json()
