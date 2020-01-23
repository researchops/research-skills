
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
    return newgoals


def band_values(band,data,tag):
    if band['name'] == 'all':
        slice = data
    else:
        slice = data.loc[(data['years_in_field'] >= band['min']) & (data['years_in_field'] <= band['max'])]
    print "\n\n" + tag + " @ " + band['name'] + " years in field:"
    print slice[tag].value_counts().nlargest(5)

# explode 4 tag categories of interest
goalsploded = prep_exploded(rsf,'goal','goal-desc_tags')
challsploded = prep_exploded(rsf,'challenge','biggest-challenge_tags')
excitesploded = prep_exploded(rsf,'excited','explore-excited_tags')
nextsploded = prep_exploded(rsf,'nextstep','one-next-step_tags')

#get values by band for each
for index, band in bands.iterrows():
    band_values(band, goalsploded, 'goal')
    band_values(band, challsploded, 'challenge')
    band_values(band, excitesploded, 'excited')
    band_values(band, nextsploded, 'nextstep')

print "\n\n In house challenges:"
print challsploded.loc[(challsploded['org-type_select'] == 'In-house private sector')]['challenge'].value_counts().nlargest(10)
print challsploded.loc[(challsploded['org-type_select'] == 'Agency')]['challenge'].value_counts().nlargest(10)
