# -*- coding: utf-8 -*-
from word_tag import Word_tag
import syllables
import re
import constants
# import sys

class MaxMatchWordSegmenter:
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    histogram = {}
    middle_n = []
    fam_n = []
    one_syl =[]
    dic = []

    # f1 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/VNDic_UTF-8.txt', 'r')
    # for line in f1.readlines():
    #     if line.startswith('##'):
    #         l = line.replace('\n','')
    #         dic.append(l[2:].lower())
    # f1.close()

    f1 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/Dict-UTF8.txt', 'r')
    for line in f1.readlines():
        if not line.startswith('##') and ' ' in line:
            broken = line.strip().split(' ')
            word = broken[0].replace('_', ' ')
            dic.append(word.lower())
    f1.close()

    f2 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/locations.txt', 'r')
    for line in f2.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f2.close()

    f3 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/country_names.txt', 'r')
    for line in f3.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f3.close()

    f4 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/middle_names.txt', 'r')
    for line in f4.readlines():
        l = line.replace('\n','')
        middle_n.append(l.strip())
    f4.close()

    f5 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/family_names.txt', 'r')
    for line in f5.readlines():
        l = line.replace('\n','')
        fam_n.append(l.strip())
    f5.close()

    f6 = open('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/Dictionary/one_syl.txt', 'r')
    for line in f6.readlines():
        l = line.replace('\n','')
        one_syl.append(l.strip())
    f6.close()

    not_words_ = [u'_' , u'#', u'$', u'!', u'"',  u'&', u"'", u'(', u')', u'*', u'+', u',', u'-', u'.', u':', u';', u'=', u'>', u'?', u'(', u')', u'[', u']',
                u'{', u'}', u'@', u'$', u'”', u'“', u'–', u'/', u'…']

    def max_match(self, tokens):
        lowTokens = [x.lower() for x in tokens]
        senLength = len(tokens)
        i = 0
        wordtags = []
        pattern_per = re.compile(constants.PERCENTAGE)
        pattern_sn = re.compile(constants.SHORT_NAME)
        pattern_ell = re.compile(constants.ELLIPSIS)
        pattern_pn = re.compile(constants.PHONE_NUMBER)
        pattern_time = re.compile(constants.TIME)
        pattern_dm = re.compile(constants.DATE_MONTH)
        pattern_my = re.compile(constants.MONTH_YEAR)
        pattern_full = re.compile(constants.FULL_DATE)
        pattern_cap = re.compile(constants.ALL_CAP)
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
                for j in range (min(i + 6, senLength), i+1, -1):
                    Word = ' '.join(tokens[i:j])
                    word = ' '.join(lowTokens[i:j])
                    not_normal = ''.join(tokens[i:j])
                    if (word in self.dic):
                        self.histogram[Word] = self.histogram.get(Word, 0) + 1
                        wordtags.append(Word_tag(token,'B'))
                        for k in range(i+1,j,1):
                            wordtags.append(Word_tag(tokens[k],"I"))
                        i = j -1
                        isSingleSyl =False
                        break
                    if (pattern_cap.match(token) and pattern_sn.match(''.join(tokens[(i+1):j]))):
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                        wordtags.append(Word_tag(token,'B'))
                        isSingleSyl = False
                        break
                    if (pattern_sn.match(not_normal)):
                        self.histogram[not_normal] = self.histogram.get(not_normal, 0) + 1
                        wordtags.append(Word_tag(token,'B'))
                        wordtags.append(Word_tag(tokens[i+1], 'I'))
                        i = j -1
                        isSingleSyl =False
                        break
                    if (pattern_dm.match(not_normal) or pattern_full.match(not_normal) or pattern_my.match(not_normal)):
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                        wordtags.append(Word_tag(token,'B'))
                        for k in range(i+1,j,1):
                            wordtags.append(Word_tag(tokens[k],"I"))
                        i = j -1
                        isSingleSyl =False
                        break
                if (isSingleSyl):
                    lowToken = lowTokens[i]
                    if (token[0].islower() or lowToken in self.one_syl):
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                        wordtags.append(Word_tag(token, 'B'))
                        i += 1
                        continue
                    ilower = i+1
                    for ilower in range(i+1, min(i+4, senLength)):
                        nToken = tokens[ilower]
                        if (nToken[0].islower() or nToken in self.not_words_):
                            break
                    if (ilower > i):
                        notMiddleName = True
                        if (lowToken in self.middle_n and i >= 1):
                            prev = tokens[i - 1]
                            if (prev[0].isupper()):
                                prevL = prev.lower()
                                if (prevL in self.fam_n):
                                    wordtags.append(Word_tag(token, 'I'))
                                    notMiddleName = False
                        if (notMiddleName):
                            temp = ' '.join(tokens[i:ilower])
                            self.histogram[temp] = self.histogram.get(temp, 0) + 1
                            wordtags.append(Word_tag(token, 'B'))
                        for k in range(i+1, ilower):
                            wordtags.append(Word_tag(tokens[k], 'I'))

                        i = ilower
                        continue
                    else:
                        self.histogram[token] = self.histogram.get(token, 0) + 1
                        wordtags.append(Word_tag(token, 'B'))

            else:
                for j in range (min(i + 5, senLength), i+1, -1):
                    not_normal = ''.join(tokens[i:j])
                    if (pattern_ell.match(not_normal) or pattern_time.match(not_normal) or pattern_pn.match(not_normal) or pattern_per.match(not_normal)
                         or pattern_full.match(not_normal) or pattern_my.match(not_normal) or pattern_dm.match(not_normal)):
                        wordtags.append(Word_tag(token,'B'))
                        for k in range(i+1,j,1):
                            wordtags.append(Word_tag(tokens[k],"I"))
                        i = j -1
                        break
                else:
                    wordtags.append(Word_tag(token, 'B'))
            i += 1
        return wordtags

    def main(self):
        syl = syllables.Syllables()
        f = open ('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/MaximumMatching/output2.txt', 'a')
        sentences = syl.split_sentences('/home/vudat1710/Downloads/Project-1--20181-Word-Segmentation/CrawlData/dantri/data2.txt')
        for sentence in sentences:
            result = syl.handle(''.join(sentence))
            words = self.max_match(result)  
            for i in words:
                f.write(i.word.strip())
                f.write('\t')
                f.write(i.tag.strip())
                f.write('\n')
            f.write('\n')  
        f.close()
        # f = open('histogram.txt','a')
        # for word, count in sorted(self.histogram.items(), key=lambda x:x[::-1], reverse=True):
        #     f.write(word)
        #     f.write("   ")
        #     f.write(str(count))
        #     f.write("\n")
        # f.close()

if __name__ =='__main__':
    a = MaxMatchWordSegmenter()
    a.main()
