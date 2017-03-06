'''script opens files which I collected into a text file from the web.
Aim is to collect the name of the school and the attainment score'''

import pandas as pd
import os
from sklearn import preprocessing

schoolname = []
schoolscore = []
def collection (file):
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

files = []
path = 'C:\Users\student01\Desktop\MyEcho\Academia\GCSE\school ranking'
lst = [x[2] for x in os.walk(path)]
for l in lst:
    for file_name in l:
        files.append(file_name)

for file in files:
    collection('C:\Users\student01\Desktop\MyEcho\Academia\GCSE\school ranking\\' + file)



df = pd.DataFrame(
    {'SchoolName': schoolname,
    'SchoolScore': schoolscore})

school = df.SchoolScore #returns a numpy array

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(school)
school1 = pd.DataFrame(x_scaled)

df.drop('SchoolScore', inplace=True, axis=1)
result = pd.concat([df, school1], axis=1)

result.to_csv('schoolranking.csv', index=False)




