#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from xml.dom import minidom
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import base64


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
    xml_str += '<Folder expanded="1">Imported from FlashFXP'

    for node in nodes:
        name = node.attributes['NAME'].value

        group = node.getElementsByTagName('GROUP')[0].firstChild.data[1:-1] \
            if node.getElementsByTagName('GROUP') else ''

        folders = group.split('\\');

        for folder in folders:
            xml_str += '<Folder>'+folder+'\n'

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


        protocol = 0
        if port != '21':
            protocol = 1

        xml_str += '\t<Server>'
        xml_str += '\n\t\t<Host>' + str(server) + '</Host>'
        xml_str += '\n\t\t<Port>' + str(port) + '</Port>'
        xml_str += '\n\t\t<Protocol>' + str(protocol) + '</Protocol>'
        xml_str += '\n\t\t<Type>0</Type>'
        xml_str += '\n\t\t<User>' + str(user) + '</User>'
        xml_str += '\n\t\t<Pass encoding="base64">' + base64.b64encode(passw) + '</Pass>'
        xml_str += '\n\t\t<Logontype>1</Logontype>'
        xml_str += '\n\t\t<TimezoneOffset>0</TimezoneOffset>'
        xml_str += '\n\t\t<PasvMode>MODE_DEFAULT</PasvMode>'
        xml_str += '\n\t\t<MaximumMultipleConnections>0</MaximumMultipleConnections>'
        xml_str += '\n\t\t<EncodingType>Auto</EncodingType>'
        xml_str += '\n\t\t<BypassProxy>0</BypassProxy>'
        xml_str += '\n\t\t<Name>' + str(name) + '</Name>'
        xml_str += '\n\t\t<Comments>Imported from FlashFXP</Comments>'
        xml_str += '\n\t\t<LocalDir>' + str(localpath) + '</LocalDir>'
        xml_str += '\n\t\t<RemoteDir>' + str(remotepath) + '</RemoteDir>'
        xml_str += '\n\t\t<SyncBrowsing>0</SyncBrowsing>'+ str(name) +''
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
