import argparse
import numpy as np
import matplotlib.pyplot as plt


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

    plt.figure(figsize=(10, 5))

    plt.plot(
        scales,
        energy,
        marker="o",
    )

    plt.xlabel("Scale")
    plt.ylabel("Mean Absolute Energy")
    plt.title("Scale Energy Spectrum")

    plt.grid(True)

    output_png = (
        args.input.replace(".npz", "")
        + "_energy.png"
    )

    plt.savefig(
        output_png,
        dpi=200,
        bbox_inches="tight",
    )

    print(f"saved: {output_png}")


if __name__ == "__main__":
    main()