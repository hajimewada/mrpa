#!/bin/bash

for f in 08 16 24 32
do
    python analysis/f0/extract_cwt.py \
        --input phrase_${f}.npy \
        --output phrase_${f}_cwt.npz

    python analysis/f0/scale_energy.py \
        --input phrase_${f}_cwt.npz
done