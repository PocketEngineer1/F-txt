import configparser
import platform
import console
import shutil
import json
import sys
import os

file=open("version.json")
pkg=file.read()
file.close()
pkg=json.loads(pkg)

if pkg['py_ver']!=platform.python_version():
    console.warn('This program was compiled/written for python '+pkg['py_ver']+', and  may not work with your currently installed version of python')

console.info('App Version: '+str(pkg['app_ver']['release'])+'.'+str(pkg['app_ver']['major'])+'.'+str(pkg['app_ver']['minor'])+'.'+str(pkg['app_ver']['patch']))

if os.path.exists('defaults.conf'):
    defaults=configparser.ConfigParser()
    defaults.sections()
    defaults.read('defaults.conf')
else:
    file=open('defaults.conf','w')
    file.write('; Valid formats: HTML, Markdown, StrapDown JS, TKinter App, Microsoft Word, OpenDocument Text\n[FORMAT]\nformat=StrapDown JS\n[DOC]\ntitle=Unnamed Document\nfavicon=\nbackground=#FFFFFF\ntext=#000000\nwidth=auto\nheight=auto\n[EXTENSIONS]\nHTML=.html\nMarkdown=.mdtxt\nStrapDownJS=.StrapDownJS.html\nTKinterApp=.TKinter.py\nMicrosoftWord=.docx\nOpenDocumentText=.odt')
    file.close()

    defaults=configparser.ConfigParser()
    defaults.sections()
    defaults.read('defaults.conf')

if os.path.exists('output.conf')!=True:
    file=open('output.conf','w')
    file.write("[HTML]\n\n[StrapDown JS]\n\n[Markdown]\n\n[TKinterApp]\nResize_X=Y\nResize_Y=Y\n[Microsoft Word]\n\n[OpenDocument Text]\n\n; Use 'Y' to enable and 'N' to disable")
    file.close()

if os.path.exists('enable.conf'):
    ModulesEnabled=configparser.ConfigParser()
    ModulesEnabled.sections()
    ModulesEnabled.read('enable.conf')
else:
    file=open('enable.conf','w')
    file.write("[Modules]\nConfigure=Y\n[Modules/Interfaces]\nGUI=Y\nCLI=Y\nWebUI=Y\n[Modules/Outputs]\nHTML=Y\nMarkdown=Y\nMicrosoftWord=Y\nOpenDocument=Y\nStrapDownJS=Y\nTKinterApp=Y\n; Use 'Y' to enable and 'N' to disable")
    file.close()

    ModulesEnabled=configparser.ConfigParser()
    ModulesEnabled.sections()
    ModulesEnabled.read('enable.conf')

ModulesInstalled={
    'Configure':False,
    'Upgrade':False,
    'Interfaces':{
        'GUI':False,
        'CLI':False,
        'WebUI':False
    },
    'Outputs':{
        'HTML':False,
        'Markdown':False,
        'MicrosoftWord':False,
        'OpenDocumentText':False,
        'StrapDownJS':False,
        'TKinterApp':False
    }
}

ModuleVersions={
    'Configure':None,
    'Upgrade':None,
    'Interfaces':{
        'GUI':None,
        'CLI':None,
        'WebUI':None
    },
    'Outputs':{
        'HTML':None,
        'Markdown':None,
        'MicrosoftWord':None,
        'OpenDocumentText':None,
        'StrapDownJS':None,
        'TKinterApp':None
    }
}

Modules={
    'Configure':'Modules/Configure.py',
    'Upgrade':'Modules/Upgrade.py',
    'Interfaces':{
        'GUI':'Modules/Interfaces/GUI.py',
        'CLI':'Modules/Interfaces/CLI.py',
        'WebUI':'Modules/Interfaces/WebUI.py'
    },
    'Outputs':{
        'HTML':'Modules/Outputs/HTML.py',
        'Markdown':'Modules/Outputs/Markdown.py',
        'MicrosoftWord':'Modules/Outputs/MicrosoftWord.py',
        'OpenDocumentText':'Modules/Outputs/OpenDocumentText.py',
        'StrapDownJS':'Modules/Outputs/StrapDownJS.py',
        'TKinterApp':'Modules/Outputs/TKinterApp.py'
    }
}

