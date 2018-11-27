# -*- coding: utf-8 -*-
import mm
class Score():
    f = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/test-BI','r')
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
    f = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/outputtestset2.txt','a')
    m = mm.MaxMatchWordSegmenter()
    for sentence in sentences:
        s = [x for x in sentence]
        words = m.max_match(s)
        for i in words:
            f.write(i.word.strip())
            f.write('\t')
            f.write(i.tag.strip())
            f.write('\n')
        f.write('\n')
    f.close()

    a=open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/test-BI','r').readlines()
    b=open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/outputtestset2.txt','r').readlines()
    with open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/test2.txt','w') as out:
        for i in range(229420):
            temp = b[i].split('\t')
            if (a[i] != '\n' and temp != '\n'):
                out.write(a[i].strip())
                out.write('\t')
                out.write(temp[1])
            else:
                out.write('\n')

 