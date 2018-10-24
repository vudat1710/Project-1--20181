# -*- coding: utf-8 -*-
import re
import sys
import unicodedata
import constants
import mm

class Syllables():
    def __init__(self):
        pass
    
    # def isBrace(self, string):
    #     if (string == "”" or string == "'" or string == ")" or 
    #             string == "}" or string == "]"):
    #         return True
    #     return False
    
    # def joinSentence(self, tokens):
    #     aList = []
    #     for i in range(len(tokens)):
    #         token = tokens[i]
    #         if (len(token) == 0 or token == None or token == constants.SPACE):
    #             continue
    #         aList.append(token)
    #         if (i < len(tokens) - 1):
    #             aList.append(constants.SPACE)
    #     out_str = ''.join(aList)
    #     return out_str.strip()

    # def joinSentences(self, tokens):
    #     sentences = []
    #     sentence = []
    #     for i in range(len(tokens)):
    #         token = tokens[i]
    #         if (i != len(tokens) - 1):
    #             nextToken = tokens[i+1]
    #         if (i > 0):
    #             prevToken = tokens[i-1]

    #         sentence.append(token)

    #         if (i == len(tokens) - 1):
    #             sentences.append(self.joinSentence(sentence))
    #             return sentences
            
    #         if (i < len(tokens) - 2 and token == constants.COLON):
    #             if (nextToken[0].isdigit() and tokens[i+2] == constants.END_SEN):
    #                 sentences.append(self.joinSentence(sentence))
    #                 sentence = []
    #                 continue
            
    #         pattern = re.compile(constants.EOS_PUNCTUATION)
    #         if (pattern.match(token)):
    #             if (nextToken == "\"" or nextToken == "''"):
    #                 count = 0
    #                 for sToken in sentence:
    #                     if (sToken == "\"" or sToken == "''"):
    #                         count += 1
    #                     if count % 2 == 1:
    #                         continue
                
    #             if (self.isBrace(nextToken) or len(nextToken) == 0
    #                 or nextToken[0].islower() or nextToken == constants.COMMA or nextToken[0].isdigit()):
    #                 continue
                
    #             if (len(sentence) == 2 and token == constants.END_SEN):
    #                 if (prevToken[0].isdigit()):
    #                     continue
    #                 if (prevToken[0].islower()):
    #                     continue
    #                 if (prevToken[0].isupper()):
    #                     if (len(prevToken) == 1):
    #                         continue
                
    #             sentences.append(self.joinSentence(sentence))
    #             sentence = []
    #     return sentences

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

    def main(self):
        f = open('test.txt', 'r')
        string = ''.join(f.readlines())
        result = self.handle(string)
        # s = self.joinSentences(result)
        print (result)
        

if __name__ =='__main__':
    a = Syllables()
    a.main()
