# extract continuous wavelet transform (CWT) coefficients
# from a given F0 sequence

import argparse
import numpy as np
import pywt


def compute_cwt(
    f0,
    scales=None,
    wavelet="morl",
):
    if scales is None:
        scales = np.arange(1, 65)

    coeffs, freqs = pywt.cwt(
        f0,
        scales,
        wavelet,
    )

    return coeffs, freqs, scales


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
        help="input F0 .npy file",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="output .npz file",
    )

    parser.add_argument(
        "--wavelet",
        default="morl",
    )

    args = parser.parse_args()

    f0 = np.load(args.input)

    coeffs, freqs, scales = compute_cwt(
        f0,
        wavelet=args.wavelet,
    )

    np.savez(
        args.output,
        coeffs=coeffs,
        freqs=freqs,
        scales=scales,
        wavelet=args.wavelet,
    )

    print("input shape :", f0.shape)
    print("cwt shape   :", coeffs.shape)
    print("saved       :", args.output)


if __name__ == "__main__":
    main()