from odf.opendocument import OpenDocumentText
from odf.text import H, P
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

document=OpenDocumentText()

def __init__(inputFile):
    if os.path.exists('TMP/'):
        if os.path.exists('TMP/output'+defaults['EXTENSIONS']['OpenDocumentText']):
            os.remove('TMP/output'+defaults['EXTENSIONS']['OpenDocumentText'])
    else:
        os.mkdir('TMP')

    file=open(inputFile,'r')
    count = 0
    while True:
        count += 1
        line = file.readline()
        if not line:
            file.close()
            document.save('TMP/output'+defaults['EXTENSIONS']['OpenDocumentText'])
            break

        # <head>
        # <style>
        if line.strip().startswith('DH'):
            console.error('Unsupported element at line: '+str(count))
        elif line.strip().startswith('DW'):
            console.error('Unsupported element at line: '+str(count))
        elif line.strip().startswith('BG'):
            console.error('Unsupported element at line: '+str(count))
        elif line.strip().startswith('TXT'):
            console.error('Unsupported element at line: '+str(count))
        # </style>
        elif line.strip().startswith('T'):
            console.error('Unsupported element at line: '+str(count))
        elif line.strip().startswith('ICO'):
            console.error('Unsupported element at line: '+str(count))
        # </head>

        elif line.strip().startswith('H1'):
            h1=H(outlinelevel=1,text=line.strip().split(':;:')[1])
            document.text.addElement(h1)
            console.log('Wrote "Hedding 1" element')
        elif line.strip().startswith('H2'):
            h2=H(outlinelevel=2,text=line.strip().split(':;:')[1])
            document.text.addElement(h2)
            console.log('Wrote "Hedding 2" element')
        elif line.strip().startswith('H3'):
            h3=H(outlinelevel=3,text=line.strip().split(':;:')[1])
            document.text.addElement(h3)
            console.log('Wrote "Hedding 3" element')
        elif line.strip().startswith('P'):
            p=P(text=line.strip().split(':;:')[1])
            document.text.addElement(p)
            console.log('Wrote "Paragraph" element')
        elif line.strip().startswith('C'):
            console.warn('Comment at line '+str(count))
        elif line.strip().startswith('~'):
            console.info('line '+str(count)+' is blank')
            p=P()
            document.text.addElement(p)
        else:
            print()
            sys.exit('Line '+str(count)+" contains an invalid element, or it's blank")