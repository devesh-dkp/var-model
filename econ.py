import matplotlib.pyplot as plt
import pandas as pd

# Function to plot data with dual y-axis
def plot_data_dual_axis(dates, prices1, title1, color1, prices2, title2, color2):
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Primary y-axis for gold prices
    ax1.plot(dates, prices1, label=title1, color=color1)
    ax1.set_xlabel('Time (YYYY-MM)')
    ax1.set_ylabel('Gold Price (in USD)', color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)

    # Secondary y-axis for oil prices (twinned)
    ax2 = ax1.twinx()
    ax2.plot(dates, prices2, label=title2, color=color2)
    ax2.set_ylabel('Oil Price (in USD)', color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)

    # Add legends for both datasets
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

    plt.title(f"{title1} & {title2} Over Time")
    plt.tight_layout()
    plt.show()

# URL for the CSV file
url = 'https://raw.githubusercontent.com/deveshkpandey/Var_financialanalytics/main/full.csv'

# Read data using pandas with correct date format
data = pd.read_csv(url, parse_dates=['date'], dayfirst=True)

# Plot gold and oil prices on the same graph
plot_data_dual_axis(data['date'], data['gold'], 'Gold Prices (per troy ounce)', 'red', data['oil'], 'Oil Prices (per barrel)', 'black')
