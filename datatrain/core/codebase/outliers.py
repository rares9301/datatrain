from datatrain.core.config import *
import pandas as pd
import sys
import os

def remove_outliers(csv_path, columns):
    # load dataset
    df = pd.read_csv(csv_path)

    # IQR computing for fields
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # clear outlier for column
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    # export cleared fields
    df.to_csv(task1path, index=False)
    print(f'Exported cleared csv to {task1path}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python outliers.py <path_to_csv> <columns>")
        sys.exit(1)

    csv_path = sys.argv[1]
    columns = sys.argv[2].split(',')
    remove_outliers(csv_path, columns)
