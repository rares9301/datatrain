from datatrain.core.config import *
from colorama import Fore, Style
import subprocess
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description=Fore.GREEN + Style.BRIGHT + 'CLI for Assignment PCLP3.' + Style.RESET_ALL,
                                     formatter_class=argparse.RawTextHelpFormatter)
    tasks = parser.add_argument_group(Fore.YELLOW + 'Tasks' + Style.RESET_ALL)
    misc = parser.add_argument_group(Fore.BLUE + 'Misc' + Style.RESET_ALL)

    tasks.add_argument('-ol', '--outliers', action='store_true',
                       help=Fore.CYAN + 'Activate the outliers clearing process.\nUsage: --outliers -c [columns] -path [path]' + Style.RESET_ALL)
    tasks.add_argument('-zs', '--zscore', action='store_true',
                       help=Fore.MAGENTA + 'Activate the Z-score clearing process.\nUsage: --zscore -c [columns + {threshold}] -path [path]' + Style.RESET_ALL)

    misc.add_argument('-p', '--path', required=True, help=Fore.RED + 'Path to the CSV file.' + Style.RESET_ALL)
    misc.add_argument('-c', '--columns', nargs='+', help=Fore.LIGHTBLACK_EX + 'Columns to be used for Z-score or outliers.' + Style.RESET_ALL)

    args = parser.parse_args()

    if args.outliers:
        if args.columns:
            subprocess.run(['python3', outliers_script_path, args.path] + args.columns)
        else:
            print(Fore.RED + Style.BRIGHT + "Please provide columns for the outliers process." + Style.RESET_ALL)
            sys.exit(1)

    if args.zscore:
        if args.columns:
            subprocess.run(['python3', zscore_script_path, args.path] + args.columns)
        else:
            print(Fore.RED + Style.BRIGHT + "Please provide columns for the Z-score process." + Style.RESET_ALL)
            sys.exit(1)

if __name__ == '__main__':
    main()
