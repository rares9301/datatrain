from datatrain.core.config import *
from colorama import Fore, Style
import subprocess
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description=Fore.GREEN + Style.BRIGHT + 'CLI for Assignment PCLP3.\n' + Style.RESET_ALL + '\n' +
                    Fore.MAGENTA + Style.DIM + '-' * 61 + '\n' + Style.RESET_ALL +
                    Fore.BLUE + Style.BRIGHT + 'Copyright (C) 2024 Rareș-Andrei Sărmășag\n' + Style.RESET_ALL  +
                    Fore.MAGENTA + Style.DIM +
                    'This program comes with ABSOLUTELY NO WARRANTY\n' +
                    'This is free software, and you are welcome to redistribute it\n' +
                    'under certain conditions' + '\n' + '-' * 61 + Style.RESET_ALL,
        formatter_class=argparse.RawTextHelpFormatter
    )
    tasks = parser.add_argument_group(Fore.YELLOW + 'Tasks' + Style.RESET_ALL)
    misc = parser.add_argument_group(Fore.BLUE + 'Misc' + Style.RESET_ALL)

    tasks.add_argument('-ol', '--outliers', action='store_true',
                       help=Fore.CYAN + 'Activate the outliers clearing process.\nUsage: --outliers -c [columns] -path [path]' + Style.RESET_ALL)
    tasks.add_argument('-zs', '--zscore', action='store_true',
                       help=Fore.MAGENTA + 'Activate the Z-score clearing process.\nUsage: --zscore -c [columns + {threshold}] -path [path]' + Style.RESET_ALL)

    misc.add_argument('-p', '--path', required=True, help=Fore.RED + 'Path to the CSV file.' + Style.RESET_ALL)
    misc.add_argument('-c', '--columns', nargs='+', help=Fore.RED + 'Columns to be used for Z-score or outliers\n' + Style.RESET_ALL + Fore.LIGHTBLACK_EX + '(might also include threshold for z-score)' + Style.RESET_ALL)

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
