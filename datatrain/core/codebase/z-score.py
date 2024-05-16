from datatrain.core.config import *
import pandas as pd
import numpy as np
import sys

def zscore(csv_path, columns, zscore_threshold=3):
    # load dataset
    df = pd.read_csv(csv_path)

    # compute z-score for each column and clear values with z-score > threshold
    for column in columns:
        mean = df[column].mean()
        std = df[column].std()
        z_score_column = column + '_Z_Score'
        df[z_score_column] = (df[column] - mean) / std
        df = df[df[z_score_column].abs() <= zscore_threshold]
        df = df.drop(columns=[z_score_column])

    # export cleared fields
    df.to_csv(task2path, index=False)
    print(f'Exported cleared csv to {task2path}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python z_score.py <path_to_csv> <columns> [z_score_threshold]")
        sys.exit(1)

    csv_path = sys.argv[1]
    columns = sys.argv[2].split(',')
    zscore_threshold = float(sys.argv[3]) if len(sys.argv) > 3 else 3
    zscore(csv_path, columns, zscore_threshold)
