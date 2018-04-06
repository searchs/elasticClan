
#!/usr/bin/env python
from elasticsearch import helpers, Elasticsearch

import sys
import csv

# To run data importer: ./data_importer.py index_name index_label

es = Elasticsearch()

index_label = sys.argv[1]
index_type = sys.argv[2]

with open('data/feed.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index=index_label, doc_type=index_type)
