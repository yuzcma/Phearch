imgPath = 'D:/Images/12.jpg'
exeProcess = "hachoir-metadata"
process = subprocess.Popen([exeProcess,imgPath],
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)

for tag in process.stdout:
        line = tag.strip().split(':')
        infoDict[line[0].strip()] = line[-1].strip()

for k,v in infoDict.items():
    print(k,':', v)