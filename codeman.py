import os
import requests

#goldenconfig file
gc = None
gc_file = None
tasks = []
response = ''

if os.path.exists('gc.txt'):
    gc = 'gc.txt'
    gc_file = open(gc,'r')
    for line in gc_file.readlines():
        if len(line) > 5 and line.split(' ')[0] != '[!Comment]' and line.split(' ')[0] != '[!Manual]':
            tasks.append(line)
        elif len(line)>5 and line.split(' ')[0] != '[!Comment]':
            response = response + line + '\n'
    gc_file.close()
elif os.path.exists('goldenconfig.txt'):
    gc = 'goldenconfig.txt'
    gc_file = open(gc,'r')
    for line in gc_file.readlines():
        if len(line) > 5 and line.split(' ')[0] != '[!Comment]' and line.split(' ')[0] != '[!Manual]':
            tasks.append(line)
        elif len(line)>5 and line.split(' ')[0] != '[!Comment]':
            response = response + line + '\n'
    gc_file.close()
else:
    print('GC not found, trying to get from API ( https://api.vishalvignesh.com/get/barista/wdtcpoc/goldenconfig )...')
    res = requests.get('https://api.vishalvignesh.com/get/barista/wdtcpoc/goldenconfig')
    if res.status_code == 200 and res.raw:
        gc_file = res.text
        for line in gc_file.splitlines():
            if len(line) > 5 and line.split(' ')[0] != '[!Comment]' and line.split(' ')[0] != '[!Manual]':
                tasks.append(line)
            elif len(line)>5 and line.split(' ')[0] != '[!Comment]':
                response = response + line + '\n'

    else:
        print("GC not found, unable to fetch from API, stopping...")
        exit(0)

if len(tasks) > 1:
    print(tasks)
    for task in tasks:
        print(os.system(task))
        None
    print('\n\n Manual Tasks / Other Comments: ' + response)

