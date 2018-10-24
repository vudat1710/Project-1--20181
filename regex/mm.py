# -*- coding: utf-8 -*-
from word_tag import Word_tag
import syllables
import re
import constants
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

class MaxMatchWordSegmenter:
    reload(sys)
    sys.setdefaultencoding('utf8')
    dic = []
    histogram = {}
    f1 = open('VNDic_UTF-8.txt', 'r')
    for line in f1.readlines():
        if line.startswith('##'):
            l = line.replace('\n','')
            dic.append(l[2:].lower())
    f1.close()

    f2 = open('locations.txt', 'r')
    for line in f2.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f2.close()

    f3 = open('country_names.txt', 'r')
    for line in f3.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f3.close()

    # f4 = open('country_s_names.txt', 'r')
    # for line in f4.readlines():
    #     l = line.replace('\n','')
    #     dic.append(l.strip())
    # f4.close()

    f4 = open('vnpernames.txt', 'r')
    for line in f4.readlines():
        l = line.replace('\n','')
        dic.append(l.strip().lower())
    f4.close()

    # f8 = open('Viet74K.txt', 'r')
    # for line in f8.readlines():
    #     l = line.replace('\n', '')
    #     dic.append(l.strip().lower())

    not_words_ = [u'_' , u'#', u'$', u'!', u'"',  u'&', u"'", u'(', u')', u'*', u'+', u',', u'-', u'.', u':', u';', u'=', u'>', u'?', u'(', u')', u'[', u']',
                u'{', u'}', u'@', u'$', u'”', u'“', u'–', u'/', u'…']

    def max_match(self, tokens):
        lowTokens = []
        lowTokens = [x.lower() for x in tokens]
        senLength = len(tokens)
        i = 0
        wordtags = []
        while i < senLength:
            token = tokens[i]
            if (token.isalpha()):
                if (token[0].islower() and (i+1) < senLength):
                    a = tokens[i+1]
                    if (a[0].isupper()):
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                        wordtags.append(Word_tag(token, 'B'))
                        i += 1
                        continue
                
                isSingleSyl = True
                for j in range (min(i + 4, senLength), i+1, -1):
                    word = ' '.join(lowTokens[i:j]).encode('utf-8')
                    if (word in self.dic):
                        self.histogram[word] = self.histogram.get(word, 0) + 1
                        wordtags.append(Word_tag(token,'B'))
                        for k in range(i+1,j,1):
                            wordtags.append(Word_tag(tokens[k],"I"))
                        i = j -1
                        isSingleSyl =False
                        break
                if (isSingleSyl):
                    if (token not in self.not_words_):
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                    wordtags.append(Word_tag(token, 'B'))

                        
            else:
                if (not token[0].isdigit() and token not in self.not_words_):
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                pattern_sn = re.compile(constants.SHORT_NAME)
                pattern_ell = re.compile(constants.ELLIPSIS)
                pattern_email = re.compile(constants.EMAIL)
                pattern_pn = re.compile(constants.PHONE_NUMBER)
                if (token[0].isdigit()):
                    words = re.split("(\W+)",token)
                    wordtags.append(Word_tag(words[0], 'B'))
                    for j in range(1, len(words)):
                        wordtags.append(Word_tag(words[j], 'I'))
                    i += 1
                    continue
                elif(pattern_sn.match(token)):
                    temp_words = re.split("(\W+)",token)
                    words = filter(lambda x: x != '', temp_words)
                    wordtags.append(Word_tag(words[0], 'B'))
                    for j in range(1, len(words)):
                        wordtags.append(Word_tag(words[j], 'I')) 
                    i += 1
                    continue
                elif(pattern_ell.match(token)):
                    temp_words = re.split("(\.)",token)
                    words = filter(lambda x: x != '', temp_words)
                    wordtags.append(Word_tag(words[0], 'B'))
                    for j in range(1, len(words)):
                        wordtags.append(Word_tag(words[j], 'I'))
                    i += 1
                    continue
                elif(pattern_email.match(token)):
                    words = re.split("([\W_-]+)", token)
                    for j in range(0, len(words)):
                        wordtags.append(Word_tag(words[j], 'B'))
                    i += 1
                    continue
                elif(pattern_pn.match(token)):
                    words = re.split("(\W+)", token)
                    wordtags.append(Word_tag(words[0], 'B'))
                    for j in range(1, len(words)):
                        wordtags.append(Word_tag(words[j], 'I'))
                    i += 1
                    continue
                else:
                    wordtags.append(Word_tag(token, 'B'))

            i += 1
        return wordtags

    def main(self):
        # result = [u'H.', u'Bắt', 'nghi', 'can', u'đâm', u'cụ', u'bà', u'để', u'cướp', u'tài', u'sản', u'Ngày', '9/10', ',', u'Công', u'an', u'huyện', u'Đông', 'Giang', '(', u'Quảng', u'Nam', ')', 'cho', u'biết', ',', u'đang', u'tạm', u'giữ', u'hình', u'sự', 'nghi', u'phạm', u'Nguyễn', u'Văn', u'Hải', '(', 'SN', '2002', ',', u'trú', u'xã', 'Ba', ',', u'huyện', u'Đông', u'Giang', ')', u'để', u'tiếp', u'tục', u'điều', 'tra', ',', u'làm', u'rõ', u'về', u'hành', 'vi', u'cướp', u'tài', u'sản', u'và', u'có', u'dấu', u'hiệu', u'phạm', u'tội', u'giết', u'người', '.']
        f = open('test.txt', 'r')
        string = ''.join(f.readlines())
        syl = syllables.Syllables()
        result = syl.handle(string)
        # s = [x.decode('utf-8') for x in result]
        words = self.max_match(result)
        f = open ('output.txt', 'a')
        for i in words:
            f.write(i.word.strip().encode('utf-8'))
            f.write('   ')
            f.write(i.tag.strip())
            f.write('\n')
        f.close()    

        # Plot histogram 
        # df = pd.DataFrame.from_dict(self.histogram, orient='index')
        # df.plot(kind='bar')
        # plt.show()
        f = open('histogram.txt','a')
        for word, count in sorted(self.histogram.iteritems(), key=lambda x:x[::-1]):
            c = str(count)
            f.write(word.encode('utf-8'))
            f.write(" ")
            f.write(c)
            f.write("\n")
        f.close()

if __name__ =='__main__':
    a = MaxMatchWordSegmenter()
    a.main()
