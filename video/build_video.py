"""Build the 3-minute video: 12 slides (1920x1080), captions timed to the Piper narration, one MP4.

Needs timings.json and audio_piper/ from narrate_piper.py.  Run from the video folder:  python build_video.py
"""
import json
import subprocess
import wave
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FRAMES = HERE / "frames"
OUT_MP4 = HERE / "conditions_not_cutoffs.mp4"
W, H = 1920, 1080
GAP = 0.6                      # pause between slides, seconds
EXTRA_HOLD = {1: 1.2, 12: 2.5}  # let the title and credits sit a little longer

BG, INK, MUTED = (248, 246, 241), (31, 41, 51), (96, 106, 116)
TEAL, AMBER = (15, 118, 110), (180, 83, 9)
CARD, LINE = (255, 255, 255), (221, 216, 207)
TEAL_TINT, AMBER_TINT = (225, 241, 238), (250, 236, 222)

FONTS = Path("C:/Windows/Fonts")
_cache = {}


def font(weight, size):
    files = {"regular": "segoeui.ttf", "semibold": "seguisb.ttf", "bold": "segoeuib.ttf", "light": "segoeuil.ttf"}
    key = (weight, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(str(FONTS / files[weight]), size)
    return _cache[key]


def wrap(d, text, f, width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if d.textlength(trial, font=f) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def text(d, xy, s, f, fill=INK, width=None, spacing=1.25, anchor="la"):
    x, y = xy
    lines = wrap(d, s, f, width) if width else [s]
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill, anchor=anchor)
        y += int(f.size * spacing)
    return y


def header(d, kicker, title, color=TEAL):
    d.rectangle([120, 104, 132, 140], fill=color)
    d.text((152, 100), kicker.upper(), font=font("semibold", 32), fill=color)
    return text(d, (120, 160), title, font("bold", 68), width=1680, spacing=1.15)


def card(d, box, fill=CARD, outline=LINE, radius=22, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def check(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    d.line([(cx - r * 0.45, cy + r * 0.02), (cx - r * 0.1, cy + r * 0.38), (cx + r * 0.5, cy - r * 0.35)], fill=CARD, width=8, joint="curve")


def cross(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    k = r * 0.42
    d.line([(cx - k, cy - k), (cx + k, cy + k)], fill=CARD, width=8)
    d.line([(cx - k, cy + k), (cx + k, cy - k)], fill=CARD, width=8)


def tag(d, x, y, label, fg, bg):
    f = font("semibold", 30)
    w = d.textlength(label, font=f)
    d.rounded_rectangle([x, y, x + w + 40, y + 50], radius=25, fill=bg)
    d.text((x + 20, y + 25), label, font=f, fill=fg, anchor="lm")


# ---------------------------------------------------------------- slides

def s01(d):
    d.text((W / 2, 380), "Conditions, not cutoffs", font=font("bold", 120), fill=INK, anchor="mm")
    d.rectangle([W / 2 - 90, 470, W / 2 + 90, 478], fill=TEAL)
    d.text((W / 2, 550), "What chip-supply-chain countries can credibly ask for on AI safety",
           font=font("regular", 48), fill=INK, anchor="mm")
    d.text((W / 2, 650), "Middle Powers hackathon  ·  Track C (Diplomacy)  ·  November 2026",
           font=font("regular", 34), fill=MUTED, anchor="mm")


def s02(d):
    header(d, "The question", "")
    y = text(d, (120, 250), "A few countries outside the US and China make parts of the AI chip supply chain that nobody can yet do without.",
             font("regular", 54), width=1650)
    end = text(d, (165, y + 40), "Which AI-safety asks could they credibly make, and what should they avoid?",
               font("semibold", 62), fill=TEAL, width=1600, spacing=1.2)
    d.rectangle([120, y + 48, 128, end - 6], fill=TEAL)


def s03(d):
    header(d, "Why now", "Their hold won't last")
    for i, (who, what) in enumerate([("United States", "CHIPS Act subsidies and new fabs, such as TSMC's in Arizona"),
                                     ("China", "A national push to make its own chips and chipmaking tools")]):
        x = 120 + i * 850
        card(d, [x, 300, x + 800, 560])
        d.text((x + 50, 340), who, font=font("bold", 48), fill=INK)
        text(d, (x + 50, 420), what, font("regular", 38), fill=MUTED, width=700)
    d.text((120, 640), "Two ways to waste it:", font=font("regular", 46), fill=INK)
    tag(d, 600, 640, "never use it", AMBER, AMBER_TINT)
    tag(d, 860, 640, "use it badly", AMBER, AMBER_TINT)


def s04(d):
    header(d, "What we did", "A rule, five past cases, one comparison")
    rows = [("A rule picks the countries",
             "Firms hold 40% or more of world supply of a specific chip input (ETO data, mostly 2025)"),
            ("Five past supplier coalitions with known endings",
             "Arab oil embargo 1973  ·  CIPEC copper 1967  ·  Tin council 1985  ·  China–Japan rare earths 2010  ·  Japan–Korea chip materials 2019"),
            ("Compare today with the past",
             "35 chokepoints scored on the same six features, with the US as the target")]
    y = 300
    for i, (head, sub) in enumerate(rows, 1):
        d.ellipse([120, y, 196, y + 76], fill=TEAL)
        d.text((158, y + 38), str(i), font=font("bold", 40), fill=CARD, anchor="mm")
        d.text((230, y - 2), head, font=font("semibold", 46), fill=INK)
        text(d, (230, y + 62), sub, font("regular", 34), fill=MUTED, width=1560)
        y += 180


def s05(d):
    header(d, "Who holds the chokepoints", "Eight countries")
    cells = [("Japan", "22", "inputs, e.g. resist processing tools 95%"),
             ("Netherlands", "100%", "EUV lithography (ASML)"),
             ("South Korea", "81%", "HBM memory (2025 projection)"),
             ("Taiwan", "69%", "leading-edge chipmaking (2022)"),
             ("Germany", "82%", "mask aligners"),
             ("Austria", "48%", "wafer bonding tools"),
             ("Singapore", "91%", "ball bonders"),
             ("Sweden", "71%", "laser mask writers")]
    for i, (country, big, sub) in enumerate(cells):
        r, c = divmod(i, 4)
        x, y = 120 + c * 425, 290 + r * 290
        card(d, [x, y, x + 395, y + 260])
        d.text((x + 34, y + 26), country, font=font("semibold", 38), fill=INK)
        d.text((x + 34, y + 80), big, font=font("bold", 72), fill=TEAL)
        text(d, (x + 34, y + 172), sub, font("regular", 28), fill=MUTED, width=340, spacing=1.2)
    d.text((120, 880 - 6), "Share of world supply, 2025 unless stated. Sources: ETO (Sept 2026 release), TrendForce, SIA/BCG.",
           font=font("regular", 26), fill=MUTED)


def s06(d):
    title_end = header(d, "What history says", "Leverage held only when replacing supply took more than five years")
    rows = [("Arab oil embargo, 1973", "More than 5 years", "Partly worked", TEAL, TEAL_TINT),
            ("CIPEC copper exporters, 1967", "2 to 5 years", "Failed", AMBER, AMBER_TINT),
            ("International Tin Council, 1985", "2 to 5 years", "Backfired", AMBER, AMBER_TINT),
            ("China's rare earths and Japan, 2010", "2 to 5 years", "Backfired", AMBER, AMBER_TINT),
            ("Japan's chip materials and Korea, 2019", "2 to 5 years", "Backfired", AMBER, AMBER_TINT)]
    y0 = title_end + 90
    d.text((120, y0 - 50), "Past case", font=font("semibold", 28), fill=MUTED)
    d.text((1000, y0 - 50), "Time for target to replace", font=font("semibold", 28), fill=MUTED)
    d.text((1460, y0 - 50), "Outcome", font=font("semibold", 28), fill=MUTED)
    for i, (case, t, outcome, fg, bg) in enumerate(rows):
        y = y0 + i * 100
        d.line([(120, y), (1800, y)], fill=LINE, width=2)
        d.text((120, y + 50), case, font=font("regular", 40), fill=INK, anchor="lm")
        d.text((1000, y + 50), t, font=font("semibold" if i == 0 else "regular", 40), fill=fg if i == 0 else INK, anchor="lm")
        tag(d, 1460, y + 25, outcome, fg, bg)
    d.line([(120, y0 + 500), (1800, y0 + 500)], fill=LINE, width=2)


def s07(d):
    header(d, "Today", "Where today's coalition stands")
    for i, (big, sub) in enumerate([("27 of 35", "chokepoints the US could replace within about five years"),
                                    ("32 of 35", "held by countries that rely on the US for their security")]):
        x = 120 + i * 850
        card(d, [x, 300, x + 800, 640])
        d.text((x + 50, 330), big, font=font("bold", 120), fill=AMBER)
        text(d, (x + 50, 510), sub, font("regular", 40), fill=INK, width=700)
    d.text((120, 720), "A threat from this group looks like the cases that backfired.", font=font("semibold", 46), fill=INK)


def s08(d):
    header(d, "Coordinate on", "Three asks that work with US policy")
    rows = [("Shared anti-diversion checks", "Keep advanced chips away from actors with no safety oversight"),
            ("Evaluator access to frontier models", "For members' own AI safety institutes, agreed alongside the checks"),
            ("Support for US-led hardware verification", "For example, location checks built into chips")]
    for i, (head, sub) in enumerate(rows):
        y = 310 + i * 175
        check(d, 165, y + 45, 42, TEAL)
        d.text((240, y), head, font=font("semibold", 50), fill=INK)
        d.text((240, y + 72), sub, font=font("regular", 36), fill=MUTED)


def s09(d):
    header(d, "Avoid", "Three moves likely to backfire", color=AMBER)
    rows = [("Withholding supply", "The US could replace most of it within five years, and the holders rely on the US for security"),
            ("Coordinating prices", "Failed in both past cases where producers tried it"),
            ("Threatening to sell to China", "Contradicts the anti-diversion checks, and would not be believed")]
    for i, (head, sub) in enumerate(rows):
        y = 310 + i * 175
        cross(d, 165, y + 45, 42, AMBER)
        d.text((240, y), head, font=font("semibold", 50), fill=INK)
        d.text((240, y + 72), sub, font=font("regular", 36), fill=MUTED)


def s10(d):
    y = header(d, "The catch", "The most valuable ask is not credible")
    d.text((120, y + 10), "Binding safety conditions on the biggest buyers of compute", font=font("regular", 44), fill=MUTED)
    chain = ["ASML", "TSMC", "Nvidia", "Cloud firms", "AI labs"]
    bw, gap, top = 270, 77, 470
    for i, name in enumerate(chain):
        x = 120 + i * (bw + gap)
        coalition = i == 0
        card(d, [x, top, x + bw, top + 130], fill=TEAL_TINT if coalition else (AMBER_TINT if i == 4 else CARD),
             outline=TEAL if coalition else (AMBER if i == 4 else LINE), width=3)
        d.text((x + bw / 2, top + 65), name, font=font("semibold", 42), fill=INK, anchor="mm")
        if i < len(chain) - 1:
            ax = x + bw + 10
            d.line([(ax, top + 65), (ax + gap - 24, top + 65)], fill=MUTED, width=5)
            d.polygon([(ax + gap - 20, top + 65), (ax + gap - 38, top + 52), (ax + gap - 38, top + 78)], fill=MUTED)
    d.text((120 + bw / 2, top + 175), "The coalition sits here", font=font("semibold", 32), fill=TEAL, anchor="mm")
    last = 120 + 4 * (bw + gap) + bw / 2
    d.text((last, top + 175), "Conditions would apply here", font=font("semibold", 32), fill=AMBER, anchor="mm")
    d.text((120, 760), "Enforcing it would take a threat to cut supply, the pattern that backfired.", font=font("semibold", 44), fill=INK)


def s11(d):
    header(d, "A first cut", "Built on five past cases")
    for i, item in enumerate(["The scores involve judgment, and one person made the final call on each",
                              "Most past cases are commodities; chips are harder to replace",
                              "Test it, challenge it, build on it"]):
        y = 320 + i * 130
        d.ellipse([130, y + 22, 154, y + 46], fill=TEAL)
        text(d, (190, y), item, font("regular" if i < 2 else "semibold", 46), fill=INK, width=1600)


def s12(d):
    d.text((W / 2, 300), "Conditions, not cutoffs", font=font("bold", 88), fill=INK, anchor="mm")
    d.rectangle([W / 2 - 80, 370, W / 2 + 80, 377], fill=TEAL)
    d.text((W / 2, 460), "Andrew Ayobami, Ayodele Abraham and Gideon Bature", font=font("semibold", 50), fill=INK, anchor="mm")
    d.text((W / 2, 570), "Video made with Claude  ·  Narration: Piper text-to-speech, \"Norman\" voice (public domain)",
           font=font("regular", 32), fill=MUTED, anchor="mm")
    d.text((W / 2, 625), "Data: ETO Semiconductor Supply Chain Dataset (Sept 2026)  ·  TrendForce (2025)  ·  SIA/BCG (2024)",
           font=font("regular", 32), fill=MUTED, anchor="mm")
    d.text((W / 2, 710), "Middle Powers hackathon  ·  Track C (Diplomacy)  ·  November 2026",
           font=font("regular", 32), fill=MUTED, anchor="mm")


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12]


def caption(img, s):
    s = s.replace("A.S.M.L.", "ASML").replace("A.I.", "AI")
    d = ImageDraw.Draw(img, "RGBA")
    for size in (40, 36, 32):
        f = font("regular", size)
        lines = wrap(d, s, f, 1560)
        if len(lines) <= 2:
            break
    lh = int(size * 1.3)
    box_h = lh * len(lines) + 40
    top = H - 70 - box_h
    d.rounded_rectangle([160, top, W - 160, H - 70], radius=18, fill=(31, 41, 51, 228))
    y = top + 20
    for ln in lines:
        d.text((W / 2, y + lh / 2), ln, font=f, fill=(255, 255, 255), anchor="mm")
        y += lh
    return img


def main():
    timings = json.loads((HERE / "timings.json").read_text(encoding="utf-8"))
    FRAMES.mkdir(exist_ok=True)
    for old in FRAMES.glob("*.png"):
        old.unlink()

    entries, audio, params = [], b"", None
    for t in timings:
        n = t["slide"]
        base = Image.new("RGB", (W, H), BG)
        SLIDES[n - 1](ImageDraw.Draw(base))
        base.save(FRAMES / f"slide{n:02d}.png")            # clean copy, no caption
        slide_len = t["duration"] + EXTRA_HOLD.get(n, 0) + (GAP if n < len(timings) else 0)
        sents = t["sentences"]
        for i, s in enumerate(sents):
            start = 0.0 if i == 0 else s["start"]
            end = sents[i + 1]["start"] if i + 1 < len(sents) else slide_len
            path = FRAMES / f"s{n:02d}_c{i:02d}.png"
            caption(base.copy(), s["text"]).save(path)
            entries.append((path, end - start))
        with wave.open(str(HERE / "audio_piper" / f"slide{n:02d}.wav")) as w:
            params = params or w.getparams()
            audio += w.readframes(w.getnframes())
        pad = slide_len - t["duration"]
        audio += b"\x00\x00" * int(params.framerate * pad)

    with wave.open(str(HERE / "narration_full.wav"), "wb") as w:
        w.setparams(params)
        w.writeframes(audio)
    total = sum(d for _, d in entries)

    listing = HERE / "frames.txt"
    with open(listing, "w", encoding="utf-8") as fh:
        for path, dur in entries:
            fh.write(f"file '{path.as_posix()}'\nduration {dur:.3f}\n")
        fh.write(f"file '{entries[-1][0].as_posix()}'\n")

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ffmpeg, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listing),
           "-i", str(HERE / "narration_full.wav"), "-r", "30", "-c:v", "libx264", "-preset", "medium",
           "-tune", "stillimage", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
           "-t", f"{total:.3f}", "-movflags", "+faststart", str(OUT_MP4)]
    subprocess.run(cmd, check=True)
    print(f"video: {OUT_MP4.name}  length {int(total // 60)}:{total % 60:04.1f}  frames {len(entries)}")


if __name__ == "__main__":
    main()
