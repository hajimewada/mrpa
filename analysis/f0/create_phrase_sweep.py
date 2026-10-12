import numpy as np

t = np.linspace(0, 1, 500)

configs = {
    "phrase_08": 8,
    "phrase_16": 16,
    "phrase_24": 24,
    "phrase_32": 32,
}

for name, freq in configs.items():

    phrase = np.sin(freq * np.pi * t)

    np.save(
        f"{name}.npy",
        phrase,
    )

    print(
        f"saved: {name}.npy"
    )