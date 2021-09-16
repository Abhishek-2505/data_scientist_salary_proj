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
df['Company'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3] , axis=1)


# job state parse & location and hq same?
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df['is_hq?'] = df.apply(lambda x: 1 if x['Location']==x['Headquarters'] else 0, axis=1)


# age of company
from datetime import date
cur_date = date.today()
df['company_age'] = df['Founded'].apply(lambda x: cur_date.year-x if x>0 else x)


# job description parse (imp keywords like python etc)
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python'].value_counts()

df['r_studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['r_studio'].value_counts()

df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['tableau'].value_counts()

df['power_bi'] = df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() else 0)
df['power_bi'].value_counts()

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel'].value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark'].value_counts()

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws'].value_counts()

df.to_csv('salary_data_cleaned.csv', index = False)
