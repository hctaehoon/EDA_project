# 라이브러리를 불러옵니다.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib as mpl

# 글꼴 깨짐 방지
mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] =False

# 데이터 프레임 
df = pd.read_csv("/Users/b26/Desktop/미니프로젝트/패스트캠퍼스 데이터분석/실습데이터.csv")

#MeCab 사용
from konlpy.tag import Mecab
from PIL import Image
import nltk
import os
import re

# Word Cloud
from wordcloud import WordCloud

