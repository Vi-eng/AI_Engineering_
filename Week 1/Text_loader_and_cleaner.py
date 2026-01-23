import re
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
import os
from docx import Document

def read_or_load(path_or_url, save_as):
    if not os.path.exists(path_or_url):
        try:
            response = requests.get(path_or_url)
            with open(save_as, "w", encoding="utf-8") as f:
                f.write(response.text)
                path_or_url = save_as
        except Exception as e:
            print(f"Something went wrong! \n Details: {e}")

    if path_or_url.endswith(".docx"):
        doc = Document(path_or_url)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
    
    else:
        with open(path_or_url, "r") as f:
                corpus = f.read()
                return corpus

STOPWORDS = set(stopwords.words("english"))

def clean_corpus(url, save_as, csv_path):
    text = read_or_load(url, save_as)
    
    #lowercase
    text = text.lower()

    #remove punctuation
    text = re.sub(r"[^\s\w]", "", text)

    #tokenize
    tokens = word_tokenize(text)

    #Remove stopwords
    tokens = [token for token in tokens if token not in STOPWORDS]

    #save
    with open (csv_path, 'w', newline = '', encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['tokens']) # A heading
        for token in tokens:
            writer.writerow([token])
        
    return tokens

if __name__ == "__main__":
    url = input("Enter text file path or URL: ")
    save_as = input("Save downloaded text as (e.g. file.txt): ")
    csv_path = input("Save cleaned CSV as (e.g. cleaned_text.csv): ")

    clean_corpus(
        url=url,
        save_as=save_as,
        csv_path=csv_path
    )
