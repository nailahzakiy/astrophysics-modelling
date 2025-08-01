import numpy as np
from astroquery.gaia import Gaia
import pandas as pd
import os

# Query: 5000 nearby stars with parallax > 10 (within ~100 parsec)
query = """
SELECT TOP 5000
    source_id, ra, dec, parallax, phot_g_mean_mag,
    bp_rp, phot_bp_mean_mag, phot_rp_mean_mag
FROM gaiadr3.gaia_source
WHERE parallax > 10 AND bp_rp IS NOT NULL
"""

print("Querying Gaia DR3...")
job = Gaia.launch_job(query)
data = job.get_results().to_pandas()

# Compute absolute magnitude
data["abs_mag_g"] = data["phot_g_mean_mag"] + 5 * (np.log10(data["parallax"] / 1000) + 1)

# Save to CSV
os.makedirs("data", exist_ok=True)
data.to_csv("data/gaia_hr_data.csv", index=False)
print("Data saved to data/gaia_hr_data.csv")
