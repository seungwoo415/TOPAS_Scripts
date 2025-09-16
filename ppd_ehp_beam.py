import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

phsp_file = "ppd_ehp_beam.phsp" 

# load phsp file 
df = pd.read_csv(phsp_file, delim_whitespace=True, header=None, dtype=str)

# Convert numeric columns to float/int
energies = df[5].astype(float)  # Energy column (MeV)
event_ids = df[13].astype(int)  # Event ID column

# Sum energy per event
unique_events = np.unique(event_ids)
energy_per_event = []
for evt in unique_events:
    mask = event_ids == evt
    energy_per_event.append(np.sum(energies[mask])) 
energy_per_event = np.array(energy_per_event)

# plot 
plt.figure(figsize=(8,6))
plt.hist(energy_per_event*1e3, bins=50, edgecolor='black')  # convert MeV -> keV
plt.xlabel("Energy Deposited per Gamma [keV]")
plt.ylabel("Number of Occurences")
plt.title("Energy Deposition in Photodiode")
plt.grid(True)
plt.show()
