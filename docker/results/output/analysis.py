import os
from pathlib import Path

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
