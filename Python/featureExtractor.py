import pandas as pd
from urllib.parse import urlparse

dataset= pd.read_csv('cleandData1.csv')

def extract_url_features (url):

    parsed_url = urlparse(url)

    fullUrl_feature= url
    scheme=parsed_url.scheme
    netloc=parsed_url.netloc
    path=parsed_url.path
    query=parsed_url.query

    domain_length= len(parsed_url.netloc)
    path_length=len(parsed_url.path)
    path_segments=len(parsed_url.path.split('/'))


    features={
        'scheme':scheme,
        'netloc':netloc,

    }

