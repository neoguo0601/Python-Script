import re

folder = ''
script = folder + ''
voiceName = ''
locale = ''
mixCountOfCentence = 3
template = '<speak version="1.0" xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="%s" xmlns="http://www.w3.org/2001/10/synthesis"><voice name="%s">%s</voice></speak>'

newScript = folder + voiceName.replace(' ', '_') + '.txt'

dr = re.compile(r'<[^>]+>',re.S)

dataList  = []

with open(script, 'r', encoding='utf-16') as s:
    for line in s:
        data = dr.sub('',line)
        if len(data) > mixCountOfCentence:
            dataList.append(data)
                
sorted(dataList)

with open(newScript, 'w', encoding='utf-16') as ns:
    for data in dataList:
        ns.write(template % (locale, voiceName, data.strip())+ '\n')

