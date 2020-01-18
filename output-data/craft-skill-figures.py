import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rsf = pd.read_csv('output-data/RSF_data_rc01.csv')
skills = pd.read_csv('output-data/craft-skill-codes.csv')
bands = pd.read_csv('output-data/year-bands.csv')
outputfolder = "graphics/craft-skill-plots/"

#proportion of people who indicated a given skill IMPORTANT...
#within a given band of experience
def most_important_prop(band,skill,data):
    slice = data.loc[(data['years_in_field'] >= band['min']) & (data['years_in_field'] <= band['max'])]
    count = slice[['craft-important_1','craft-important_2','craft-important_3']].eq(skill['code']).sum().sum()
    prop = 1. * count / len(slice.index)  # divide by # of people in this band-slice
    return(prop)

#proportion of people who indicated a given skill DESIRED...
#within a given band of experience
def most_desired_prop(band,skill,data):
    slice = data.loc[(data['years_in_field'] >= band['min']) & (data['years_in_field'] <= band['max'])]
    count = slice[['craft-desired_1','craft-desired_2','craft-desired_3']].eq(skill['code']).sum().sum()
    prop = 1. * count / len(slice.index)  # divide by # of people in this band-slice
    return(prop)

# SKILL LOOP
# Iterate through all skills
for index, skill in skills.iterrows():

    rows_list = []

    # EXPERIENCE BAND LOOP
    # Get observations for this skill, by band level as rows, dump into dataframe (skillframe)
    for index, band in bands.iterrows():
        rows_list.append([band['name'],most_important_prop(band, skill, rsf), "important now"])
        rows_list.append([band['name'],most_desired_prop(band, skill, rsf), "desired skill"])

    skillframe = pd.DataFrame(rows_list,columns=['experience', 'proportion-responding', 'category'])

    # Plot skillframe and save as graphical output
    sns.set(style="whitegrid", palette="muted")
    g = sns.catplot(x="experience", y="proportion-responding", hue="category", data=skillframe,
                        height=6, kind="bar", legend=True)
    g.set_ylabels("% respondents indicating skill as...")
    g.set_xlabels("Years experience in field")
    plt.ylim(0,.5)
    plt.title("Skill: " + skill['skill'].capitalize())
    print("generating Skill: " + skill['skill'].capitalize() + "image")
    #plt.show()

    #Title with skillname-cleaned up
    plt.savefig(outputfolder + skill['skill'].replace(" ", "_").replace("/","-")+".png")
    plt.close()
