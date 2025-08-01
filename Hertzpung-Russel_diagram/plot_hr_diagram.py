import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Load data
df = pd.read_csv("C:/Users/ideap/Documents/astrophysics-modelling/astrophysics-modelling/Hertzpung-Russel_diagram/data/gaia_hr_data.csv")


# Filter out NaN values for safety
df = df.dropna(subset=["bp_rp", "phot_g_mean_mag"])

# Plotting if you want to use the original color index
# plt.figure(figsize=(8, 10))
# plt.scatter(df["bp_rp"], df["phot_g_mean_mag"], s=1, color="black")
# Use BP-RP as color source

# Prepare the plot
plt.figure(figsize=(8, 10))

#Plotting if you want to use the color index
scatter = plt.scatter(
    df["bp_rp"],
    df["phot_g_mean_mag"],
    c=df["bp_rp"],         # color by BP-RP index
    cmap="coolwarm",       # blue (hot) to red (cool)
    vmin=-1, vmax=5,  # set limits for color scale
    s=3,
    alpha=1,
    edgecolor="none"
)
# Enlarge axis ranges
plt.xlim(-1, 5)  
plt.ylim(0, 25)   

#invert y-axis to have brighter stars at the top
plt.gca().invert_yaxis()   


plt.xlabel("BP - RP (Color Index)")
plt.ylabel("G-band Mean Magnitude")
plt.title("Hertzsprung-Russell Diagram from Gaia DR3")
plt.grid(True)

# Add grid, legend, and layout
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
