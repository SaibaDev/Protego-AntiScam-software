#Dinideconstruct yung URL into its different components para mas maayos kapag pinasok sa model

import csv
from urllib.parse import urlparse


input_csv_path = 'Datasets\Dataset1.csv'
output_csv_path = 'cleanedData1.csv'

# Mga different components ng url
schemes = []
netlocs = []
paths = []
params_list = []
queries = []
fragments = []


with open(input_csv_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        url = row['url']
        parsed_url = urlparse(url)
        
        
        schemes.append(parsed_url.scheme)
        netlocs.append(parsed_url.netloc)
        paths.append(parsed_url.path)
        params_list.append(parsed_url.params)
        queries.append(parsed_url.query)
        fragments.append(parsed_url.fragment)

#nilalagay ang mga output sa csv file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['scheme', 'netloc', 'path', 'params', 'query', 'fragment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    
    for components in zip(schemes, netlocs, paths, params_list, queries, fragments):
        writer.writerow(dict(zip(fieldnames, components)))
