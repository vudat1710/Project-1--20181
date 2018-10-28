# -*- coding: utf-8 -*-
from a import Word_tag
import syllables

class MaxMatchWordSegmenter:
    dic = []
    # loc = []
    # country_l =[]
    # country_s = []
    # sent_w = []
    # middle_n =[]
    # fam_n = []
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

    # f3 = open('middle_names.txt', 'r')
    # for line in f3.readlines():
    #     l = line.replace('\n','')
    #     dic.append(l.strip())
    # f3.close()

    # f4 = open('family_names.txt', 'r')
    # for line in f4.readlines():
    #     l = line.replace('\n','')
    #     dic.append(l.strip())
    # f4.close()

    f5 = open('first_sent_words.txt', 'r')
    for line in f5.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f5.close()

    f6 = open('country_names.txt', 'r')
    for line in f6.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f6.close()

    f7 = open('country_s_names.txt', 'r')
    for line in f7.readlines():
        l = line.replace('\n','')
        dic.append(l.strip())
    f7.close()

    f7 = open('vnpernames.txt', 'r')
    for line in f7.readlines():
        l = line.replace('\n','')
        dic.append(l.strip().lower())
    f7.close()
    
    
    # f1 = open('VNDic_UTF-8.txt', 'r')
    # f2 = open('vnlocations.txt', 'r')
    # f3 = open('vnpernames.txt', 'r')
    # dictionary = f1.readlines() + f2.readlines() + f3.readlines()

    # lowDictionary = []
    # f1 = open('VNDic_UTF-8.txt', 'r')
    # for line in f1.readlines():
    #     if line.startswith('##'):
    #         l = line.replace('\n','')
    #         lowDictionary.append(l[2:].lower())

    # f2 = open('vnlocations.txt', 'r')
    # for line in f2.readlines():
    #     l = line.replace('\n','')
    #     lowDictionary.append(l.strip().lower())

    # f3 = open('vnpernames.txt', 'r')
    # for line in f3.readlines():
    #     l = line.replace('\n','')
    #     lowDictionary.append(l.strip().lower())
    # f3.close()
    # f1.close()
    # f2.close()

    # def __init__(self, dictionary):
    #     """
    #     :param dictionary: dictionary containing all words that may be in given strings
    #     """
    #     self.dictionary = dictionary

    # def segment_words(self, string):
    #     """
    #     Segments a sentence into words using the max-match algorithm.  This will attempt to greedily find the largest
    #     words in a sentence, starting at the beginning and moving left-to-right with the remaining string.
    #     :param string: words without spaces separating them
    #     :return: list of words that are a word segmentation of the given string
    #     """
    #     words = []
    #     word_begin = 0
    #     while word_begin < len(string):
    #         e = len(string)
    #         while e > 1:
    #             test_word = ''.join(string[word_begin:e])
    #             if (test_word in self.dictionary):
    #                 break
    #             else:
    #                 e -= 1
    #         word = ''.join(string[word_begin:e])
    #         words.append(word)
    #         word_begin = e + 1
    #         # if e < len(string):
    #         #     e = len(string)
    #     return words

    # def find_longest_word(self, string):
    #     """
    #     Finds the longest word that is a prefix of a given string
    #     :param string: string for which to find the longest word prefix
    #     :return: longest prefix of the given string, or the first letter of the string if there is no word prefix
    #     """
    #     e = len(string)
    #     while e > 1:
    #         test_word = ''.join(string[:e])
    #         if (test_word in self.dictionary):
    #             return test_word
    #         e -= 1
    #     return ''.join(string[0])
    not_words_ = [u'!', u'"',  u'&', u"'", u'(', u')', u'*', u'+', u',', u'-', u'.', u':', u';', u'=', u'>', u'?', u'(', u')', u'[', u']', u'{', u'}']

    # def max_match(self, sentence, dictionary):
    #     n = len(sentence)
    #     if n == 0:
    #         return []
    #     words = []
    #     remainder  = sentence
    #     s = 0
    #     while len(remainder) > 0:
    #         s = 0
    #         for i in range(len(remainder), -1, -1):
    #             word = ''.join(remainder[0:i]) +'\n'
    #             if word in dictionary:
    #                 words.append(word.strip())
    #                 remainder = remainder[i:]
    #                 s = 1
    #                 break
    #         if s == 1:
    #             break
    #         a = 1
    #         m = 0
    #         for i in range(len(remainder)):
    #             if remainder[i][0].isupper():
    #                 m = 1
    #                 a = a+1
    #             else:
    #                 if m == 1:
    #                     a = a - 1
    #                 break
    #         word = ''.join(remainder[:a])
    #         remainder = remainder[a:]
    #         words.append(word)
    #     return words

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
                        wordtags.append(Word_tag(token, 'B'))
                        i += 1
                        continue
                
                # isSingleSyl = True
                for j in range (min(i + 4, senLength), i+1, -1):
                    word = ' '.join(lowTokens[i:j]).encode('utf-8')
                    if (word in self.dic):
                        wordtags.append(Word_tag(token,'B'))
                        for k in range(i+1,j,1):
                            wordtags.append(Word_tag(tokens[k],"I"))
                        i = j -1
                        # isSingleSyl =False
                        break
                # if (isSingleSyl):
                #     lowToken = lowTokens[i].encode('utf-8')
                #     if (lowToken in self.sent_w or token[0].islower() or token.isalpha()
                #         or lowToken in self.country_s):
                #         wordtags.append(Word_tag(token, 'B'))
                #         i += 1
                #         continue
                
                # ilower = i+1
                # for ilower in range(i+1, min(i+4, senLength)):
                #     nToken = tokens[ilower].encode('utf-8')
                #     if (nToken[0].islower() or not nToken.isalpha()
                #         or nToken == 'LBKT' or nToken == 'RBKT'):
                #         break
                
                # if (ilower > i + 1):
                #     notMiddleName = True
                #     if (lowToken in self.middle_n and i >= 1):
                #         prev = tokens[i - 1].encode('utf-8')
                #         if (prev[0].isupper()):
                #             wordtags.append(Word_tag(token, 'I'))
                #             notMiddleName = False
                #     if (notMiddleName):
                #         wordtags.append(Word_tag(token, 'B'))
                #     for k in range(i+1, ilower):
                #         wordtags.append(Word_tag(tokens[k], 'I'))

                #     i = ilower - 1
                
                # else: wordtags.append(Word_tag(token, 'B'))
            else: wordtags.append(Word_tag(token,'B'))
            i += 1
        return wordtags

    def main(self):
        # r = [u'Bắt', 'nghi', 'can', u'đâm', u'cụ', u'bà', u'để', u'cướp', u'tài', u'sản', u'Ngày', '9/10', ',', u'Công', u'an', u'huyện', u'Đông', 'Giang', '(', u'Quảng', u'Nam', ')', 'cho', u'biết', ',', u'đang', u'tạm', u'giữ', u'hình', u'sự', 'nghi', u'phạm', u'Nguyễn', u'Văn', u'Hải', '(', 'SN', '2002', ',', u'trú', u'xã', 'Ba', ',', u'huyện', u'Đông', u'Giang', ')', u'để', u'tiếp', u'tục', u'điều', 'tra', ',', u'làm', u'rõ', u'về', u'hành', 'vi', u'cướp', u'tài', u'sản', u'và', u'có', u'dấu', u'hiệu', u'phạm', u'tội', u'giết', u'người', '.']
        # s = 'Bắt nghi can đâm cụ bà để cướp tài sản Ngày 9/10 , Công an huyện Đông Giang ( Quảng Nam ) cho biết , đang tạm giữ hình sự nghi phạm Nguyễn Văn Hải ( SN 2002 , trú xã Ba , huyện Đông Giang ) để tiếp tục điều tra , làm rõ về hành vi cướp tài sản và có dấu hiệu phạm tội giết người .'
        # words = self.max_match(s,self.dictionary)
        # words = self.segment_words(s)
        # r = ['tài', 'sản']
        # r = ['Bắt', 'nghi', 'can', 'đâm', 'cụ', 'bà', 'để', 'cướp', 'tài', 'sản', 'Ngày', '9/10', ',', 'Công', 'an', 'huyện', 'Đông', 'Giang', '(', 'Quảng', 'Nam', ')', 'cho', 'biết', ',', 'đang', 'tạm', 'giữ', 'hình', 'sự', 'nghi', 'phạm', 'Nguyễn', 'Văn', 'Hải', '(', 'SN', '2002', ',', 'trú', 'xã', 'Ba', ',', 'huyện', 'Đông', 'Giang', ')', 'để', 'tiếp', 'tục', 'điều', 'tra', ',', 'làm', 'rõ', 'về', 'hành', 'vi', 'cướp', 'tài', 'sản', 'và', 'có', 'dấu', 'hiệu', 'phạm', 'tội', 'giết', 'người', '.', 'Theo', 'kết', 'quả', 'điều', 'tra', 'ban', 'đầu', ',', 'khoảng', '10h10', 'ngày', '7/10', ',', 'Công', 'an', 'huyện', 'Đông', 'Giang', 'nhận', 'được', 'tin', 'báo', 'về', 'vụ', 'cướp', 'tài', 'sản', '.', 'Nạn', 'nhân', 'là', 'bà', 'Nguyễn', 'Thị', 'Quy', '(', 'SN', '1936', ',', 'trú', 'thôn', 'Bốn', ',', 'xã', 'Ba', ',', 'huyện', 'Đông', 'Giang', ')', 'bị', 'kẻ', 'gian', 'vào', 'nhà', 'cướp', 'tiền', 'và', 'gây', 'thương', 'tích', 'tại', 'vùng', 'cổ', ',', 'lấy', 'đi', 'số', 'tiền', '830', '.', '000', 'đồng', '.', 'Nhận', 'thấy', 'đây', 'là', 'vụ', 'án', 'đặc', 'biệt', 'nghiêm', 'trọng', 'chưa', 'từng', 'xảy', 'ra', 'tại', 'địa', 'bàn', 'huyện', 'miền', 'núi', ',', 'lãnh', 'đạo', 'Công', 'an', 'huyện', 'Đông', 'Giang', 'đã', 'huy', 'động', 'tất', 'cả', 'các', 'lực', 'lượng', ',', 'phân', 'công', 'nhiều', 'tổ', 'trinh', 'sát', ',', 'nhanh', 'chóng', 'triển', 'khai', 'các', 'biện', 'pháp', 'nghiệp', 'vụ', ',', 'tiến', 'hành', 'rà', 'soát', ',', 'truy', 'xét', 'và', 'truy', 'tìm', 'đối', 'tượng', 'tại', 'địa', 'bàn', 'và', 'các', 'khu', 'vực', 'giáp', 'ranh', '.', 'Đến', '11h30', 'cùng', 'ngày', ',', 'Công', 'an', 'huyện', 'đã', 'phát', 'hiện', 'và', 'bắt', 'giữ', 'đối', 'tượng', 'Nguyễn', 'Văn', 'Hải', '.', 'Qua', 'đấu', 'tranh', 'ban', 'đầu', ',', 'đối', 'tượng', 'khai', 'nhận', 'do', 'nhiều', 'lần', 'nhìn', 'thấy', 'bà', 'Nguyễn', 'Thị', 'Quy', 'thường', 'hay', 'bỏ', 'tiền', 'trong', 'người', 'nên', 'sáng', 'ngày', '7/10', ',', 'Hải', 'chuẩn', 'bị', 'một', 'con', 'dao', 'mang', 'theo', 'trong', 'người', 'đến', 'nhà', 'nạn', 'nhân', 'để', 'thực', 'hiện', 'hành', 'vi', '.', 'Lợi', 'dụng', 'lúc', 'bà', 'Quy', 'ở', 'nhà', 'một', 'mình', ',', 'Hải', 'vào', 'nhà', 'giả', 'vờ', 'hỏi', 'thăm', '.', 'Thấy', 'trong', 'túi', 'áo', 'của', 'nạn', 'nhân', 'có', 'tiền', ',', 'đối', 'tượng', 'đã', 'đưa', 'tay', 'vào', 'túi', 'áo', 'để', 'lấy', ',', 'nạn', 'nhân', 'phát', 'hiện', ',', 'giằng', 'co', 'với', 'đối', 'tượng', 'và', 'ngã', 'ra', 'nền', 'nhà', ',', 'đối', 'tượng', 'sau', 'đó', 'đã', 'lấy', 'số', 'tiền', 'từ', 'trong', 'túi', 'áo', 'nạn', 'nhân', '.', 'Do', 'lo', 'sợ', 'nạn', 'nhân', 'biết', 'mặt', 'và', 'tố', 'giác', ',', 'Hải', 'đã', 'rút', 'con', 'dao', 'thủ', 'sẵn', 'trong', 'người', ',', 'đâm', 'vào', 'cổ', 'phía', 'bên', 'trái', 'của', 'nạn', 'nhân', 'và', 'bỏ', 'chạy', '.', 'Trên', 'đường', 'tẩu', 'thoát', ',', 'Hải', 'tẩu', 'tán', 'tang', 'vật', ',', 'xóa', 'mọi', 'dấu', 'vết', '.', 'Nạn', 'nhân', 'sau', 'khi', 'bị', 'Hải', 'đâm', 'đã', 'đến', 'ngất', 'xỉu', 'và', 'được', 'con', 'trai', 'bà', 'là', 'Hồ', 'Văn', 'Sơn', '(', 'SN', '1978', ',', 'trú', 'thôn', 'Bốn', ',', 'xã', 'Ba', ',', 'Đông', 'Giang', ')', 'về', 'nhà', 'phát', 'hiện', ',', 'đưa', 'đi', 'cấp', 'cứu', 'kịp', 'thời', '.', 'Hiện', 'vụ', 'việc', 'đang', 'được', 'Cơ', 'quan', 'CSĐT', 'Công', 'an', 'huyện', 'Đông', 'Giang', 'tích', 'cực', 'điều', 'tra', ',', 'làm', 'rõ', '.']
        f = open('test.txt', 'r')
        string = ''.join(f.readlines())
        syl = syllables.Syllables()
        result = syl.handle(string)
        # s = [x.decode('utf-8') for x in result]
        words = self.max_match(result)
        for i in words:
            print (i.word.strip() + '   ' + i.tag.strip())

if __name__ =='__main__':
    a = MaxMatchWordSegmenter()
    a.main()
