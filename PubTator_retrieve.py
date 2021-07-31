import re
import PubTator_read
import requests


def SubmitText():
    #
    # load SessionNumbers
    #
    with open("SessionNumber.txt", 'r', encoding="utf-8") as file_input:
        for line in file_input:
            pattern = re.compile("^([^\t]+)	(.+)$")
            if pattern.search(line):  # title
                m = pattern.match(line)
                retrieve_number = m.group(1)
                filename = m.group(2)

                r = requests.get(
                    "https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/retrieve/" + retrieve_number)
                code = r.status_code
                if code == 200:
                    response = r.text
                    response_format = ""
                    pattern_json = re.compile('"sourcedb"')
                    pattern_bioc = re.compile('.*<collection>.*')
                    pattern_pubtator = re.compile('^([^\|]+)\|[^\|]+\|(.*)')
                    print(response)
                    if pattern_pubtator.search(line):
                        PubTator_read.extract_pubtator(response)
                        break
                    elif pattern_bioc.search(line):
                        PubTator_read.extract_xml(response)
                        break
                    elif pattern_json.search(line):
                        PubTator_read.extract_json(response)
                        break

                    print(retrieve_number + " : Result is retrieved.");
                else:
                    print(retrieve_number + " : Result is not ready. please wait.");


if __name__ == "__main__":
    SubmitText()
