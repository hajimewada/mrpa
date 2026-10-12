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
    selected = [
        0,   # scale 1
        1,   # scale 2
        3,   # scale 4
        7,   # scale 8
        15,  # scale 16
        31,  # scale 32
        47,  # scale 48
        63,  # scale 64
    ]

    print("coeffs:", coeffs.shape)
    print("freqs :", freqs.shape)
    print("scales:", scales.shape)

    n_scales = len(selected)

    fig, axes = plt.subplots(
        n_scales,
        1,
        figsize=(12, 2 * n_scales),
        sharex=True,
    )

    for j, i in enumerate(selected):

        axes[j].plot(coeffs[i])

        axes[j].set_title(
            f"Scale={scales[i]} | "
            f"Freq={freqs[i]:.4f}"
        )
        # f"Scale={scales[i]}  Freq={freqs.4f}"
        
    output_png = (
        args.input
        .replace(".npz", "")
        + "_scales.png"
    )

    plt.tight_layout()

    plt.savefig(
        output_png,
        dpi=200,
        bbox_inches="tight",
    )

    print("first 8 scales")
    print(scales[:8])

    print("first 8 freqs")
    print(freqs[:8])

    print(f"saved: {output_png}")


if __name__ == "__main__":
    main()