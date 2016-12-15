# -*- coding: utf-8 -*-
# Python 3 only
import os
from xml.dom.minidom import parse
import webbrowser

def links_from_catalog(out_file, catalog_file_name="ext/file_catalog.xml"):
    doc = parse(catalog_file_name)
    docElem = doc.documentElement
    for x in docElem.childNodes[1:-1]:
        name = x.childNodes[1].firstChild.data
        link = x.childNodes[2].attributes['link']
        link = link.value.replace('\\','/')
        print ('    <a href="%s">%s</a><br/>' % (link, name), file=out_file)


HEADER = """<html>
  <head>
    <meta charset="UTF-8">
    <title>"תיק עמותה"</title>
  </head>
  <body dir="rtl">
    <h3>מסמכים בתיק עמותה</h3>
"""


FOOTER= """  </body>
</html>
"""


def index_from_catalog(index_name):
    with open(index_name, "w") as out_file:
        print(HEADER, file=out_file)
        links_from_catalog(out_file)
        print(FOOTER, file=out_file)


if __name__=='__main__':
    print ("Current directory contents:")
    for e in os.listdir():
        print ("\t",e)
    answer = "x"
    while answer not in ("yn"):
        answer = input("Are you sure you're at the root of the Tik Amuta (y/n)? ")
    if answer=='y':
        name = input("file name to generate: ")
        index_from_catalog(name)
        webbrowser.open("./"+name)
