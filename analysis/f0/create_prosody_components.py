import numpy as np

t = np.linspace(0, 1, 500)

# Pitch Accent
accent = 0.3 * np.sin(40 * np.pi * t)

# Accentual Phrase
phrase = 1.0 * np.sin(8 * np.pi * t)

# Downstep
downstep = np.linspace(
    1.0,
    0.3,
    500,
)

combined = accent + phrase + downstep

np.save("accent.npy", accent)
np.save("phrase.npy", phrase)
np.save("downstep.npy", downstep)
np.save("combined.npy", combined)

print("saved:")
print(" accent.npy")
print(" phrase.npy")
print(" downstep.npy")
print(" combined.npy")
