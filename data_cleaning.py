# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:07:29 2021

@author: Abhishek
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parse
df = df[df['Salary Estimate']!='-1']

df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

salClean1 = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salClean2 = salClean1.apply(lambda x: x.split(':')[1] if 'employer provided salary:' in x.lower() else x)
salClean3 =salClean2.apply(lambda x: x.split('Per')[0].replace('K','').replace('$','') if 'per hour' in x.lower() else x.replace('K','').replace('$',''))

df['min_sal($)'] = salClean3.apply(lambda x: int(x.split('-')[0]) * 1000)
df['max_sal($)'] = salClean3.apply(lambda x: int(x.split('-')[1]) * 1000)
df['avg_sal($)'] = ( df['min_sal($)'] + df['max_sal($)']) /2


# company name

# job state parse & location and hq same?

# age of company

# job description parse (imp keywords like python etc)

