import numpy as np
import pywt


def reconstruct_signal(coeffs):
    reconstruction = coeffs.sum(axis=0)

    return reconstruction


def main():
    coeffs = np.load("cwt.npy")

    recon = reconstruct_signal(coeffs)

    np.save("reconstructed.npy", recon)

    print(recon.shape)


if __name__ == "__main__":
    main()