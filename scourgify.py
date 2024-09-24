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

students = []
try:
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            splitted_name = row['name'].split(sep=', ')
            first = splitted_name[1]
            last = splitted_name[0]
            students.append({
                'first': first,
                'last' : last,
                'house': row['house']
            })

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')

with open(sys.argv[2], 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    writer.writerows(students)