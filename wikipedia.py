import xml.etree.ElementTree as et
from bz2 import BZ2File

path = r"K:\Lessons 00-1\++ Progrmming Assignments And Projects ++\Information Retrieval Projects\Project1\fawiki-20211101-pages-articles-multistream.xml.bz2"
with BZ2File(path) as xml_file:
    tree = et.parse(xml_file)
    root = tree.getroot()






