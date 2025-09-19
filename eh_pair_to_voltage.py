import csv
from bin_counter import sum_counts_from_csv

sum_count = False 

def average_energy_from_csv(filename, bin_width, num_bins):
    total_counts = 0
    total_energy = 0.0
    
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#') or line.strip() == '':
                continue
            counts = [int(x.strip()) for x in line.split(',') if x.strip().isdigit()]
            
            # Only take the main bins (skip first underflow bin and last overflow/no-incident bins)
            main_counts = counts[1:1+num_bins]
            for i, count in enumerate(main_counts):
                bin_energy = i * bin_width + bin_width/2  # bin center
                total_energy += count * bin_energy
                total_counts += count

    if total_counts == 0:
        return 0.0
    return (total_energy / total_counts) * 1e6

def average_energy_per_depositing_photon(csv_file):

    sums = []
    counts = []

    with open(csv_file, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comment lines and empty lines
            if line.startswith("#") or line == "":
                continue
            
            # Split the line by commas
            parts = line.split(',')
            
            # Process alternating Sum, Count_in_Bin
            for i in range(0, len(parts)-1, 2):
                try:
                    s = float(parts[i])
                    c = int(parts[i+1])
                    sums.append(s)
                    counts.append(c)
                except ValueError:
                    continue  # skip non-numeric entries

    # Compute overall average per depositing photon
    total_sum = sum(sums)
    total_counts = sum(counts)
    overall_avg = total_sum / total_counts if total_counts != 0 else 0

    return overall_avg * 1e6

# file names 
primary_file = 'gamma_eh_pair.csv'
#secondary_file = 'secondary.csv' 
bin_width = 0.002 
num_bins = 100 
c_fd = 5e-15
    
if sum_count == False: 
    #primary_total = sum_counts_from_csv(primary_file)
    #secondary_total = sum_counts_from_csv(secondary_file)
    avg_E_dep = average_energy_from_csv(primary_file, bin_width, num_bins)
else: 
    avg_E_dep = average_energy_per_depositing_photon(primary_file)

avg_eh_pairs = avg_E_dep / (3 * 1.12) # quenching factor and bandgap energy of silicon
voltage = (avg_eh_pairs * 1.602176634e-19) / c_fd
#print(f"Total Primary: {primary_total}")
#print(f"Total Secondary: {secondary_total}")
#print(f"Secondary / Primary ratio: {avg_sec_per_primary}")
print(f"E_dep per primary: {avg_E_dep}")
print(f"Average # of e/h pair: {avg_eh_pairs}")
print(f"Voltage Drop for {c_fd} F: {voltage}")
    
