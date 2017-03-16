'''script loops through the files in the folder 'school_ranking_raw_data' and collects the school name and school score'''

import pandas as pd
import os
from sklearn import preprocessing

schoolname = []
schoolscore = []


def collection (file):
    '''Function is run on individual files and collects the schoolname and attainment score and appends it to the two lists above'''
    with open(file, 'r') as fhand:
        for line in fhand:
            if not line.startswith('Type'):
                    if not line.startswith('Well'):
                        if not line.startswith('('):
                            if not line.startswith('Add'):
                                if not line.startswith('Open'):
                                    if not line.startswith('Number'):
                                        if not line.startswith('Above'):
                                            if not line.startswith('Grade'):
                                                if not line.startswith('Progress'):
                                                    if not line.startswith('School'):
                                                        if not line.startswith('Attainment'):
                                                            if not line.startswith('Entering'):
                                                                if not line.startswith('Overall'):
                                                                    if not line.startswith('Staying'):
                                                                        if not line.startswith('Achieving'):
                                                                            if not line.startswith('Average'):
                                                                                if not line.startswith('Below'):
                                                                                    schoolname.append(line.strip('\n'))
            if line.startswith('('):
                if 'score' in line:
                    line = line.strip('\n')  # remove empty lines
                    line = line.split()
                    schoolscore.append(line[6])

# This block loops there the files in the school_ranking_raw_data and collects the names of the files
files = []
path = 'C:\Users\student01\Desktop\MyEcho\Academia\GCSE\school_ranking_raw_data'
lst = [x[2] for x in os.walk(path)]
for l in lst:
    for file_name in l:
        files.append(file_name)
# This block loops through the files and runs the above function
for file in files:
    collection('C:\Users\student01\Desktop\MyEcho\Academia\GCSE\school_ranking_raw_data\\' + file)


# Create a dataframe of the two lists, normalise the attainment score and save the df as csv file.
df = pd.DataFrame(
    {'SchoolName': schoolname,
    'SchoolScore': schoolscore})

school = df.SchoolScore #returns a numpy array

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(school)
school1 = pd.DataFrame(x_scaled)

df.drop('SchoolScore', inplace=True, axis=1)
result = pd.concat([df, school1], axis=1)

result.to_csv('schoolranking.csv', index=False) # note this file is then moved into school_ranking_clean_data




