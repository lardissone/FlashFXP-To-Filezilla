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
    xml_str += '<Folder expanded="1">Imported from FlashFXP&#x0A;            '

    for node in nodes:
        name = node.attributes['NAME'].value

        group = node.getElementsByTagName('GROUP')[0].firstChild.data[1:-1] \
            if node.getElementsByTagName('GROUP') else ''

        folders = group.split('\\');

        for folder in folders:
            xml_str += '<Folder>'+folder+'&#x0A;            \n'

        server = node.getElementsByTagName('ADDRESS')[0].firstChild.data \
            if node.getElementsByTagName('ADDRESS') else ''
        port = node.getElementsByTagName('PORT')[0].firstChild.data \
            if node.getElementsByTagName('PORT') else 21
        user = node.getElementsByTagName('USERNAME')[0].firstChild.data \
            if node.getElementsByTagName('USERNAME') else ''
        passw = node.getElementsByTagName('PASSWORD')[0].firstChild.data \
            if node.getElementsByTagName('PASSWORD') else ''
        localpath = node.getElementsByTagName('LOCALPATH')[0].firstChild.data \
            if node.getElementsByTagName('LOCALPATH') else ''
        remotepath = node.getElementsByTagName('REMOTEPATH')[0].firstChild.data \
            if node.getElementsByTagName('REMOTEPATH') else ''

        xml_str += '<Server>\n'
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
        xml_str += '<Comments>Imported from FlashFXP</Comments>'
        xml_str += '<LocalDir>' + str(localpath) + '</LocalDir>'
        xml_str += '<RemoteDir>' + str(remotepath) + '</RemoteDir>'
        xml_str += '<SyncBrowsing>0</SyncBrowsing>'+ str(name) +'&#x0A;                '
        xml_str += '</Server>\n'

        for folder in folders:
            xml_str += '</Folder>\n'

    xml_str += '</Folder>'
    xml_str += '</Servers></FileZilla3>'

    xml_output_file = open('FileZilla.xml', 'w')
    xml_output_file.write(xml_str)
    xml_output_file.close()

if __name__ == "__main__":
    main()
