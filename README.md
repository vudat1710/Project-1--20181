# Project-1--20181
Project includes crawling data and word tokenization using Maximum Matching

# Problem Description

In this project, I have done the initial process of segmenting a text file into words with tags (B- standing for "Beginning of the word" and I- standing for "Inside the word"). This process includes 3 major steps. First of all, a crawling tool was implemented to crawl approximately 12,000 of articles from websites on the internet (In this project, I crawled 12,000 articles from 'https://dantri.com.vn/nhip-song-tre.htm'), then saved into 'data.txt'. Secondly, I implemented the word segmentation using the longest matching method with some modifications for the purpose of getting a better result. This step also includes the evaluation when compared the result achieved from this algorithm I have implemented with the test-BI file provided by my supervisor. The f1 score was 92.38%. This result was not quite outstanding according to the fact that the longest matching is the initial step in the process of word segmentation and the huge differences between the dictionaries used to generate 2 test files. In addition, due to the requirements of my supervisor, I built a histogram of most frequently used words in 12,000 articles crawled (this consists of only words, all of the punctuations are not counted) and plot it into a bar chart for visualization purpose.
[Edit]: With the new provided dictionary, the result increases significantly from 92.38% to 97.57%

# Requirements
Python 2 with scrapy, pandas, numpy, and matplotlib packages installed

# Compilation Steps
1) Crawling:
- cd to the CrawlData/dantri directory.
- In this directory run the script `scrapy crawl dantri_crawl`.
2) Maximum Matching:
- Compile and run the code in mm.py in MaximumMatching folder to generate 2 files including: 'output.txt' (The output of the algorithm implemented) and 'histogram.txt' (histogram file consists of words and the number of its appearances in 12,000 articles crawled).
- In this folder, run the code in f1_score.py to generate 'outputtestset.txt' (output generated from the test-BI file provided) and 'test.txt' (for the evaluation step mentioned above).
- In this directory, I have the script provided by my supervisor 'conlleval.pl' (written by Thai Hoang Pham - https://github.com/pth1993/NNVLP/blob/master/conlleval.pl). Run the script by typing `./conlleval.pl -l -d '\t' < test.txt`. The result will appear on your terminal.
3) Plotting
- Run plot_his.py in PlotHistogram folder to have visual aspect of the words frequency.  
