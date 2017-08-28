# Elasticsearch Commands to check status, metrics and more
# This assumes that the Pythin libray httpie is installed.  If not run 'pip install httpie' 
http :9200/_cluster/settings

http :9200/markets/product/_search?q=Watch
http :9200/_nodes
http :9200/_mappings
http :9200/markets/_stats
