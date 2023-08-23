import os
import sys
import pandas as pd
from tqdm import tqdm

file_name = sys.argv[1]
steps = int(sys.argv[2]) - 1

os.mkdir('data')
df = pd.read_csv(file_name)

step = len(df)//steps
end = len(df)

for i in tqdm(range(0,end-step,step)):
    df.iloc[i: i + step].to_csv( 'data/' + str(i) + '.csv'  , index = False)
    
df.iloc[i+step : len(df)].to_csv('data/' + str(len(df)) + '.csv', index = False)