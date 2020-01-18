import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rsf = pd.read_csv('output-data/RSF_data_rc01.csv')
skills = pd.read_csv('output-data/human-skill-codes.csv')
bands = pd.read_csv('output-data/year-bands.csv')
outputfolder = "graphics/human-skill-plots/"
