import argparse
import numpy as np
from scipy.interpolate import interp1d


def interpolate_f0(f0):

    voiced = np.where(f0 > 0)[0]

    if len(voiced) < 2:
        return f0

    interp_fn = interp1d(
        voiced,
        f0[voiced],
        bounds_error=False,
        fill_value=(
            f0[voiced[0]],
            f0[voiced[-1]],
        ),
    )

    return interp_fn(
        np.arange(len(f0))
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    f0 = np.load(args.input)

    f0_interp = interpolate_f0(f0)

    np.save(
        args.output,
        f0_interp,
    )

    print("saved:", args.output)


if __name__ == "__main__":
    main()