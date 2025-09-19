from bin_counter import sum_counts_from_csv 

num_incident = sum_counts_from_csv("de_surface.csv")
num_interacted = sum_counts_from_csv("de_primary.csv") 

print(f"Detector Eficiency: {num_interacted/num_incident}")