if os.path.exists(Modules['Outputs']['HTML']):
    import Modules.Outputs.HTML as HTML
    ModulesInstalled['Outputs']['HTML']=True
    ModuleVersions['Outputs']['HTML']=HTML.version

if os.path.exists(Modules['Outputs']['Markdown']):
    import Modules.Outputs.Markdown as Markdown
    ModulesInstalled['Outputs']['Markdown']=True
    ModuleVersions['Outputs']['Markdown']=Markdown.version

if os.path.exists(Modules['Outputs']['MicrosoftWord']):
    import Modules.Outputs.MicrosoftWord as MicrosoftWord
    ModulesInstalled['Outputs']['MicrosoftWord']=True
    ModuleVersions['Outputs']['MicrosoftWord']=MicrosoftWord.version

if os.path.exists(Modules['Outputs']['OpenDocumentText']):
    import Modules.Outputs.OpenDocumentText as OpenDocumentText
    ModulesInstalled['Outputs']['OpenDocumentText']=True
    ModuleVersions['Outputs']['OpenDocumentText']=OpenDocumentText.version

if os.path.exists(Modules['Outputs']['StrapDownJS']):
    import Modules.Outputs.StrapDownJS as StrapDownJS
    ModulesInstalled['Outputs']['StrapDownJS']=True
    ModuleVersions['Outputs']['StrapDownJS']=StrapDownJS.version

if os.path.exists(Modules['Outputs']['TKinterApp']):
    import Modules.Outputs.TKinterApp as TKinterApp
    ModulesInstalled['Outputs']['TKinterApp']=True
    ModuleVersions['Outputs']['TKinterApp']=TKinterApp.version

if os.path.exists(Modules['Interfaces']['GUI']):
    import Modules.Interfaces.GUI as GUI
    ModulesInstalled['Interfaces']['GUI']=True
    ModuleVersions['Interfaces']['GUI']=GUI.version

if os.path.exists(Modules['Interfaces']['CLI']):
    import Modules.Interfaces.CLI as CLI
    ModulesInstalled['Interfaces']['CLI']=True
    ModuleVersions['Interfaces']['CLI']=CLI.version

if os.path.exists(Modules['Interfaces']['WebUI']):
    import Modules.Interfaces.WebUI as WebUI
    ModulesInstalled['Interfaces']['WebUI']=True
    ModuleVersions['Interfaces']['WebUI']=WebUI.version

if os.path.exists(Modules['Configure']):
    import Modules.Configure as Configure
    ModulesInstalled['Configure']=True
    ModuleVersions['Configure']=Configure.version

if os.path.exists(Modules['Upgrade']):
    import Modules.Upgrade as Upgrade
    ModulesInstalled['Upgrade']=True
    ModuleVersions['Upgrade']=Upgrade.version

