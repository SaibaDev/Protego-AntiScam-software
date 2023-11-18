import csv
from urllib.parse import urlparse, parse_qs


input_csv_path = 'Datasets\Dataset4.csv'
output_csv_path = 'cleanedData4.csv'

#listt
schemes = []
netlocs = []
paths = []
params_list = []
queries = []
fragments = []
labels = []


with open(input_csv_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csvfile:
        fieldnames = ['scheme', 'netloc', 'path', 'params', 'query', 'fragment', 'label']
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        
        
        writer.writeheader()

        for row in reader:
            url = row['url']
            label = row['label']
            parsed_url = urlparse(url)

            
            schemes.append(parsed_url.scheme)
            netlocs.append(parsed_url.netloc)
            paths.append(parsed_url.path)
            params_list.append(parse_qs(parsed_url.query))
            queries.append(parsed_url.query)
            fragments.append(parsed_url.fragment)
            labels.append(label)

            
            writer.writerow({
                'scheme': parsed_url.scheme,
                'netloc': parsed_url.netloc,
                'path': parsed_url.path,
                'params': parse_qs(parsed_url.query),
                'query': parsed_url.query,
                'fragment': parsed_url.fragment,
                'label': label
            })


