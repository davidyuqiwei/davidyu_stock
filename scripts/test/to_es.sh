#curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/test1/test2/123" -d "{ \"field\" : \"value\" }"
#curl -H "Content-Type: application/json" -XGET "http://localhost:9200/test1/test2/123?pretty"
curl -H "Content-Type: application/json" -XGET "http://localhost:9200/test1/test2/_search?pretty"

