import argparse
import numpy as np
import librosa


def extract_f0(wav_path):

    wav, sr = librosa.load(
        wav_path,
        sr=None,
    )

    f0, voiced_flag, voiced_prob = librosa.pyin(
        wav,
        fmin=librosa.note_to_hz("C2"),
        fmax=librosa.note_to_hz("C7"),
    )

    f0 = np.nan_to_num(f0)

    return f0


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    f0 = extract_f0(args.input)

    np.save(args.output, f0)

    print("saved:", args.output)
    print("shape:", f0.shape)

    voiced = f0[f0 > 0]

    print("voiced frames:", len(voiced))

    if len(voiced):
        print("min f0 :", voiced.min())
        print("max f0 :", voiced.max())
        print("mean f0:", voiced.mean())


if __name__ == "__main__":
    main()