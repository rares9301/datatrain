from datatrain.core.config import WORKLOAD_DIR
import pandas as pd
import sys
import os

def remove_outliers(csv_path):
    # load dataset
    df = pd.read_csv(csv_path)

    # outlier fields
    numeric_columns = ['Age', 'SibSp', 'Fare']

    # IQR computing for fields
    for column in numeric_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # clear outlier for column
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    cleared_csv_path = os.path.join(WORKLOAD_DIR, 'cleared_train.csv')

    # export cleared fields
    df.to_csv(cleared_csv_path, index=False)
    print('Exported cleared csv to workload/cleared_train.csv')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python outliers.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    remove_outliers(csv_path)
