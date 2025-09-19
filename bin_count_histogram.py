import matplotlib.pyplot as plt

def plot_histogram(filename, bin_width):
    # Read file and skip header lines
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if not line.startswith("#") and line.strip()]

    # The data is one long comma-separated row
    data = [float(x) for x in lines[0].split(",")]

    # Bin info from header
    n_bins = len(data)
    bin_edges = [i * bin_width for i in range(n_bins + 1)]
    bin_centers = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(n_bins)]

    # Plot histogram
    plt.bar(bin_centers, data, width=bin_width, align="center", color="skyblue", edgecolor="black")

    # Add red points for nonzero bins
    for x, y in zip(bin_centers, data):
        if y > 0:
            plt.plot(x, y, 'ro', markersize=2)  # red circle at the top of the bar

    
    plt.xlim(0, 0.1)
    plt.xlabel("Deposited Energy (MeV)")
    plt.ylabel("Counts")
    plt.title("Energy Deposition Histogram (TOPAS Output)")
    plt.show()


# Example usage
plot_histogram("primary.csv", 0.002)
