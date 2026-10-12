import argparse
import numpy as np
import csv
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)

    args = parser.parse_args()

    data = np.load(args.input)

    coeffs = data["coeffs"]
    scales = data["scales"]
    freqs = data["freqs"]

    energy = np.mean(
        np.abs(coeffs),
        axis=1,
    )

    order = np.argsort(energy)[::-1]

    print("\nTop 10 Scales\n")

    for rank, idx in enumerate(order[:10], start=1):
        print(
            f"{rank:2d} | "
            f"Scale={scales[idx]:2d} | "
            f"Freq={freqs[idx]:.5f} | "
            f"Energy={energy[idx]:.6f}"
        )

    peak_idx = np.argmax(energy)

    peak_scale = int(scales[peak_idx])
    peak_freq = float(freqs[peak_idx])
    peak_energy = float(energy[peak_idx])

    print(
        f"\nPeak: "
        f"Scale={peak_scale} "
        f"Freq={peak_freq:.5f} "
        f"Energy={peak_energy:.6f}"
    )

    csv_path = "results/phrase_sweep_results.csv"

    file_exists = os.path.exists(csv_path)

    with open(
        csv_path,
        "a",
        newline="",
    ) as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(
                [
                    "input",
                    "peak_scale",
                    "peak_freq",
                    "peak_energy",
                ]
            )

        writer.writerow(
            [
                args.input,
                peak_scale,
                peak_freq,
                peak_energy,
            ]
        )

    print(
        f"saved csv: {csv_path}"
    )

if __name__ == "__main__":
    main()