#Analyses article-Devices.csv and answers questions:
#1. Percentage views from mobile devices.
#2. Times when views from mobile exceed its mean.

#import pandas as pd
import pandas as pd

#import numpy as np
import numpy as np

#read in the csv file of raw data to a dataframe df_raw:
df_raw = pd.read_csv('article-Devices.csv')

#sum total column to calculate divisor for percentage calculation: Total_views
Total_views = sum(df_raw['Total'])

#percentage mobile equals addition of sums of Mobile and Tablet columns over total views, round to 2 decimal places
Percentage_mobile = round((sum(df_raw['Mobile']) + sum(df_raw['Tablet']))/Total_views * 100, 2)

#Percentage mobile as type string
Percentage_mobile = str(Percentage_mobile)

#output the percentage calculation:
print('Percentage of total views from mobile devices: ' + Percentage_mobile +'%.')

#Output the result to a text file:
with open("Result_mobile_percentage.txt", 'w') as txt_file1:
    print('Percentage of total views from mobile devices: ' + Percentage_mobile +'%.', file=txt_file1)

#calculate mean page views from mobile:
mean_mobile = np.mean(df_raw['Mobile'])

#create a dataframe with rows where mobile figure is larger than its mean: df_results
df_results = df_raw.loc[df_raw['Mobile'] > mean_mobile]

#Output the Date column of results df to a text file:
with open("Result_times_above_mean.txt", 'w') as txt_file2:
    print(df_results['Date'].to_string(index=False, dtype=False), file=txt_file2)




