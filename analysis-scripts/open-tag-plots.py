
# Needs all the data from this google sheet, exported to CSVs:
# https://docs.google.com/spreadsheets/d/1IgbQiHOBhKZNEaTAXMJY16ZDwbE8NQmgZbX07fmMY6I/edit?usp=sharing

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from itertools import chain
from collections import Counter

rsf = pd.read_csv('input-data/RSF_data.csv')
bands = pd.read_csv('input-data/year-bands.csv')
gfxfolder = "graphics/open-tag-plots/"

#explode tags from string to Lis
rsf['goal'] = rsf['goal-desc_tags'].str.split(",")
rsf['challenge'] = rsf['biggest-challenge_tags'].str.split(",")
rsf['excited'] = rsf['explore-excited_tags'].str.split(",")
rsf['nextstep'] = rsf['one-next-step_tags'].str.split(",")
#rsf['nextstep'].replace('', np.nan, inplace=True)

goaldata = rsf.dropna(subset=['goal'])
goals = Counter(chain.from_iterable(x for x in goaldata.goal))
print("\nGoal tags, most common:")
print(goals.most_common())

chaldata = rsf.dropna(subset=['challenge'])
challenges = Counter(chain.from_iterable(x for x in chaldata['challenge']))
print("\nChallenge tags, most common:")
print(challenges.most_common())

excdata = rsf.dropna(subset=['excited'])
excitements = Counter(chain.from_iterable(x for x in excdata.excited))
print("\nExcited tags, most common:")
print(excitements.most_common())

nextdata = rsf.dropna(subset=['nextstep'])
nextsteps = Counter(chain.from_iterable(x for x in nextdata.nextstep))
print("\nNext step tags, most common:")
print(nextsteps.most_common())



#very annoying: take a column that contains lists and get unique elements
#def all_tags_from_col(col):
#    list = []
#    alltags = [item for item in col]
#    for taglist in alltags:
#        for tag in taglist:
#            list.append(tag)
#    return list

#goal_tags = all_tags_from_col(goaldata['goal'])
#print goal_tags
