# Audacity Cookbook

A practical collection of repeatable game-audio workflows: sound-effect design, voice cleanup, loop preparation, loudness checks, and export validation.

> **Status:** starter repository. Automated examples create and inspect deterministic audio files, but they do not replace listening tests or verification inside Audacity.

## Goals

- Keep source and exported audio specifications explicit.
- Provide reproducible, license-aware starter assets and processing recipes.
- Validate WAV format, duration, peak level, clipping, and silence with offline tests.
- Document the Audacity editor steps separately from automated file checks.
- Avoid claiming perceptual quality based only on file metadata.

## Planned example path

1. **First sound effect** — generate a short deterministic WAV fixture suitable for importing into Audacity.
2. **Cleanup workflow** — non-destructive noise reduction and high-pass workflow, with before/after listening checklist.
3. **Voice line** — dialogue editing, fades, peak/loudness targets, and export naming.
4. **Seamless loop** — boundary checks plus listening verification.
5. **Batch export** — stable filenames, metadata, and format validation.

## Quick start

Requirements: Python 3.11 or newer. Example generation and tests use only the Python standard library.

```sh
python examples/01-first-sfx/generate.py --output build/soft-pulse.wav
python -m unittest discover -s tests -v
```

Import the generated WAV into Audacity for waveform inspection and listening. Automated tests cannot establish whether a sound is pleasing, appropriate, or free of audible artifacts.

## Quality rules

- Keep raw/source audio separate from edited and delivery exports.
- Record sample rate, channel count, bit depth, peak ceiling, and intended use.
- Do not normalize blindly; preserve headroom and review true-peak behavior in the final delivery toolchain.
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