args=sys.argv
if len(args)==2:
    one=args[1]

    if one=='configure':
        if ModulesEnabled['Modules']['Configure']=='Y':
            if one=='configure':
                if ModulesInstalled['Configure']==True:
                    Configure.__init__()
                else:
                    console.exit("The module 'Configure is not installed'")
        else:
            console.error("The module 'Configure' is disabled!")
            console.error("The module 'Configure' is disabled?")
            console.exit("Why is the module 'Configure' disabled?")

    elif one=='upgrade':
        if ModulesEnabled['Modules']['Upgrade']=='Y':
            if one=='Upgrade':
                if ModulesInstalled['Upgrade']==True:
                    Upgrade.__init__()
                else:
                    console.exit("The module 'Upgrade is not installed'")
        else:
            console.error("The module 'Upgrade' is disabled!")
            console.error("The module 'Upgrade' is disabled?")
            console.exit("Why is the module 'Upgrade' disabled?")

    elif defaults['FORMAT']['format']=='HTML':
        if ModulesEnabled['Modules/Outputs']['HTML']=='Y':
            if ModulesInstalled['Outputs']['HTML']==True:
                HTML.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['HTML'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['HTML'])
            else:
                console.exit("The output module 'HTML' is not installed!")
        else:
            console.exit("The output module 'HTML' is disabled!")

    elif defaults['FORMAT']['format']=='StrapDownJS':
        if ModulesEnabled['Modules/Outputs']['StrapDownJS']=='Y':
            if ModulesInstalled['Outputs']['StrapDownJS']==True:
                StrapDownJS.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['StrapDownJS'])
            else:
                console.exit("The output module 'StrapDownJS' is not installed!")
        else:
            console.exit("The output module 'StrapDownJS' is disabled!")

    elif defaults['FORMAT']['format']=='Markdown':
        if ModulesEnabled['Modules/Outputs']['Markdown']=='Y':
            if ModulesInstalled['Outputs']['Markdown']==True:
                Markdown.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['Markdown'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['Markdown'])
            else:
                console.exit("The output module 'Markdown' is not installed!")
        else:
            console.exit("The output module 'Markdown' is disabled!")

    elif defaults['FORMAT']['format']=='TKinterApp':
        if ModulesEnabled['Modules/Outputs']['TKinterApp']=='Y':
            if ModulesInstalled['Outputs']['TKinterApp']==True:
                TKinterApp.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['TKinterApp'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['TKinterApp'])
            else:
                console.exit("The output module 'TKinterApp' is not installed!")
        else:
            console.exit("The output module 'TKinterApp' is disabled!")

    elif defaults['FORMAT']['format']=='MicrosoftWord':
        if ModulesEnabled['Modules/Outputs']['MicrosoftWord']=='Y':
            if ModulesInstalled['Outputs']['MicrosoftWord']==True:
                MicrosoftWord.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['MicrosoftWord'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['MicrosoftWord'])
            else:
                console.exit("The output module 'MicrosoftWord' is not installed!")
        else:
            console.exit("The output module 'MicrosoftWord' is disabled!")

    elif defaults['FORMAT']['format']=='OpenDocumentText':
        if ModulesEnabled['Modules/Outputs']['OpenDocumentText']=='Y':
            if ModulesInstalled['Outputs']['OpenDocumentText']==True:
                OpenDocumentText.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['OpenDocumentText'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['OpenDocumentText'])
            else:
                console.exit("The output module 'OpenDocumentText' is not installed!")
        else:
            console.exit("The output module 'OpenDocumentText' is disabled!")

elif len(args)==3:
    one=args[1]
    two=args[2]

    if one=='configure':
        if ModulesEnabled['Modules']['Configure']=='Y':
            if one=='configure':
                if ModulesInstalled['Configure']==True:
                    Configure.__init__(two)
                else:
                    console.exit("The module 'Configure' is not installed!")
        else:
            console.error("The module 'Configure' is disabled!")
            console.exit("The module 'Configure' is disabled? Why is the module 'Configure' disabled?")

    elif two=='HTML':
        if ModulesEnabled['Modules/Outputs']['HTML']=='Y':
            if ModulesInstalled['Outputs']['HTML']==True:
                HTML.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['HTML'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['HTML'])
            else:
                console.exit("The output module 'HTML' is not installed!")
        else:
            console.exit("The output module 'HTML' is disabled!")

    elif two=='StrapDownJS':
        if ModulesEnabled['Modules/Outputs']['StrapDownJS']=='Y':
            if ModulesInstalled['Outputs']['StrapDownJS']==True:
                StrapDownJS.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['StrapDownJS'])
            else:
                console.exit("The output module 'StrapDownJS' is not installed!")
        else:
            console.exit("The output module 'StrapDownJS' is disabled!")

    elif two=='Markdown':
        if ModulesEnabled['Modules/Outputs']['Markdown']=='Y':
            if ModulesInstalled['Outputs']['Markdown']==True:
                Markdown.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['Markdown'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['Markdown'])
            else:
                console.exit("The output module 'Markdown' is not installed!")
        else:
            console.exit("The output module 'Markdown' is disabled!")

    elif two=='TKinterApp':
        if ModulesEnabled['Modules/Outputs']['TKinterApp']=='Y':
            if ModulesInstalled['Outputs']['TKinterApp']==True:
                TKinterApp.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['TKinterApp'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['TKinterApp'])
            else:
                console.exit("The output module 'TKinterApp' is not installed!")
        else:
            console.exit("The output module 'TKinterApp' is disabled!")
        
    elif two=='MicrosoftWord':
        if ModulesEnabled['Modules/Outputs']['MicrosoftWord']=='Y':
            if ModulesInstalled['Outputs']['MicrosoftWord']==True:
                MicrosoftWord.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['MicrosoftWord'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['MicrosoftWord'])
            else:
                console.exit("The output module 'MicrosoftWord' is not installed!")
        else:
            console.exit("The output module 'MicrosoftWord' is disabled!")

    elif two=='OpenDocumentText':
        if ModulesEnabled['Modules/Outputs']['OpenDocumentText']=='Y':
            if ModulesInstalled['Outputs']['OpenDocumentText']==True:
                OpenDocumentText.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['OpenDocumentText'],os.path.splitext(one)[0]+defaults['EXTENSIONS']['OpenDocumentText'])
            else:
                console.exit("The output module 'OpenDocumentText' is not installed!")
        else:
            console.exit("The output module 'OpenDocumentText' is disabled!")

