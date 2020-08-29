import pandas as pd;

#step 1 = read data from csv file 
csv_file = 'MarvellousInfosystems_PlayPredictor.csv';
batches = pd.read_csv(csv_file);

print(batches.head());

