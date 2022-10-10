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

output=configparser.ConfigParser()
output.sections()
output.read('output.conf')

def __init__(inputFile):
    if os.path.exists('TMP/'):
        if os.path.exists('TMP/body'+defaults['EXTENSIONS']['TKinterApp']):
            os.remove('TMP/body'+defaults['EXTENSIONS']['TKinterApp'])
            body=open('TMP/body'+defaults['EXTENSIONS']['TKinterApp'],'w')
        else:
            body=open('TMP/body'+defaults['EXTENSIONS']['TKinterApp'],'w')
        if os.path.exists('TMP/head'+defaults['EXTENSIONS']['TKinterApp']):
            os.remove('TMP/head'+defaults['EXTENSIONS']['TKinterApp'])
            head=open('TMP/head'+defaults['EXTENSIONS']['TKinterApp'],'w')
        else:
            head=open('TMP/head'+defaults['EXTENSIONS']['TKinterApp'],'w')
        if os.path.exists('TMP/output'+defaults['EXTENSIONS']['TKinterApp']):
            os.remove('TMP/output'+defaults['EXTENSIONS']['TKinterApp'])
            output=open('TMP/output'+defaults['EXTENSIONS']['TKinterApp'],'w')
        else:
            output=open('TMP/output'+defaults['EXTENSIONS']['TKinterApp'],'w')
    else:
        os.mkdir('TMP')
        body=open('TMP/body'+defaults['EXTENSIONS']['TKinterApp'],'w')
        head=open('TMP/head'+defaults['EXTENSIONS']['TKinterApp'],'w')
        output=open('TMP/output'+defaults['EXTENSIONS']['TKinterApp'],'w')

    if defaults['DOC']['width']=='auto':
        defaults['DOC']['width']='420'
    if defaults['DOC']['height']=='auto':
        defaults['DOC']['height']='320'

    file=open(inputFile,'r')
    count = 0
    while True:
        count += 1
        line = file.readline()
        if not line:
            file.close()
            head.write("import tkinter as tk\nfrom tkscrolledframe import ScrolledFrame\nimport sys\n\n# <head>\nroot=tk.Tk()\nroot.title('"+defaults['DOC']['title']+"')\nroot.geometry('"+defaults['DOC']['width']+'x'+defaults['DOC']['height']+"')\nsf=ScrolledFrame(root)\nsf.pack(side='top',expand=1,fill='both')\nsf.bind_arrow_keys(root)\nsf.bind_scroll_wheel(root)\ninner_frame=sf.display_widget(tk.Frame)\nroot.bind('<Escape>',lambda event:sys.exit())\n# </head>\n\n# <body>\n")
            body.close()
            head.close()
            body=open('TMP/body'+defaults['EXTENSIONS']['TKinterApp'],'r')
            head=open('TMP/head'+defaults['EXTENSIONS']['TKinterApp'],'r')
            output.write(head.read()+body.read()+'# </body>\n\ninner_frame.configure(background="'+defaults['DOC']['background']+'")\nroot.mainloop()')
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
            body.write("tk.Label(inner_frame,text='"+line.strip().split(':;:')[1]+"',font=("+'"-size"'+",36),background='"+defaults['DOC']['background']+"',foreground='"+defaults['DOC']['text']+"').pack()\n")
            console.log('Wrote "Hedding 1" element')
        elif line.strip().startswith('H2'):
            body.write("tk.Label(inner_frame,text='"+line.strip().split(':;:')[1]+"',font=("+'"-size"'+",26),background='"+defaults['DOC']['background']+"',foreground='"+defaults['DOC']['text']+"').pack()\n")
            console.log('Wrote "Hedding 2" element')
        elif line.strip().startswith('H3'):
            body.write("tk.Label(inner_frame,text='"+line.strip().split(':;:')[1]+"',font=("+'"-size"'+",16),background='"+defaults['DOC']['background']+"',foreground='"+defaults['DOC']['text']+"').pack()\n")
            console.log('Wrote "Hedding 3" element')
        elif line.strip().startswith('P'):
            body.write('tk.Label(inner_frame,text="'+line.strip().split(':;:')[1]+'",background="'+defaults['DOC']['background']+'",foreground="'+defaults['DOC']['text']+'").pack()\n')
            console.log('Wrote "Paragraph" element')
        # </body>

        elif line.strip().startswith('C'):
            console.info('Comment at line '+str(count))
            body.write('# '+line.strip().split(':;:')[1]+'\n')
        elif line.strip().startswith('~'):
            console.info('line '+str(count)+' is blank')
            body.write("tk.Label(inner_frame,text='',background='#c0ffee',foreground='#000000').pack()\n")
        else:
            head.close()
            body.close()
            output.close()
            print()
            sys.exit('Line '+str(count)+" contains an invalid element, or it's blank")