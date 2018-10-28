# -*- coding: utf-8 -*-
import mm
class Score():
    f = open('test-BI','r')
    result = []
    sentences = []
    for line in f.readlines():
        s = line.split('\t')
        if '\n' in s:
            sentences.append(result)
            result = []
            continue
        result.append(s[0])
    f.close()
    f = open('outputtestset.txt','a')
    m = mm.MaxMatchWordSegmenter()
    for sentence in sentences:
        s = [x.decode('utf-8') for x in sentence]
        words = m.max_match(s)
        for i in words:
            f.write(i.word.strip().encode('utf-8'))
            f.write('\t')
            f.write(i.tag.strip())
            f.write('\n')
        f.write('\n')
    f.close()

    a=open('test-BI','r').readlines()
    b=open('outputtestset.txt','r').readlines()
    with open('test.txt','w') as out:
        for i in range(229420):
            temp = b[i].split('\t')
            if (a[i] != '\n' and temp != '\n'):
                out.write(a[i].strip())
                out.write('\t')
                out.write(temp[1])
            else:
                out.write('\n')

 