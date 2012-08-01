#!/usr/bin/env python
import os
from xml.dom import minidom
import sys


def main():
    flash_file = sys.argv[1]

    xml_file = os.path.abspath(__file__)
    xml_file = os.path.dirname(xml_file)
    xml_file = os.path.join(xml_file, flash_file)

    try:
        xmldoc = minidom.parse(xml_file)
    except Exception, inst:
        print "No, no :("
        print "-Please, be sure that this file exists: %s" % xml_file
        print inst
        return

    nodes = xmldoc.getElementsByTagName('SITE')

    xml_str = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><FileZilla3><Servers>'

    for node in nodes:
        name = node.attributes['NAME'].value
        server = node.getElementsByTagName('ADDRESS')[0].firstChild.data \
            if node.getElementsByTagName('ADDRESS') else ''
        port = node.getElementsByTagName('PORT')[0].firstChild.data \
            if node.getElementsByTagName('PORT') else 21
        user = node.getElementsByTagName('USERNAME')[0].firstChild.data \
            if node.getElementsByTagName('USERNAME') else ''
        passw = node.getElementsByTagName('PASSWORD')[0].firstChild.data \
            if node.getElementsByTagName('PASSWORD') else ''

        xml_str += '<Server>'
        xml_str += '<Host>' + str(server) + '</Host>'
        xml_str += '<Port>' + str(port) + '</Port>'
        xml_str += '<Protocol>0</Protocol>'
        xml_str += '<Type>0</Type>'
        xml_str += '<User>' + str(user) + '</User>'
        xml_str += '<Pass>' + str(passw) + '</Pass>'
        xml_str += '<Logontype>1</Logontype>'
        xml_str += '<TimezoneOffset>0</TimezoneOffset>'
        xml_str += '<PasvMode>MODE_DEFAULT</PasvMode>'
        xml_str += '<MaximumMultipleConnections>0</MaximumMultipleConnections>'
        xml_str += '<EncodingType>Auto</EncodingType>'
        xml_str += '<BypassProxy>0</BypassProxy>'
        xml_str += '<Name>' + str(name) + '</Name>'
        xml_str += '<Comments></Comments>'
        xml_str += '<LocalDir></LocalDir>'
        xml_str += '<RemoteDir></RemoteDir>'
        xml_str += '<SyncBrowsing>0</SyncBrowsing>'
        xml_str += '</Server>'

    xml_str += '</Servers></FileZilla3>'

    xml_output_file = open('filezilla.xml', 'w')
    xml_output_file.write(xml_str)
    xml_output_file.close()

if __name__ == "__main__":
    main()
