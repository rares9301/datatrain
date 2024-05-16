from datatrain.core.config import *
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='CLI for Assignment PCLP3.')
    parser.add_argument('--outliers', action='store_true', help='Activate the outliers clearing process.')
    parser.add_argument('--path', required=True, help='Path to the CSV file.')

    args = parser.parse_args()

    if args.outliers:
        subprocess.run(['python3', outliers_script_path, args.path])

if __name__ == '__main__':
    main()
