
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

#function to pick ONLY years, role, orgtype, and also explode tag of interest
def prep_exploded(df,newtag,tagcol):
    rsf[newtag] = rsf[tagcol].str.split(",")
    df = rsf[['years_in_field', 'job_category_select', 'org-type_select', newtag]]
    df = df.dropna(subset=[newtag])

    rows_list = []
    for index, row in df.iterrows():
        for tag in row[newtag]:
            rows_list.append([row['years_in_field'], row['job_category_select'], row['org-type_select'], tag])
    newgoals =  pd.DataFrame(rows_list,columns=['years_in_field', 'job_category_select', 'org-type_select',newtag])
    #print newgoals.head()

# explode 4 tag categories of interest
goalsploded = prep_exploded(rsf,'goal','goal-desc_tags')
challsploded = prep_exploded(rsf,'challenge','biggest-challenge_tags')
excitesploded = prep_exploded(rsf,'excited','explore-excited_tags')
nextsploded = prep_exploded(rsf,'nextstep','one-next-step_tags')

#
# DO SOMETHING COOL HERE:
# - Filter by yearbands & get most common
# - Check for different trends from Roletype, Orgtype
#


#### Unmelted freq. counts
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
