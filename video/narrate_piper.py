"""Narrate script.txt with the Piper "norman" voice (public domain), one WAV per slide.

Also writes timings.json: each slide's duration and the start/end time of every sentence,
used to time the slides and captions.  Run from the video folder:  python narrate_piper.py
"""
import json
import re
import wave
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

HERE = Path(__file__).resolve().parent
MODEL = HERE / "models" / "en_US-norman-medium.onnx"
OUT = HERE / "audio_piper"
LENGTH_SCALE = 1.0      # 1.0 = the voice's normal pace (lower is faster)
SENTENCE_PAUSE = 0.40   # seconds of silence after each sentence


def slides(text):
    for block in re.split(r"(?m)^## ", text):
        if block.strip():
            head, body = block.split("\n", 1)
            yield head.strip(), body.strip()


def main():
    OUT.mkdir(exist_ok=True)
    voice = PiperVoice.load(str(MODEL))
    cfg = SynthesisConfig(length_scale=LENGTH_SCALE)
    timings = []
    for n, (head, body) in enumerate(slides((HERE / "script.txt").read_text(encoding="utf-8")), 1):
        sentences, t, rate, frames = [], 0.0, None, b""
        # split on sentence ends followed by a capital, so "A.I. safety" stays whole
        for sentence in re.split(r"(?<=[.?!])\s+(?=[A-Z])", body):
            audio = b""
            for chunk in voice.synthesize(sentence, syn_config=cfg):
                rate = chunk.sample_rate
                audio += chunk.audio_int16_bytes
            dur = len(audio) / 2 / rate
            sentences.append({"text": sentence, "start": round(t, 3), "end": round(t + dur, 3)})
            frames += audio + b"\x00\x00" * int(rate * SENTENCE_PAUSE)
            t += dur + SENTENCE_PAUSE
        with wave.open(str(OUT / f"slide{n:02d}.wav"), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(rate)
            w.writeframes(frames)
        timings.append({"slide": n, "title": head.split("|", 1)[1].strip(), "duration": round(t, 3), "sentences": sentences})
        print(f"{n:02d} {t:6.2f}s  {head}")
    (HERE / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    print(f"TOTAL {sum(s['duration'] for s in timings):.1f}s (+ gaps between slides)")


if __name__ == "__main__":
    main()
