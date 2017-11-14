# Elasticsearch Commands to check status, metrics and more
# This assumes that the Pythin libray httpie is installed.  If not run 'pip install httpie' 
http :9200/_cluster/settings

http :9200/markets/product/_search?q=Watch
http :9200/_nodes
http :9200/_mappings
http :9200/markets/_stats


#ElasticSearch StartUp

#1.  Install ElasticSearch (brew install elasticsearch)
#2.  Install plugins -kopf or head, javascript and python (optional) (search Github for these plugins)
#3.  Check ElasticSearch is running  at localhost:9200.  On commandline, create an index by running the command:
#--the name of the index, crux, can be anything you want
curl -XPUT http://localhost:9200/crux -d '{
    "settings" : {
        "index" : {
            "number_of_shards" : 2,
            "number_of_replicas" : 1
        }
    }
}'

#4.  Verify the index is created. Check http://localhost:9200
#5.  Run the create index command again.  An error should be returned:
 # E.g.: {"error":"IndexAlreadyExistsException[[crux] already exists]","status":400}

#6.  Create an index with mappings:

curl -XPOST localhost:9200/yaba -d '{ "settings" : { "number_of_shards" : 2,
        "number_of_replicas" : 1    },    "mappings" : { "order" : { "properties" : {
              "id" : {"type" : "string", "store" : "yes" , "index":"not_analyzed"},
              "date" : {"type" : "date", "store" : "no" , "index":"not_analyzed"},
              "customer_id" : {"type" : "string", "store" : "yes" , "index":"not_analyzed"},
              "sent" : {"type" : "boolean", "index":"not_analyzed"},
              "name" : {"type" : "string", "index":"analyzed"},
              "quantity" : {"type" : "integer", "index":"not_analyzed"},
              "vat" : {"type" : "double", "index":"no"}
          }                                            
      }    
  }    
}'
#7.  Delete an index: *** CAUTION: cannot be reversed if index backup does not exists ***
  curl -XDELETE http://localhost:9200/{existing_index_name}
  #-should get an acknowledged true response.   Http 404 is returned for non-existing index
#8.  Closing an index:
  curl -XPOST http://localhost:9200/{existing_index_name}/_close
   # -should get an acknowledged true response
#9.  Open a closed index:
  curl -XPOST http://localhost:9200/{existing_index_name}/_open
    - should get an acknowledged true response
#10.  Rivers  - are ElasticSearch services that pulls/get data into ElasticSearch.  Compartible data sources include
 # CouchDB, MongoDB, RabbitMQ, SQL DBMS (Oracle, MySQL, PostgreSQL etc), Redis, Twitter, Wikipedia
#11.  To create a river, run a command like this :
   curl -XPUT 'http://localhost:9200/_river/benue/_meta' -d  '{"type": "dummy"}'
  #  --should get an OK:true response
#12.  
