import configparser
import os
import sys
import console

version={
    "release":0,
    "major":0,
    "minor":0,
    "patch":0
}

defaults=configparser.ConfigParser()
defaults.sections()
defaults.read('defaults.conf')

def __init__(inputFile):
    if os.path.exists('TMP/'):
        if os.path.exists('TMP/body'+defaults['EXTENSIONS']['StrapDownJS']):
            os.remove('TMP/body'+defaults['EXTENSIONS']['StrapDownJS'])
            body=open('TMP/body'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        else:
            body=open('TMP/body'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        if os.path.exists('TMP/head'+defaults['EXTENSIONS']['StrapDownJS']):
            os.remove('TMP/head'+defaults['EXTENSIONS']['StrapDownJS'])
            head=open('TMP/head'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        else:
            head=open('TMP/head'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        if os.path.exists('TMP/output'+defaults['EXTENSIONS']['StrapDownJS']):
            os.remove('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'])
            output=open('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        else:
            output=open('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'],'w')
    else:
        os.mkdir('TMP')
        body=open('TMP/body'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        head=open('TMP/head'+defaults['EXTENSIONS']['StrapDownJS'],'w')
        output=open('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'],'w')

    file=open(inputFile,'r')
    count = 0
    while True:
        count += 1
        line = file.readline()
        if not line:
            file.close()
            head.write('<title>'+defaults['DOC']['title']+'</title>\n<style>\nbody{\n    background-color:'+defaults['DOC']['background']+';\n    color:'+defaults['DOC']['text']+';\n    width:'+defaults['DOC']['width']+';\n    height:'+defaults['DOC']['height']+';\n}\n</style>\n')
            body.close()
            head.close()
            body=open('TMP/body'+defaults['EXTENSIONS']['StrapDownJS'],'r')
            head=open('TMP/head'+defaults['EXTENSIONS']['StrapDownJS'],'r')
            output.write('<!DOCTYPE html>\n<html>\n<head>\n'+head.read()+'</head>\n<body>\n<xmp style="display:none;">\n'+body.read()+'\n</xmp>\n<script src="http://ndossougbe.github.io/strapdown/dist/strapdown.js"></script>\n</body>\n</html>')
            break

        # <head>
        # <style>
        if line.strip().startswith('DH'):
            defaults['DOC']['height']=line.strip().split(':;:')[1]
        elif line.strip().startswith('DW'):
            defaults['DOC']['width']=line.strip().split(':;:')[1]
        elif line.strip().startswith('BG'):
            defaults['DOC']['background']=line.strip().split(':;:')[1]
        elif line.strip().startswith('TXT'):
            defaults['DOC']['text']=line.strip().split(':;:')[1]
        # </style>
        elif line.strip().startswith('T'):
            defaults['DOC']['title']=line.strip().split(':;:')[1]
            console.info('Title set to: '+line.strip().split(':;:')[1])
        elif line.strip().startswith('ICO'):
            console.warn('Icon/Favicon not implemented')
        # </head>

        # <body>
        elif line.strip().startswith('H1'):
            body.write('\n# '+line.strip().split(':;:')[1]+'\n')
            console.log('Wrote "Hedding 1" element')
        elif line.strip().startswith('H2'):
            body.write('\n## '+line.strip().split(':;:')[1]+'\n')
            console.log('Wrote "Hedding 2" element')
        elif line.strip().startswith('H3'):
            body.write('\n### '+line.strip().split(':;:')[1]+'\n')
            console.log('Wrote "Hedding 3" element')
        elif line.strip().startswith('P'):
            body.write('\n'+line.strip().split(':;:')[1]+'\n')
            console.log('Wrote "Paragraph" element')
        # </body>

        elif line.strip().startswith('C'):
            console.info('Comment at line '+str(count))
            body.write('<!-- '+line.strip().split(':;:')[1]+' -->\n')
        elif line.strip().startswith('~'):
            console.info('line '+str(count)+' is blank')
            body.write('\n')
        else:
            head.close()
            body.close()
            output.close()
            print()
            sys.exit('Line '+str(count)+" contains an invalid element, or it's blank")