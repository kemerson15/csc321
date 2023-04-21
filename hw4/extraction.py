import tldextract
import csv

with open("domains(1).tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        extracted_info = tldextract.extract(tsv_file)
        print (extracted_info)