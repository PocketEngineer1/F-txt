from utils import *
import configparser
import console
import sys
import os

defaults=configparser.ConfigParser()
defaults.sections()
defaults.read('defaults.conf')

output=configparser.ConfigParser()
output.sections()
output.read('output.conf')

enable=configparser.ConfigParser()
enable.sections()
enable.read('enable.conf')

version={
    "release":0,
    "major":0,
    "minor":0,
    "patch":0
}

def __init__(file='none',group='none',target='none',value='none'):
    if file=='none':
        print('Select file to modify:')
        print('defaults, output, enable')
        usr_in=input()
        
        if usr_in=='defaults':
            print('Please select one of the following groups:')
            print('FORMAT, DOC, EXTENSIONS')
            usr_in=input()
            if usr_in=='FORMAT':
                print('Type the name of one of the following formats:')
                print('HTML, Markdown, StrapDownJS, TKinterApp, MicrosoftWord, OpenDocumentText')
                usr_in=input()
                if usr_in=='HTML':
                    replace_line('defaults.conf',2,'format=HTML\n')
                elif usr_in=='Markdown':
                    replace_line('defaults.conf',2,'format=Markdown\n')
                elif usr_in=='StrapDownJS':
                    replace_line('defaults.conf',2,'format=StrapDownJS\n')
                elif usr_in=='TKinterApp':
                    replace_line('defaults.conf',2,'format=TKinterApp\n')
                elif usr_in=='MicrosoftWord':
                    replace_line('defaults.conf',2,'format=MicrosoftWord\n')
                elif usr_in=='OpenDocumentText':
                    replace_line('defaults.conf',2,'format=OpenDocumentText\n')
                else:
                    console.exit('Invalid')

            elif usr_in=='DOC':
                file=open('defaults.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following items to set a new value.')
                print(lines[4]+lines[5]+lines[6]+lines[7]+lines[8]+lines[9])
                usr_in=input()
                if usr_in=='title':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',4,'title='+usr_in+'\n')
                elif usr_in=='favicon':
                    console.error('403 Forbidden')
                elif usr_in=='background':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',6,'background=#'+usr_in+'\n')
                elif usr_in=='text':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',7,'text='+usr_in+'\n')
                elif usr_in=='width':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',8,'width='+usr_in+'\n')
                elif usr_in=='height':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',9,'height='+usr_in+'\n')
                else:
                    console.exit('Invalid Item')

            elif usr_in=='EXTENSIONS':
                file=open('defaults.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following items to set a new value.')
                print(lines[11]+lines[12]+lines[13]+lines[14]+lines[15]+lines[16])
                usr_in=input()
                if usr_in=='HTML':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',11,'HTML='+usr_in+'\n')
                elif usr_in=='Markdown':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',12,'Markdown='+usr_in+'\n')
                elif usr_in=='StrapDownJS':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',13,'StrapDownJS='+usr_in+'\n')
                elif usr_in=='TKinterApp':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',14,'TKinterApp='+usr_in+'\n')
                elif usr_in=='MicrosoftWord':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',15,'MicrosoftWord='+usr_in+'\n')
                elif usr_in=='OpenDocumentText':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',16,'OpenDocumentText='+usr_in+'\n')
                else:
                    console.exit('Invalid Item')
            else:
                console.exit('Invalid group')
            
        elif usr_in=='enable':
            print('Please select one of the following groups:')
            print('Interfaces, Outputs')
            usr_in=input()
            if usr_in=='Interfaces':
                file=open('enable.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following modules to toggle them on or off.')
                print(lines[3]+lines[4]+lines[5])
                usr_in=input()
                if usr_in=='GUI':
                    if enable['Modules/Interfaces']['GUI']=='Y':
                        replace_line('enable.conf',3,'GUI=N\n')
                    elif enable['Modules/Interfaces']['GUI']=='N':
                        replace_line('enable.conf',3,'GUI=Y\n')
                elif usr_in=='CLI':
                    if enable['Modules/Interfaces']['CLI']=='Y':
                        replace_line('enable.conf',4,'CLI=N\n')
                    elif enable['Modules/Interfaces']['CLI']=='N':
                        replace_line('enable.conf',4,'CLI=Y\n')
                elif usr_in=='WebUI':
                    if enable['Modules/Interfaces']['WebUI']=='Y':
                        replace_line('enable.conf',5,'WebUI=N\n')
                    elif enable['Modules/Interfaces']['WebUI']=='N':
                        replace_line('enable.conf',5,'WebUI=Y\n')
                else:
                    console.exit('Invalid module')

            elif usr_in=='Outputs':
                file=open('enable.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following modules to toggle them on or off.')
                print(lines[7]+lines[8]+lines[9]+lines[10]+lines[11]+lines[12])
                usr_in=input()
                if usr_in=='HTML':
                    if enable['Modules/Outputs']['HTML']=='Y':
                        replace_line('enable.conf',7,'HTML=N\n')
                    elif enable['Modules/Outputs']['HTML']=='N':
                        replace_line('enable.conf',7,'HTML=Y\n')

                elif usr_in=='Markdown':
                    if enable['Modules/Outputs']['Markdown']=='Y':
                        replace_line('enable.conf',8,'Markdown=N\n')
                    elif enable['Modules/Outputs']['Markdown']=='N':
                        replace_line('enable.conf',8,'Markdown=Y\n')

                elif usr_in=='MicrosoftWord':
                    if enable['Modules/Outputs']['MicrosoftWord']=='Y':
                        replace_line('enable.conf',9,'MicrosoftWord=N\n')
                    elif enable['Modules/Outputs']['MicrosoftWord']=='N':
                        replace_line('enable.conf',9,'MicrosoftWord=Y\n')

                elif usr_in=='OpenDocumentText':
                    if enable['Modules/Outputs']['OpenDocumentText']=='Y':
                        replace_line('enable.conf',10,'OpenDocumentText=N\n')
                    elif enable['Modules/Outputs']['OpenDocumentText']=='N':
                        replace_line('enable.conf',10,'OpenDocumentText=Y\n')

                elif usr_in=='StrapDownJS':
                    if enable['Modules/Outputs']['StrapDownJS']=='Y':
                        replace_line('enable.conf',11,'StrapDownJS=N\n')
                    elif enable['Modules/Outputs']['StrapDownJS']=='N':
                        replace_line('enable.conf',11,'StrapDownJS=Y\n')

                elif usr_in=='TKinterApp':
                    if enable['Modules/Outputs']['TKinterApp']=='Y':
                        replace_line('enable.conf',12,'TKinterApp=N\n')
                    elif enable['Modules/Outputs']['TKinterApp']=='N':
                        replace_line('enable.conf',12,'TKinterApp=Y\n')
                else:
                    console.exit('Invalid module')
            else:
                console.exit('Invalid group')

    elif file.lower()=='defaults':
        if group=='none':
            print('Please select one of the following groups:')
            print('FORMAT, DOC, EXTENSIONS')
            usr_in=input()
            if usr_in=='FORMAT':
                print('Type the name of one of the following formats:')
                print('HTML, Markdown, StrapDownJS, TKinterApp, MicrosoftWord, OpenDocumentText')
                usr_in=input()
                if usr_in=='HTML':
                    replace_line('defaults.conf',2,'format=HTML\n')
                elif usr_in=='Markdown':
                    replace_line('defaults.conf',2,'format=Markdown\n')
                elif usr_in=='StrapDownJS':
                    replace_line('defaults.conf',2,'format=StrapDownJS\n')
                elif usr_in=='TKinterApp':
                    replace_line('defaults.conf',2,'format=TKinterApp\n')
                elif usr_in=='MicrosoftWord':
                    replace_line('defaults.conf',2,'format=MicrosoftWord\n')
                elif usr_in=='OpenDocumentText':
                    replace_line('defaults.conf',2,'format=OpenDocumentText\n')
                else:
                    console.exit('Invalid')
            elif usr_in=='DOC':
                file=open('defaults.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following items to set a new value.')
                print(lines[4]+lines[5]+lines[6]+lines[7]+lines[8]+lines[9])
                usr_in=input()
                if usr_in=='title':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',4,'title='+usr_in+'\n')
                elif usr_in=='favicon':
                    console.error('403 Forbidden')
                elif usr_in=='background':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',6,'background='+usr_in+'\n')
                elif usr_in=='text':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',7,'text='+usr_in+'\n')
                elif usr_in=='width':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',8,'width='+usr_in+'\n')
                elif usr_in=='height':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',9,'height='+usr_in+'\n')
                else:
                    console.exit('Invalid Item')

            elif usr_in=='EXTENSIONS':
                file=open('defaults.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following items to set a new value.')
                print(lines[11]+lines[12]+lines[13]+lines[14]+lines[15]+lines[16])
                usr_in=input()
                if usr_in=='HTML':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',11,'HTML='+usr_in+'\n')
                elif usr_in=='Markdown':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',12,'Markdown='+usr_in+'\n')
                elif usr_in=='StrapDownJS':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',13,'StrapDownJS='+usr_in+'\n')
                elif usr_in=='TKinterApp':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',14,'TKinterApp='+usr_in+'\n')
                elif usr_in=='MicrosoftWord':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',15,'MicrosoftWord='+usr_in+'\n')
                elif usr_in=='OpenDocumentText':
                    usr_in=input('Value: ')
                    replace_line('defaults.conf',16,'OpenDocumentText='+usr_in+'\n')
                else:
                    console.exit('Invalid Item')

        elif group=='FORMAT':
            if target=='HTML':
                replace_line('defaults.conf',2,'format=HTML\n')
            elif target=='Markdown':
                replace_line('defaults.conf',2,'format=Markdown\n')
            elif target=='StrapDownJS':
                replace_line('defaults.conf',2,'format=StrapDownJS\n')
            elif target=='TKinterApp':
                replace_line('defaults.conf',2,'format=TKinterApp\n')
            elif target=='MicrosoftWord':
                replace_line('defaults.conf',2,'format=MicrosoftWord\n')
            elif target=='OpenDocumentText':
                replace_line('defaults.conf',2,'format=OpenDocumentText\n')
            else:
                console.exit('Invalid')
        elif group=='DOC':
            if target=='title':
                replace_line('defaults.conf',4,'title='+value+'\n')
            elif target=='favicon':
                console.exit('403 Forbidden')
            elif target=='background':
                replace_line('defaults.conf',6,'background=#'+value+'\n')
            elif target=='text':
                replace_line('defaults.conf',7,'text='+value+'\n')
            elif target=='width':
                replace_line('defaults.conf',8,'width='+value+'\n')
            elif target=='height':
                replace_line('defaults.conf',9,'height='+value+'\n')
            else:
                console.exit('Invalid Item')
        elif group=='EXTENSIONS':
            if target=='HTML':
                replace_line('defaults.conf',11,'HTML='+value+'\n')
            elif target=='Markdown':
                    replace_line('defaults.conf',12,'Markdown='+value+'\n')
            elif target=='StrapDownJS':
                    replace_line('defaults.conf',13,'StrapDownJS='+value+'\n')
            elif target=='TKinterApp':
                    replace_line('defaults.conf',14,'TKinterApp='+value+'\n')
            elif target=='MicrosoftWord':
                    replace_line('defaults.conf',15,'MicrosoftWord='+value+'\n')
            elif target=='OpenDocumentText':
                replace_line('defaults.conf',16,'OpenDocumentText='+value+'\n')
            else:
                console.exit('Invalid Item')

    elif file.lower()=='output':
        if group=='none':
            print('Please select one of the following groups:')
            print('HTML, StrapDownJS, Markdown, TKinterApp, MicrosoftWord, OpenDocumentText')
            usr_in=input()
            if usr_in=='HTML':
                console.error('No HTML specific configuration')
            elif usr_in=='StrapDownJS':
                console.error('No StrapDownJS specific configuration')
            elif usr_in=='Markdown':
                console.error('No Markdown specific configuration')
            elif usr_in=='TKinterApp':
                file=open('output.conf','r')
                lines=file.readlines()
                print()
                print('Type the name of one of the following options to toggle them on or off.')
                print()
                print(lines[7]+lines[8])
                usr_in=input()
                if usr_in=='Resize_X':
                    if output['TKinterApp']['Resize_X']=='Y':
                        replace_line('output.conf',7,'Resize_X=N\n')
                    elif output['TKinterApp']['Resize_X']=='N':
                        replace_line('output.conf',7,'Resize_X=Y\n')
                elif usr_in=='Resize_Y':
                    if output['TKinterApp']['Resize_Y']=='Y':
                        replace_line('output.conf',8,'Resize_Y=N\n')
                    elif output['TKinterApp']['Resize_Y']=='N':
                        replace_line('output.conf',8,'Resize_Y=Y\n')
                else:
                    console.exit('Invalid option')
            elif usr_in=='MicrosoftWord':
                console.error('No MicrosoftWord specific configuration')
            elif usr_in=='OpenDocumentText':
                console.error('No OpenDocumentText specific configuration')
            else:
                console.exit('Invalid group')
        elif group=='HTML':
            console.exit('No HTML specific configuration')
        elif group=='StrapDownJS':
            console.exit('No StrapDownJS specific configuration')
        elif group=='Markdown':
            console.exit('No Markdown specific configuration')
        elif group=='TKinterApp':
            if target=='Resize_X':
                if value=='none':
                    if output['TKinterApp']['Resize_X']=='Y':
                        replace_line('output.conf',7,'Resize_X=N\n')
                    elif output['TKinterApp']['Resize_X']=='N':
                        replace_line('output.conf',7,'Resize_X=Y\n')
                elif value=='Y':
                    replace_line('output.conf',7,'Resize_X=Y\n')
                elif value=='N':
                    replace_line('output.conf',7,'Resize_X=N\n')
                else:
                    console.exit('Invalid value')
            if target=='Resize_X':
                if value=='none':
                    if output['TKinterApp']['Resize_Y']=='Y':
                        replace_line('output.conf',8,'Resize_Y=N\n')
                    elif output['TKinterApp']['Resize_Y']=='N':
                        replace_line('output.conf',8,'Resize_Y=Y\n')
                elif value=='Y':
                    replace_line('output.conf',8,'Resize_Y=Y\n')
                elif value=='N':
                    replace_line('output.conf',8,'Resize_Y=N\n')
                else:
                    console.exit('Invalid value')
        elif usr_in=='MicrosoftWord':
            console.error('No MicrosoftWord specific configuration')
        elif usr_in=='OpenDocumentText':
            console.error('No OpenDocumentText specific configuration')
        else:
            console.exit('Invalid group')

    elif file.lower()=='enable':
        if group=='none':
            print('Please select one of the following groups:')
            print('Interfaces, Outputs')
            usr_in=input()
            if usr_in=='Interfaces':
                file=open('enable.conf','r')
                lines=file.readlines()

                print('Type the name of one of the following modules to toggle them on or off.')
                print(lines[3]+lines[4]+lines[5])
                usr_in=input()
                if usr_in=='GUI':
                    if enable['Modules/Interfaces']['GUI']=='Y':
                        replace_line('enable.conf',3,'GUI=N\n')
                    elif enable['Modules/Interfaces']['GUI']=='N':
                        replace_line('enable.conf',3,'GUI=Y\n')
                elif usr_in=='CLI':
                    if enable['Modules/Interfaces']['CLI']=='Y':
                        replace_line('enable.conf',4,'CLI=N\n')
                    elif enable['Modules/Interfaces']['CLI']=='N':
                        replace_line('enable.conf',4,'CLI=Y\n')
                elif usr_in=='WebUI':
                    if enable['Modules/Interfaces']['WebUI']=='Y':
                        replace_line('enable.conf',5,'WebUI=N\n')
                    elif enable['Modules/Interfaces']['WebUI']=='N':
                        replace_line('enable.conf',5,'WebUI=Y\n')
                else:
                    console.exit('Invalid module')

            elif usr_in=='Outputs':
                file=open('enable.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following modules to toggle them on or off.')
                print(lines[7]+lines[8]+lines[9]+lines[10]+lines[11]+lines[12])
                usr_in=input()
                if usr_in=='HTML':
                    if enable['Modules/Outputs']['HTML']=='Y':
                        replace_line('enable.conf',7,'HTML=N\n')
                    elif enable['Modules/Outputs']['HTML']=='N':
                        replace_line('enable.conf',7,'HTML=Y\n')

                elif usr_in=='Markdown':
                    if enable['Modules/Outputs']['Markdown']=='Y':
                        replace_line('enable.conf',8,'Markdown=N\n')
                    elif enable['Modules/Outputs']['Markdown']=='N':
                        replace_line('enable.conf',8,'Markdown=Y\n')

                elif usr_in=='MicrosoftWord':
                    if enable['Modules/Outputs']['MicrosoftWord']=='Y':
                        replace_line('enable.conf',9,'MicrosoftWord=N\n')
                    elif enable['Modules/Outputs']['MicrosoftWord']=='N':
                        replace_line('enable.conf',9,'MicrosoftWord=Y\n')

                elif usr_in=='OpenDocumentText':
                    if enable['Modules/Outputs']['OpenDocumentText']=='Y':
                        replace_line('enable.conf',10,'OpenDocumentText=N\n')
                    elif enable['Modules/Outputs']['OpenDocumentText']=='N':
                        replace_line('enable.conf',10,'OpenDocumentText=Y\n')

                elif usr_in=='StrapDownJS':
                    if enable['Modules/Outputs']['StrapDownJS']=='Y':
                        replace_line('enable.conf',11,'StrapDownJS=N\n')
                    elif enable['Modules/Outputs']['StrapDownJS']=='N':
                        replace_line('enable.conf',11,'StrapDownJS=Y\n')

                elif usr_in=='TKinterApp':
                    if enable['Modules/Outputs']['TKinterApp']=='Y':
                        replace_line('enable.conf',12,'TKinterApp=N\n')
                    elif enable['Modules/Outputs']['TKinterApp']=='N':
                        replace_line('enable.conf',12,'TKinterApp=Y\n')
                else:
                    console.exit('Invalid module')
            else:
                console.exit('Invalid group')

        elif group=='Interfaces':
                if target=='none':
                    file=open('enable.conf','r')
                    lines=file.readlines()
                    print('Type the name of one of the following modules to toggle them on or off.')
                    print(lines[3]+lines[4])
                    usr_in=input()
                    if usr_in=='GUI':
                        if enable['Modules/Interfaces']['GUI']=='Y':
                            replace_line('enable.conf',3,'GUI=N\n')
                        elif enable['Modules/Interfaces']['GUI']=='N':
                            replace_line('enable.conf',3,'GUI=Y\n')
                    elif usr_in=='CLI':
                        if enable['Modules/Interfaces']['CLI']=='Y':
                            replace_line('enable.conf',4,'CLI=N\n')
                        elif enable['Modules/Interfaces']['CLI']=='N':
                            replace_line('enable.conf',4,'CLI=Y\n')
                    elif usr_in=='WebUI':
                        if enable['Modules/Interfaces']['WebUI']=='Y':
                            replace_line('enable.conf',5,'WebUI=N\n')
                        elif enable['Modules/Interfaces']['WebUI']=='N':
                            replace_line('enable.conf',5,'WebUI=Y\n')
                    else:
                        console.exit('Invalid module')
                elif target=='GUI':
                    if value=='none':
                        if enable['Modules/Interfaces']['GUI']=='Y':
                            replace_line('enable.conf',3,'GUI=N\n')
                        elif enable['Modules/Interfaces']['GUI']=='N':
                            replace_line('enable.conf',3,'GUI=Y\n')
                    elif value=='Y':
                        replace_line('enable.conf',3,'GUI=Y\n')
                    elif value=='N':
                        replace_line('enable.conf',3,'GUI=N\n')
                    else:
                        console.exit('Invalid value')

                elif target=='CLI':
                    if value=='none':
                        if enable['Modules/Interfaces']['CLI']=='Y':
                            replace_line('enable.conf',4,'CLI=N\n')
                        elif enable['Modules/Interfaces']['CLI']=='N':
                            replace_line('enable.conf',4,'CLI=Y\n')
                    elif value=='Y':
                        replace_line('enable.conf',4,'CLI=Y\n')
                    elif value=='N':
                        replace_line('enable.conf',4,'CLI=N\n')
                    else:
                        console.exit('Invalid value')
                elif target=='CLI':
                    if value=='none':
                        if enable['Modules/Interfaces']['WebUI']=='Y':
                            replace_line('enable.conf',5,'WebUI=N\n')
                        elif enable['Modules/Interfaces']['WebUI']=='N':
                            replace_line('enable.conf',5,'WebUI=Y\n')
                    elif value=='Y':
                        replace_line('enable.conf',5,'WebUI=Y\n')
                    elif value=='N':
                        replace_line('enable.conf',5,'WebUI=N\n')
                    else:
                        console.exit('Invalid value')
                else:
                    console.exit('Invalid module')

        elif group=='Outputs':
            if target=='none':
                file=open('enable.conf','r')
                lines=file.readlines()
                print('Type the name of one of the following modules to toggle them on or off.')
                print(lines[7]+lines[8]+lines[9]+lines[10]+lines[11]+lines[12])
                usr_in=input()
                if usr_in=='HTML':
                    if enable['Modules/Outputs']['HTML']=='Y':
                        replace_line('enable.conf',7,'HTML=N\n')
                    elif enable['Modules/Outputs']['HTML']=='N':
                        replace_line('enable.conf',7,'HTML=Y\n')

                elif usr_in=='Markdown':
                    if enable['Modules/Outputs']['Markdown']=='Y':
                        replace_line('enable.conf',8,'Markdown=N\n')
                    elif enable['Modules/Outputs']['Markdown']=='N':
                        replace_line('enable.conf',8,'Markdown=Y\n')

                elif usr_in=='MicrosoftWord':
                    if enable['Modules/Outputs']['MicrosoftWord']=='Y':
                        replace_line('enable.conf',9,'MicrosoftWord=N\n')
                    elif enable['Modules/Outputs']['MicrosoftWord']=='N':
                        replace_line('enable.conf',9,'MicrosoftWord=Y\n')

                elif usr_in=='OpenDocumentText':
                    if enable['Modules/Outputs']['OpenDocumentText']=='Y':
                        replace_line('enable.conf',10,'OpenDocumentText=N\n')
                    elif enable['Modules/Outputs']['OpenDocumentText']=='N':
                        replace_line('enable.conf',10,'OpenDocumentText=Y\n')

                elif usr_in=='StrapDownJS':
                    if enable['Modules/Outputs']['StrapDownJS']=='Y':
                        replace_line('enable.conf',11,'StrapDownJS=N\n')
                    elif enable['Modules/Outputs']['StrapDownJS']=='N':
                        replace_line('enable.conf',11,'StrapDownJS=Y\n')

                elif usr_in=='TKinterApp':
                    if enable['Modules/Outputs']['TKinterApp']=='Y':
                        replace_line('enable.conf',12,'TKinterApp=N\n')
                    elif enable['Modules/Outputs']['TKinterApp']=='N':
                        replace_line('enable.conf',12,'TKinterApp=Y\n')
                else:
                    console.exit('Invalid module')

            elif target=='HTML':
                if value=='none':
                    if enable['Modules/Outputs']['HTML']=='Y':
                        replace_line('enable.conf',7,'HTML=N\n')
                    elif enable['Modules/Outputs']['HTML']=='N':
                        replace_line('enable.conf',7,'HTML=Y\n')
                elif value=='Y':
                    replace_line('enable.conf',7,'HTML=Y\n')
                elif value=='N':
                    replace_line('enable.conf',7,'HTML=N\n')
                else:
                    console.exit('Invalid value')

            elif target=='Markdown':
                if value=='none':
                    if enable['Modules/Outputs']['Markdown']=='Y':
                        replace_line('enable.conf',8,'Markdown=N\n')
                    elif enable['Modules/Outputs']['Markdown']=='N':
                        replace_line('enable.conf',8,'Markdown=Y\n')
                elif value=='Y':
                    replace_line('enable.conf',8,'Markdown=Y\n')
                elif value=='N':
                    replace_line('enable.conf',8,'Markdown=N\n')
                else:
                    console.exit('Invalid value')

            elif target=='MicrosoftWord':
                if value=='none':
                    if enable['Modules/Outputs']['MicrosoftWord']=='Y':
                        replace_line('enable.conf',9,'MicrosoftWord=N\n')
                    elif enable['Modules/Outputs']['MicrosoftWord']=='N':
                        replace_line('enable.conf',9,'MicrosoftWord=Y\n')
                elif value=='Y':
                    replace_line('enable.conf',9,'MicrosoftWord=Y\n')
                elif value=='N':
                    replace_line('enable.conf',9,'MicrosoftWord=N\n')
                else:
                    console.exit('Invalid value')

            elif target=='OpenDocumentText':
                if value=='none':
                    if enable['Modules/Outputs']['OpenDocumentText']=='Y':
                        replace_line('enable.conf',10,'OpenDocumentText=N\n')
                    elif enable['Modules/Outputs']['OpenDocumentText']=='N':
                        replace_line('enable.conf',10,'OpenDocumentText=Y\n')
                elif value=='Y':
                    replace_line('enable.conf',10,'OpenDocumentText=Y\n')
                elif value=='N':
                    replace_line('enable.conf',10,'OpenDocumentText=N\n')
                else:
                    console.exit('Invalid value')

            elif target=='StrapDownJS':
                if value=='none':
                    if enable['Modules/Outputs']['StrapDownJS']=='Y':
                        replace_line('enable.conf',11,'StrapDownJS=N\n')
                    elif enable['Modules/Outputs']['StrapDownJS']=='N':
                        replace_line('enable.conf',11,'StrapDownJS=Y\n')
                elif value=='Y':
                    replace_line('enable.conf',11,'StrapDownJS=Y\n')
                elif value=='N':
                    replace_line('enable.conf',11,'StrapDownJS=N\n')
                else:
                    console.exit('Invalid value')

            elif target=='TKinterApp':
                if value=='none':
                    if enable['Modules/Outputs']['TKinterApp']=='Y':
                        replace_line('enable.conf',12,'TKinterApp=N\n')
                    elif enable['Modules/Outputs']['TKinterApp']=='N':
                        replace_line('enable.conf',12,'TKinterApp=Y\n')
                elif value=='Y':
                    replace_line('enable.conf',12,'TKinterApp=Y\n')
                elif value=='N':
                    replace_line('enable.conf',12,'TKinterApp=N\n')
                else:
                    console.exit('Invalid value')
            else:
                console.exit('Invalid module')
        else:
            console.exit('Invalid group')
    else:
        console.exit('Invalid config file')