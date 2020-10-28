import jieba
import jieba.posseg as pseg
import numpy as np
import os, time, random
import sys
from tqdm import tqdm
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest,chi2
from collections import defaultdict
import numpy as np
import re
import math
rootdir =  './raw_data'
father = './'
cat_index = { 'mil':"10",
        "jinrong":"11",
         "gat":"12",
        'ty':"13",
        'wine':"14",
        'jk':"15",
        'world':"16",
        'society':"17",
        'life':"18",
        'car':"19",
        'it':"20",
        'house':"21",
        'energy':"22",
        'yl':"23"}
def getText(category, saveFile):
    rootpath = rootdir + '/' + category
    filelist = os.listdir(rootdir+'/'+category)
    with open(saveFile,'a+',encoding='utf-8',errors= 'ignore') as f:
        for i in range(len(filelist)):
            inpath = os.path.join(rootpath,filelist[i])
            if os.path.isfile(inpath):
                with open(inpath,'r',encoding="utf-8",errors= 'ignore') as infile:
                    content = infile.read()
                    paras_num = content.count('\n')
                    content = content.replace('\n', '')
                    content = content.replace('\r', '')
                    content = content.replace('\t', '')
                    content = content.replace(' ', '')
                    content = content.replace('　', '')
                    file_name = filelist[i].split('-')
                    f.write(category)
                    f.write('|_|' + str(int(file_name[1])) + cat_index[category])
                    f.write('|_|' + file_name[2][:-4])
                    f.write('|_|' + str(paras_num))
                    f.write('|_|' + content)
                    f.write("\n")