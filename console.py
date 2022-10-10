from datetime import datetime
import sys

def log(log):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('['+current_time+'] LOG: '+log)

def info(info):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('['+current_time+'] INFO: '+info)

def warn(warn):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('['+current_time+'] WARN: '+warn)

def error(error):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('['+current_time+'] ERROR: '+error)

def exit(exit):
    sys.exit(error(exit))