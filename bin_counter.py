import csv

def sum_counts_from_csv(filename):
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            # Skip comment lines
            if line.startswith('#') or line.strip() == '':
                continue
            # Split by comma and sum the integers
            numbers = [int(x.strip()) for x in line.split(',') if x.strip().isdigit()]
            total += sum(numbers)
    return total