elif len(args)==4:
    one=args[1]
    two=args[2]
    three=args[3]

    if one=='configure':
        if ModulesEnabled['Modules']['Configure']=='Y':
            if ModulesInstalled['Configure']==True:
                Configure.__init__(two,three)
            else:
                console.exit("The module 'Configure' is not installed!")
        else:
            console.error("The module 'Configure' is disabled!")
            console.exit("The module 'Configure' is disabled? Why is the module 'Configure' disabled")

    elif three=='HTML':
        if ModulesEnabled['Modules/Outputs']['HTML']=='Y':
            if ModulesInstalled['Outputs']['HTML']==True:
                HTML.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['HTML'],os.path.splitext(one)[0]+two+defaults['EXTENSIONS']['HTML'])
            else:
                console.exit("The output module 'HTML' is not installed!")
        else:
            console.exit("The output module 'HTML' is disabled!")

    elif three=='StrapDownJS':
        if ModulesEnabled['Modules/Outputs']['StrapDownJS']=='Y':
            if ModulesInstalled['Outputs']['StrapDownJS']==True:
                StrapDownJS.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['StrapDownJS'],os.path.splitext(one)[0]+two+defaults['EXTENSIONS']['StrapDownJS'])
            else:
                console.exit("The output module 'StrapDownJS' is not installed!")
        else:
            console.exit("The output module 'StrapDownJS' is disabled!")

    elif three=='Markdown':
        if ModulesEnabled['Modules/Outputs']['Markdown']=='Y':
            if ModulesInstalled['Outputs']['Markdown']==True:
                Markdown.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['Markdown'],os.path.splitext(one)[0]+two+defaults['EXTENSIONS']['Markdown'])
            else:
                console.exit("The output module 'Markdown' is not installed!")
        else:
            console.exit("The output module 'Markdown' is disabled!")

    elif three=='TKinterApp':
        if ModulesEnabled['Modules/Outputs']['TKinterApp']=='Y':
            if ModulesInstalled['Outputs']['TKinterApp']==True:
                TKinterApp.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['TKinterApp'],os.path.splitext(one)[0]+two+defaults['EXTENSIONS']['TKinterApp'])
            else:
                console.exit("The output module 'TKinterApp' is not installed!")
        else:
            console.exit("The output module 'TKinterApp' is disabled!")

    elif three=='MicrosoftWord':
        if ModulesEnabled['Modules/Outputs']['MicrosoftWord']=='Y':
            if ModulesInstalled['Outputs']['MicrosoftWord']==True:
                MicrosoftWord.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['MicrosoftWord'],os.path.splitext(one)[0]+two+defaults['EXTENSIONS']['MicrosoftWord'])
            else:
                console.exit("The output module 'MicrosoftWord' is not installed!")
        else:
            console.exit("The output module 'MicrosoftWord' is disabled!")

    elif three=='OpenDocumentText':
        if ModulesEnabled['Modules/Outputs']['OpenDocumentText']=='Y':
            if ModulesInstalled['Outputs']['OpenDocumentText']==True:
                OpenDocumentText.__init__(one)
                shutil.copyfile('TMP/output'+defaults['EXTENSIONS']['OpenDocumentText'],os.path.splitext(one)[0]+two+defaults['EXTENSIONS']['OpenDocumentText'])
            else:
                console.exit("The output module 'OpenDocumentText' is not installed!")
        else:
            console.exit("The output module 'OpenDocumentText' is disabled!")

