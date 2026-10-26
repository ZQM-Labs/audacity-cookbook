import importlib.util
import tempfile
import unittest
import wave
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "examples/01-first-sfx/generate.py"
SPEC = importlib.util.spec_from_file_location("generate_sfx", SCRIPT)
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


class AudioContractTests(unittest.TestCase):
    def test_generated_wav_has_documented_format_and_duration(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "soft-pulse.wav"
            frame_count = GENERATOR.write_wav(output)
            with wave.open(str(output), "rb") as audio:
                self.assertEqual(audio.getnchannels(), 1)
                self.assertEqual(audio.getsampwidth(), 2)
                self.assertEqual(audio.getframerate(), 44100)
                self.assertEqual(audio.getnframes(), frame_count)
                self.assertAlmostEqual(audio.getnframes() / audio.getframerate(), 0.35, places=3)

    def test_audio_is_non_silent_and_has_headroom(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "soft-pulse.wav"
            GENERATOR.write_wav(output)
            with wave.open(str(output), "rb") as audio:
                import array
                samples = array.array("h")
                samples.frombytes(audio.readframes(audio.getnframes()))
            self.assertGreater(max(abs(value) for value in samples), 1000)
            self.assertLess(max(abs(value) for value in samples), 32767)

    def test_generation_is_deterministic(self):
        with tempfile.TemporaryDirectory() as temporary:
            first, second = Path(temporary) / "a.wav", Path(temporary) / "b.wav"
            GENERATOR.write_wav(first)
            GENERATOR.write_wav(second)
            self.assertEqual(first.read_bytes(), second.read_bytes())


if __name__ == "__main__":
    unittest.main()
