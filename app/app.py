import meilisearch
import json

json_file = open('/tmp/movies.json')
client = meilisearch.Client('http://meilisearch:7700', 'MASTER_KEY')

movies = json.load(json_file)
client.index('movies').add_documents(movies)

result = client.index('movies').search('batman')
print("\n".join([hit['title'] for hit in result['hits']]))
