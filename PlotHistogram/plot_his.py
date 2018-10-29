import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import sys

class PlotHistogram():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    histogram = {}
    f = open('../MaximumMatching/histogram.txt')
    for x in range(100):
        (word, count) = next(f).split('   ')
        histogram[word] = int(count)
    f.close()
    df = pd.DataFrame.from_dict(histogram, orient='index')
    df.plot(kind='bar')
    plt.show()
