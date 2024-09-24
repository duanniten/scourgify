import sys
import csv


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 4:
    sys.exit('Too many commmand-line arguments')
elif len(sys.argv[1]) < 3:
    sys.exit('Not a CSV file')
elif sys.argv[1][-4:] != '.csv':
    sys.exit('Not a CSV file')
elif len(sys.argv[2]) < 3:
    sys.exit('Not a CSV file')
elif sys.argv[2][-4:] != '.csv':
    sys.exit('Not a CSV file')

try:
    with open(sys.argv[1]) as file:
        reader = 
except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
