# -*- coding: utf-8 -*-
import re
import sys
import unicodedata
import constants
import mm

class Syllables():
    def __init__(self):
        pass

    def handle(self, paragraph):
        paragraph = unicode(paragraph, 'utf-8')
        paragraph = unicodedata.normalize('NFC', paragraph)

        regexes = []
        regexes.extend([constants.FULL_DATE,constants.DATE_MONTH,constants.MONTH_YEAR, constants.TIME])
        regexes.extend([constants.URL,constants.EMAIL])
        regexes.extend([constants.SHORT_NAME])
        regexes.extend([constants.NUMBER, constants.WORD, constants.NOT_WORD, constants.ALL_CAP, constants.SPECIAL_CHAR, constants.COST_MONEY])
        regexes.extend(constants.ABBREVIATION)
        regexes.extend(constants.EXCEPTION)
        regexes.extend([constants.EOS_PUNCTUATION, constants.PUNCTUATION, constants.ELLIPSIS])

        regexes = "(" + "|".join(regexes) + ")"
        if sys.version_info < (3, 0):
            regexes = regexes.decode('utf-8')
        
        syls = re.findall(regexes, paragraph, re.UNICODE)
    
        return [syl[0] for syl in syls]

    def split_sentences(self, string):
        f = open(string, 'r')
        sentences = []
        for line in f.readlines():
            for sentence in re.split(constants.SENTENCES, line):
                if sentence != '' and '\n' not in sentence:
                    sentences.append(sentence.strip())
        f.close()
        return sentences

    def main(self):
        # f = open('test2.txt', 'r')
        # string = ''.join(f.readlines())
        string = 'Khi thi đại học là một mình mình đi thi, làm bài nhưng 4 năm đại học để được danh hiệu như hiện tại còn có sự giúp đỡ của bạn bè, thầy cô. Cấp 3 là một bài thi để vào trường, còn ĐH lại là kết quả rèn luyện của cả 4 năm nên Phương Anh nghĩ điểm số cũng có sự đóng góp của nhiều tố khác nữa nên mỗi danh hiệu đều có một cảm xúc riêng. T. 9/10/1000'
        result = self.handle(string)
        # s = self.joinSentences(result)
        print (result)
        # print (sentences)
        

if __name__ =='__main__':
    a = Syllables()
    a.main()
