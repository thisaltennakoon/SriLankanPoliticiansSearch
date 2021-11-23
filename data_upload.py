from elasticsearch import Elasticsearch, helpers
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
file1 = open('preprocessed.json', 'r', encoding="UTF-8")
data = json.loads(file1.read())
for i in data:
    if i["date_of_birth"] == '':
        i["date_of_birth"] = None
helpers.bulk(es, data, index='politicians')
file1.close()
