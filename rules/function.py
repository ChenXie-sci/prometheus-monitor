import time
import os
import shutil
import pycurl


def change():
    oldtime = time.time()

    #boundary = at + b
    with open("hoststats-alert-rules.yml") as f:
        contents = f.read()

    bound = float(contents[212:218])
    #print(contents[212:218])

    time.sleep(1)
    newtime = time.time() - oldtime
    k = 0.1
    if((bound - k * newtime) > 0):
        bound = format(bound - k * newtime, '.4f')
    else:
        bound = 0.000

    string = str(bound)
    content_list = list(contents)
    for i in range(len(string)):
        content_list[212+i] = string[i]
    contents = ''.join(content_list)
    for i in range(0, 5):
        contents += ' '
    print(bound)
    #print(contents)
    #print((contents))
    def save_to_file(file_name, contents):
        fh = open(file_name, 'w')
        fh.write(contents)
        fh.close()

    save_to_file('hoststats-alert-rules.yml', contents)
    c = pycurl.Curl()
    checkurl = "http://localhost:9090/-/reload"
    c.setopt(pycurl.URL, checkurl)
    c.setopt(c.POST, 1)
    c.perform()
while(1):
    change()


