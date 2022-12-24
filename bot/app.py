from elasticsearch import Elasticsearch
import csv

csv_file = open('posts.csv', 'r', encoding='utf-8')
reader = csv.reader(csv_file)

es = Elasticsearch("https://elasticsearch:9200")
