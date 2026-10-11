MRPA Architecture
Baseline: FastSpeech2

Preprocessing:

wav -> pitch.npy (PyWorld)

MRPA Extension:

pitch.npy -> CWT(F0) -> cwt.npy

Model:

Encoder -> CWT Predictor -> inverse CWT -> F0 -> Pitch Embedding -> Decoder

Analysis:

CWT Scale -> Pitch Accent -> Accentual Phrase -> Downstep