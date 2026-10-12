import argparse
import numpy as np
import librosa
import pyworld as pw


def extract_f0(wav_path):

    wav, sr = librosa.load(
        wav_path,
        sr=None,
    )

    f0, t = pw.dio(
        wav.astype(np.float64),
        sr,
    )

    f0 = pw.stonemask(
        wav.astype(np.float64),
        f0,
        t,
        sr,
    )

    return f0


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
    )

    parser.add_argument(
        "--output",
        required=True,
    )

    args = parser.parse_args()

    f0 = extract_f0(args.input)

    np.save(
        args.output,
        f0,
    )

    print(
        "saved:",
        args.output,
    )

    print(
        "shape:",
        f0.shape,
    )


if __name__ == "__main__":
    main()