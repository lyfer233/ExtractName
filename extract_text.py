import json
from urllib.parse import unquote

if __name__ == "__main__":
    # extract text from json
    extract_text = ""
    with open("./input/1.json", "r") as f:
        my_json = json.load(f)
        formImage = my_json['formImage']
        Pages = formImage['Pages']
        for page in Pages:
            Texts = page['Texts'];
            for text in Texts:
                R = text['R'][0]
                extract_text += R['T']

    # Saving the file
    with open("end_file.json", "w", encoding='utf-8') as p:
        p.write("{\"text\":\"")
        p.write(unquote(str(extract_text)))
        p.write("\"}")
