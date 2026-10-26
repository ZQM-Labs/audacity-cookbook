# Audacity Cookbook

Repeatable game-audio workflows for sound effects, voice cleanup, music loops, loudness review, and delivery exports, using [Audacity](https://www.audacityteam.org/) alongside small, automatable checks.

> **Status:** first deterministic audio example. CI creates and inspects a WAV file using Python's standard library. No claim is made that the file has been opened in Audacity or passed a human listening review.

## What is here

- `examples/01-first-sfx/generate.py` — generates a deterministic 350 ms descending-pitch pulse.
- `tests/test_audio_contract.py` — checks WAV encoding, duration, non-silence, headroom, and byte-for-byte determinism.
- `.github/workflows/examples.yml` — runs the tests and generates a CI artifact candidate.

## Quick start

Requirements: Python 3.11 or newer. No third-party Python packages are required.

```sh
python examples/01-first-sfx/generate.py --output build/soft-pulse.wav
python -m unittest discover -s tests -v
```

## First sound effect: inspect in Audacity

1. Generate `build/soft-pulse.wav` with the command above.
2. Open the WAV in Audacity.
3. Inspect the waveform for the expected short decay and confirm there is no unexpected DC offset or abrupt click at the end.
4. Listen on headphones and a representative speaker at a conservative volume.
5. If you edit it, save an editable Audacity project separately from the delivery WAV.
6. Export using the target game's agreed sample rate, channel count, bit depth, and filename convention; re-run file checks on the exported result.

## Automated contract

The starter generator writes mono, 16-bit PCM at 44.1 kHz for approximately 0.35 seconds. The generated signal intentionally leaves digital headroom. Tests confirm measurable file properties only; they do not assess loudness perception, timbre, loop quality, accessibility, or whether the sound fits the game.

## Planned workflows

1. Noise cleanup and non-destructive dialogue editing.
2. Voice-line trims, fades, and delivery specifications.
3. Seamless-loop boundary checks plus mandatory listening review.
4. Batch export naming and metadata checks.
5. Optional integration with pinned audio-analysis tools when licensing and reproducibility are clear.

## Quality and safety rules

- Keep raw/source audio separate from edited sessions and delivery exports.
- Record sample rate, channels, bit depth, peak ceiling, and intended use.
- Do not normalize blindly; preserve headroom and review final exports in the target toolchain.
- Use original, appropriately licensed, or clearly attributed assets.
- Do not commit private voice recordings or identifiable personal audio without authorization.
- Distinguish file-integrity tests from perceptual review.

## Contribution checklist

- [ ] Include purpose, source, and expected export specification.
- [ ] Add deterministic checks for measurable requirements.
- [ ] Document manual Audacity steps and listening criteria.
- [ ] Avoid network dependencies in tests.
- [ ] State which editor/version and formats were actually tested.

## License

Unless otherwise stated, code examples are MIT-licensed. Audio assets and third-party plugins may have separate licenses; check their terms before redistribution.
