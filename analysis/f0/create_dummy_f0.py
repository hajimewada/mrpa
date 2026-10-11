import numpy as np

t = np.linspace(0, 1, 500)

accent = 0.3 * np.sin(40 * np.pi * t)

phrase = 1.0 * np.sin(8 * np.pi * t)

downstep = np.linspace(1.0, 0.3, 500)

f0 = accent + phrase + downstep

np.save("dummy_downstep_f0.npy", f0)

print("saved:", f0.shape)