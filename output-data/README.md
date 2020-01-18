## Code for generating plots
Python code to generate plots based on output data from RSF Workshops 2019. All data in google sheet here: https://docs.google.com/spreadsheets/d/1IgbQiHOBhKZNEaTAXMJY16ZDwbE8NQmgZbX07fmMY6I/edit?usp=sharing, and CSV's in this folder.

Output plots are in ../output-graphics.

#### Script stuff
There're two scripts in here:

__craft-skill-figures.py__
Loads skills from craft-skill-codes.csv, loads bands of skills from year-bands.csv, and then builds a plot for each skill: proportion of respondents who chose a skill as 'currently important', and proportion who chose the skill as 'desired for growth'. It's actually kind of interesting already.

__human-skill-figures.py__
Loads skills from human-skill-codes.csv, loads bands of skills from year-bands.csv, and then builds a plot for each skill: avg rating across each skill band bucket. It's not super interesting at this fidelity.


_Notes to self on python setup / code_
- Install Anaconda
- Install Seaborn: 'conda install -c anaconda seaborn'
- I'm using Atom with the project as the folder one level higher than this one
- It's all really janky; if I knew how to slice and dice dataframes right I could probably get rid of a lot of looping, and make it easier to filter by arbitrary categories (e.g., organization type)... more expedient to do it this way now, and get elegant if we plan to revisit

