import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
args = parser.parse_args()

f0 = np.load(args.input)

plt.figure(figsize=(12,4))
plt.plot(f0)

plt.title("F0 Contour")
plt.xlabel("Frame")
plt.ylabel("F0 (Hz)")

outfile = (
    args.input
    .replace(".npy", "_plot.png")
)

plt.savefig(
    outfile,
    dpi=200,
    bbox_inches="tight"
)

print("saved:", outfile)