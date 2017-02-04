#  Create index with autocomplete from the start
curl -XPUT 'localhost:9200/markets?pretty' -d'
{
    "settings": {
        "number_of_shards" : 1,
        "number_of_replicas": 0,
        "analysis": {
            "filter": {
                "autocomplete_filter": {
                    "type":     "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 15
                }
            },
            "analyzer": {
                "autocomplete": {
                    "type":      "custom",
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase",
                        "autocomplete_filter" 
                    ]
                }
            }
        }
    }
}'
