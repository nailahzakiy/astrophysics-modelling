import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Load data
df = pd.read_csv('C:/Users/ideap/Documents/astrophysics-modelling/Gaia_DR3_5853498713190525696/XP_SAMPLED-Gaia DR3 5853498713190525696.csv')

# Fungsi untuk konversi wavelength ke RGB (kasar untuk spektrum tampak)
def wavelength_to_rgb(wavelength):
    gamma = 0.8
    intensity_max = 255
    factor = 0.0
    R = G = B = 0.0

    if 380 <= wavelength <= 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 <= wavelength <= 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 <= wavelength <= 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength <= 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength <= 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= wavelength <= 780:
        R = 1.0
        G = 0.0
        B = 0.0

    # Intensitas
    if 380 <= wavelength <= 420:
        factor = 0.3 + 0.7*(wavelength - 380) / (420 - 380)
    elif 420 <= wavelength <= 700:
        factor = 1.0
    elif 700 <= wavelength <= 780:
        factor = 0.3 + 0.7*(780 - wavelength) / (780 - 700)

    R = round(intensity_max * (R * factor) ** gamma)
    G = round(intensity_max * (G * factor) ** gamma)
    B = round(intensity_max * (B * factor) ** gamma)

    return (R/255, G/255, B/255)

# Buat plot
plt.figure(figsize=(12, 5))
for i in range(len(df) - 1):
    wl1 = df['wavelength'].iloc[i]
    wl2 = df['wavelength'].iloc[i+1]
    flux1 = df['flux'].iloc[i]
    flux2 = df['flux'].iloc[i+1]
    color = wavelength_to_rgb((wl1 + wl2) / 2)
    plt.plot([wl1, wl2], [flux1, flux2], color=color)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Flux')
plt.title('Spectral Plot with Visible Colors')
plt.grid(True)
plt.tight_layout()
plt.show()
