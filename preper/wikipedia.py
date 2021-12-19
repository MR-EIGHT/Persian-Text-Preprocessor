import xml.etree.ElementTree as et
from Document import Document
import preper

normalizer = preper.Normalizer()

file = open(r"..\data\fawiki-20211101-abstract.xml", 'r', encoding='utf-8').read()
root = et.fromstring(file)
counter = 0
doc_store = []
for doc in root.findall(r'doc'):
    doc_store.append(Document(doc.find('title').text, doc.find('abstract').text, counter))
    counter += 1

for doc in doc_store:
    if doc.body is not None:
        doc.body = normalizer.normalize(doc.body)

