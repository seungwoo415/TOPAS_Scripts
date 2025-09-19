from bin_counter import sum_counts_from_csv

filename = "de_surface.csv" 
num_runs = 100000
num_counts = sum_counts_from_csv(filename)

print(f"# of particles: {num_counts}") 
print(f"ratio: {num_counts/num_runs}")