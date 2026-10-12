MRPA-1 Findings
F0 Extraction
Python
pitch, t = pw.dio(...)
pitch = pw.stonemask(...)
So:
Plain Text
wav
↓
DIO
↓
StoneMask
↓
frame-level F0
________________________________________
Interpolation
Before phoneme averaging:
Python
interp_fn(...)
pitch = interp_fn(...)
Unvoiced gaps are filled by interpolation.
Therefore the signal becomes approximately continuous.
That is actually good for CWT.
________________________________________
Phoneme-Level Conversion
Then:
Python
pitch[i] = np.mean(
pitch[pos : pos + d]
)
So the model is NOT necessarily trained on frame-level F0.
It can become:
Plain Text
frame F0
↓
duration alignment
↓
phoneme F0
↓
pitch.npy
depending on configuration.
________________________________________
Saved Artifact
Python
speaker-pitch-basename.npy
contains:
Plain Text
pitch
after preprocessing.
________________________________________
Why This Matters for MRPA
This answers our first architectural question.
Our future pipeline should probably be:
Plain Text
wav
↓
DIO
↓
StoneMask
↓
pitch.npy
↓
CWT(F0)
↓
cwt.npy
NOT
Plain Text
waveform
↓
CWT
The FastSpeech2-CWT repository appears to operate on waveform-derived wavelet features, whereas MRPA's theoretical foundation is explicitly based on prosodic F0 structure.
________________________________________

config/LJSpeech/preprocess.yaml

pitch:
    feature: phoneme_level

energy:
    feature: phoneme_level


config/LJSpeech_paper/preprocess.yaml

pitch:
    feature: frame_level


Finding #003
FastSpeech2 は両方をサポートしている。
Plain Text
phoneme_level F0
と
Plain Text
frame_level F0
です。
________________________________________
MRPAとしてどちらを使うか？
私の意見はかなり明確です。
学習
最初は
Plain Text
phoneme_level
で始める。
理由：
Plain Text
FastSpeech2標準
 
だから。
まずは再現性優先。


Finding #004: FastSpeech2のF0時間解像度
Python
pitch, t = pw.dio(
wav.astype(np.float64),
self.sampling_rate,
frame_period=self.hop_length / self.sampling_rate * 1000,
)
 
pitch = pw.stonemask(...)
つまり、
Plain Text
wav
↓
DIO
↓
StoneMask
↓
frame-level F0


MRPA Finding #005

10/10/2026

Markdown
## Finding #005
 
Artificial Prosody Experiment
 
Signal
 
F0 =
Accent
+ Phrase
+ Downstep
 
Results
 
Scale 1-8
High-frequency oscillations dominate.
 
Scale 16
Phrase-level structure becomes prominent.
 
Scale 32-64
Long-range trend dominates and
high-frequency oscillations disappear.
 
Interpretation
 
The result is consistent with the hypothesis:
 
Pitch Accent
→ High Frequencies
 
Accentual Phrase
→ Mid Frequencies
 
Downstep / Global Trend
→ Low Frequencies

MRPA Finding #006

研究メモへ。

Markdown
## Finding #006
 
Artificial decomposition experiment
 
Results
 
Accent:
Scale 20-21 dominant
 
Phrase:
Scale 55-64 dominant
 
Downstep:
Scale 55-64 dominant
 
Interpretation
 
The current synthetic phrase signal
occupies similar low-frequency bands
as the downstep trend.
 
Therefore phrase and downstep are not
yet separable using the current toy setup.

MRPA Finding #007

現時点の結論。

Plain Text
Accent
→ Scale ≈ 20

は成功。

Plain Text
Downstep
→ Scale ≈ 64

も成功。

しかし

Plain Text
Phrase
→ Scale ≈ 64

になってしまい、

Plain Text
Phrase

と

Plain Text
Downstep
``

の分離には失敗。

MRPA Finding #008

現在の Artificial Prosody 実験では

Plain Text
Accent
≈ Scale 20
 

と

Plain Text
Phrase + Downstep
≈ Scale 64

が共存しています。

これは実際に Combined スペクトルで

Plain Text
Scale 20
↑
局所ピーク
 
Scale 64
↑
グローバルピーク

として見えています。

なぜ重要か

これは MRPA の仮説

Plain Text
Japanese Prosody
=
Multi-Resolution Structure
``

に対して、

少なくとも

Plain Text
High-Frequency Component

と

Plain Text
Low-Frequency Component

は分離可能であることを示しています。

つまり

Plain Text
Accent
 

と

Plain Text
Downstep

は

少なくとも Toy Signal では

Plain Text
異なる Scale Preference

を持っています。

課題

ただし

Plain Text
Phrase

が

Plain Text
Scale 64

側に乗ってしまっています。

つまり現状は

Plain Text
Accent
≠
( Phrase + Downstep )

という2クラス分離しかできていません。


MRPA Finding #008（更新版）

現在の Artificial Prosody 実験では、

Plain Text
Accent
``

と

Plain Text
Phrase + Downstep

は明瞭に分離しています。

つまり

Plain Text
High Scale Band
(Scale ≈ 20)
 
Low Scale Band
(Scale ≈ 64)

という二帯域構造が既に観測されています。

10/12/2026

MRPA-3C の結果を表にすると、

Signal	Peak Scale	Peak Freqphrase_08	64	0.0127
phrase_16	51	0.0159
phrase_24	34	0.0239
phrase_32	25	0.0325

になります。

そして非常に重要なのは、

Plain Text
Phrase Frequency ↑
↓
Peak Scale ↓
 

がほぼ単調に成立していることです。

つまり

Plain Text
8π → Scale 64
16π → Scale 51
24π → Scale 34
32π → Scale 25

です。

MRPA Finding #009

今回の結果から、

CWT は少なくとも人工信号に対して

Plain Text
Prosodic Frequency
↓
Preferred Scale

の対応を持つことが確認できました。

これは MRPA 最初の定量的成功と言っていいです。

Finding #009

Phrase Frequency Sweep

8π -> Peak Scale 64 16π -> Peak Scale 51 24π -> Peak Scale 34 32π -> Peak Scale 25

Observation:

Higher phrase frequency shifts energy toward smaller scales.

This supports the hypothesis that prosodic structure can be represented as scale-preference distributions in CWT space.


完璧です。CSV自動保存は成功しています。✅

現在の MRPA-3C の結果は正式にこうまとめられます。

Signal	Peak Scale	Peak Freq	Peak Energyphrase_08	64	0.01270	1.50
phrase_16	51	0.01593	5.22
phrase_24	34	0.02390	4.37
phrase_32	25	0.03250	3.82
Finding #009 (正式版)

CWT Scale Preference は Phrase Frequency に応じて移動する。

Plain Text
Phrase Frequency ↑
↓
Peak Scale ↓

実測値:

Plain Text
8π → 64
16π → 51
24π → 34
32π → 25
さらに面白い発見

Peak Scale × Peak Freq を計算すると

Plain Text
64 × 0.01270 ≈ 0.813
 
51 × 0.01593 ≈ 0.812
 
34 × 0.02390 ≈ 0.813
 
25 × 0.03250 ≈ 0.813

ほぼ一定です。

つまり

Plain Text
Scale ∝ 1 / Frequency

が非常に綺麗に成立しています。

これは Morlet Wavelet の理論と一致します。


Finding #010

Morlet CWT obeys the inverse relation

Scale × Frequency ≈ 0.8125
for all synthetic phrase conditions tested.

This validates that phrase frequency is systematically mapped onto CWT scale space.
