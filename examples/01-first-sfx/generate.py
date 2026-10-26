#!/usr/bin/env python3
"""Generate a short, deterministic, mono PCM16 WAV pulse using stdlib only."""
import argparse
import math
import struct
import wave
from pathlib import Path

SAMPLE_RATE = 44100
DURATION_SECONDS = 0.35
PEAK = 0.35


def synthesize(sample_rate=SAMPLE_RATE, duration=DURATION_SECONDS):
    count = int(sample_rate * duration)
    samples = []
    for index in range(count):
        t = index / sample_rate
        envelope = max(0.0, 1.0 - t / duration) ** 2
        frequency = 880.0 - 420.0 * (t / duration)
        value = PEAK * envelope * math.sin(2.0 * math.pi * frequency * t)
        samples.append(max(-32768, min(32767, round(value * 32767))))
    return samples


def write_wav(destination: Path):
    destination.parent.mkdir(parents=True, exist_ok=True)
    samples = synthesize()
    with wave.open(str(destination), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        output.writeframes(b"".join(struct.pack("<h", sample) for sample in samples))
    return len(samples)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("build/soft-pulse.wav"))
    args = parser.parse_args()
    count = write_wav(args.output)
    print(f"Wrote {args.output} ({count} frames at {SAMPLE_RATE} Hz, mono PCM16)")


if __name__ == "__main__":
    main()