elif len(args)==5:
    one=args[1]
    two=args[2]
    three=args[3]
    four=args[4]

    if one=='configure':
        if ModulesEnabled['Modules']['Configure']=='Y':
            if ModulesInstalled['Configure']==True:
                Configure.__init__(two,three,four)
            else:
                console.exit("The module 'Configure' is not installed!")
        else:
            console.error("The module 'Configure' is disabled!")
            console.exit("The module 'Configure' is disabled? Why is the module 'Configure' disabled")

elif len(args)==6:
    one=args[1]
    two=args[2]
    three=args[3]
    four=args[4]
    five=args[5]

    if one=='configure':
        if ModulesEnabled['Modules']['Configure']=='Y':
            if ModulesInstalled['Configure']==True:
                Configure.__init__(two,three,four,five)
            else:
                console.exit("The module 'Configure' is not installed!")
        else:
            console.error("The module 'Configure' is disabled!")
            console.exit("The module 'Configure' is disabled? Why is the module 'Configure' disabled")

else:
    if ModulesEnabled['Modules/Interfaces']['GUI']=='Y' and ModulesEnabled['Modules/Interfaces']['CLI']=='Y' and ModulesEnabled['Modules/Interfaces']['WebUI']=='Y':
        console.exit("Modules 'CLI', 'GUI', and 'WebUI' are incompatable! Please disable one of them with the 'Configure' module, or by editing the file 'enable.conf'.")
    elif ModulesEnabled['Modules/Interfaces']['GUI']=='Y' and ModulesEnabled['Modules/Interfaces']['CLI']=='Y':
        console.exit("Modules 'CLI', and 'GUI' are incompatable! Please disable one of them with the 'Configure' module, or by editing the file 'enable.conf'.")
    elif ModulesEnabled['Modules/Interfaces']['GUI']=='Y' and ModulesEnabled['Modules/Interfaces']['WebUI']=='Y':
        console.exit("Modules 'GUI', and 'WebUI' are incompatable! Please disable one of them with the 'Configure' module, or by editing the file 'enable.conf'.")
    elif ModulesEnabled['Modules/Interfaces']['CLI']=='Y' and ModulesEnabled['Modules/Interfaces']['WebUI']=='Y':
        console.exit("Modules 'CLI', and 'WebUI' are incompatable! Please disable one of them with the 'Configure' module, or by editing the file 'enable.conf'.")
    elif ModulesEnabled['Modules/Interfaces']['GUI']=='N' and ModulesEnabled['Modules/Interfaces']['CLI']=='N' and ModulesEnabled['Modules/Interfaces']['WebUI']=='N':
        console.exit("Please enable at least one interface module.")

    elif ModulesEnabled['Modules/Interfaces']['GUI']=='Y':
        if ModulesInstalled['Interfaces']['GUI']==True:
            GUI.__init__()
        else:
            console.exit("The interface module 'GUI' is not installed!")

    elif ModulesEnabled['Modules/Interfaces']['CLI']=='Y':
        if ModulesInstalled['Interfaces']['CLI']==True:
            CLI.__init__()
        else:
            console.exit("The interface module 'WebUI' is not installed!")

    elif ModulesEnabled['Modules/Interfaces']['WebUI']=='Y':
        if ModulesInstalled['Interfaces']['WebUI']==True:
            WebUI.__init__()
        else:
            console.exit("The interface module 'CLI' is not installed!")

    else:
        console.exit('Something went wrong!')
        