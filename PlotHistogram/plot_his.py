import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

class PlotHistogram():
    # Plot histogram 
        # df = pd.DataFrame.from_dict(self.histogram, orient='index')
        # df.plot(kind='bar')
        # plt.show()
    reload(sys)
    sys.setdefaultencoding('utf8')
    histogram = {}
    f = open('../MaximumMatching/histogram.txt')
        # histogram.append([next(myfile).replace('\n','') for x in xrange(20)])
    for x in xrange(100):
        (word, count) = next(f).split('   ')
        histogram[word] = int(count)
    f.close()
    df = pd.DataFrame.from_dict(histogram, orient='index')
    df.plot(kind='bar')
    plt.show()
    # print (histogram)
