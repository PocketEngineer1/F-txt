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
        if os.path.exists('TMP/body'+defaults['EXTENSIONS']['Markdown']):
            os.remove('TMP/body'+defaults['EXTENSIONS']['Markdown'])
            body=open('TMP/body'+defaults['EXTENSIONS']['Markdown'],'w')
        else:
            body=open('TMP/body'+defaults['EXTENSIONS']['Markdown'],'w')
        if os.path.exists('TMP/head'+defaults['EXTENSIONS']['Markdown']):
            os.remove('TMP/head'+defaults['EXTENSIONS']['Markdown'])
            head=open('TMP/head'+defaults['EXTENSIONS']['Markdown'],'w')
        else:
            head=open('TMP/head'+defaults['EXTENSIONS']['Markdown'],'w')
        if os.path.exists('TMP/output'+defaults['EXTENSIONS']['Markdown']):
            os.remove('TMP/output'+defaults['EXTENSIONS']['Markdown'])
            output=open('TMP/output'+defaults['EXTENSIONS']['Markdown'],'w')
        else:
            output=open('TMP/output'+defaults['EXTENSIONS']['Markdown'],'w')
    else:
        os.mkdir('TMP')
        body=open('TMP/body'+defaults['EXTENSIONS']['Markdown'],'w')
        head=open('TMP/head'+defaults['EXTENSIONS']['Markdown'],'w')
        output=open('TMP/output'+defaults['EXTENSIONS']['Markdown'],'w')

    file=open(inputFile,'r')
    count = 0
    while True:
        count += 1
        line = file.readline()
        if not line:
            file.close()
            head.write('# '+defaults['DOC']['title']+'\n')
            body.close()
            head.close()
            body=open('TMP/body'+defaults['EXTENSIONS']['Markdown'],'r')
            head=open('TMP/head'+defaults['EXTENSIONS']['Markdown'],'r')
            output.write(head.read()+'\n'+body.read())
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
            defaults['DOC']['title']=line.strip().split(':;:')[1]
            console.info('Title set to: '+line.strip().split(':;:')[1])
        elif line.strip().startswith('ICO'):
            console.error('Unsupported element at line: '+str(count))
        # </head>
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
        elif line.strip().startswith('C'):
            console.warn('Comment at line '+str(count))
        elif line.strip().startswith('~'):
            console.info('line '+str(count)+' is blank')
            body.write('\n')
        else:
            head.close()
            body.close()
            output.close()
            print()
            sys.exit('Line '+str(count)+" contains an invalid element, or it's blank")