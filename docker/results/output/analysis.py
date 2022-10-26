import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# Load .env file from environment
OLD_PY = str(os.environ.get("OLD_PY_VERSION", "OLD"))
NEW_PY = str(os.environ.get("NEW_PY_VERSION", "NEW"))

# Load comparison.csv from /opt/output/ directory
df = pd.read_csv("/opt/output/comparison.csv")

# Analysis
df.rename(
    {"Base": OLD_PY, "Changed": NEW_PY, "Benchmark": "function"}, axis=1, inplace=True
)

df["speed_up"] = (df[OLD_PY] / df[NEW_PY]).round(3)
df.sort_values(by="speed_up", inplace=True)


# Plot Result
fig, ax = plt.subplots()

sns.histplot(df["speed_up"], bins=11)
ax.set(
    xlabel="Speedup (times)",
    title=f"Python {OLD_PY} vs. Python {NEW_PY} - speedup comparison",
)

# Save Outputs
plt.savefig("/opt/output/Compare.png", dpi=300)

df.to_csv("/opt/output/speed_up.csv", index=False)


# Details

fig, ax = plt.subplots(figsize=(13, 20))
labels = df.function
widths = df.speed_up

ax.grid(True)
ax.set_xlim(0.75, 2)


my_cmap = plt.get_cmap('seismic_r')
rescale = lambda y: y-0.5

rects = ax.barh(labels, widths, color=my_cmap(rescale(widths)), height=0.8, label="AA")

ax.bar_label(rects, label_type='edge')

ax.set(
    xlabel="Speedup (times)",
    title=f"Python {OLD_PY} vs. Python {NEW_PY} - speedup comparison in modules",
)
plt.margins(0.01, 0.01)

plt.rcParams['font.size'] = 16

fig.savefig("/opt/output/details.jpg", dpi=300, bbox_inches='tight')
fig.show()