from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "visuals" / "senior_architect_agent_core_flow.gif"

W, H = 1200, 600
BG_TOP = (4, 9, 18)
BG_BOTTOM = (8, 15, 30)
TEXT = (240, 246, 255)
MUTED = (151, 164, 190)
GRID = (18, 32, 55)
CYAN = (45, 212, 255)
BLUE = (92, 142, 255)
GREEN = (84, 255, 170)
AMBER = (255, 192, 92)
ROSE = (255, 100, 140)
VIOLET = (190, 120, 255)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


TITLE = font(46, True)
SUB = font(22)
LABEL = font(21, True)
BODY = font(15)
SMALL = font(13)
MONO = font(14)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * max(0, min(1, t))


def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(round(lerp(x, y, t)) for x, y in zip(a, b))


def ease(t: float) -> float:
    t = max(0, min(1, t))
    return t * t * (3 - 2 * t)


def add_glow(base: Image.Image, box: tuple[int, int, int, int], color: tuple[int, int, int], radius: int = 28, alpha: int = 120) -> None:
    glow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle(box, radius=24, fill=color + (alpha,))
    glow = glow.filter(ImageFilter.GaussianBlur(radius))
    base.alpha_composite(glow)


def rounded_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: tuple[int, int, int]) -> None:
    draw.text(xy, text, font=fnt, fill=fill)


def draw_background(im: Image.Image, draw: ImageDraw.ImageDraw, progress: float) -> None:
    for y in range(H):
        t = y / H
        color = mix(BG_TOP, BG_BOTTOM, t)
        draw.line((0, y, W, y), fill=color)

    for x in range(0, W, 48):
        draw.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H, 48):
        draw.line((0, y, W, y), fill=GRID, width=1)

    orb = Image.new("RGBA", im.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    pulse = 0.45 + 0.55 * math.sin(progress * math.tau)
    od.ellipse((-120, -160, 380, 340), fill=(29, 78, 216, int(34 + 20 * pulse)))
    od.ellipse((820, 250, 1320, 760), fill=(20, 184, 166, int(28 + 18 * pulse)))
    orb = orb.filter(ImageFilter.GaussianBlur(42))
    im.alpha_composite(orb)

    draw.rounded_rectangle((28, 28, W - 28, H - 28), radius=26, outline=(38, 67, 112), width=2)


def draw_chip(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, active: float, color: tuple[int, int, int]) -> None:
    fill = mix((9, 17, 32), (16, 31, 55), active)
    outline = mix((43, 61, 92), color, active)
    draw.rounded_rectangle((x, y, x + 142, y + 34), radius=17, fill=fill, outline=outline, width=2)
    draw.ellipse((x + 13, y + 11, x + 25, y + 23), fill=mix((58, 75, 103), color, active))
    draw.text((x + 34, y + 8), label, font=SMALL, fill=mix(MUTED, TEXT, active))


def draw_code_panel(draw: ImageDraw.ImageDraw, x: int, y: int, active: float, scan: float) -> None:
    draw.rounded_rectangle((x, y, x + 210, y + 150), radius=18, fill=(7, 13, 25), outline=mix((44, 65, 100), CYAN, active), width=2)
    draw.text((x + 22, y + 18), "REAL SYSTEM", font=LABEL, fill=mix(MUTED, TEXT, active))
    files = ["src/app.ts", "routes/api.ts", "docs/adr.md", "tests/auth.spec"]
    for i, f in enumerate(files):
        yy = y + 55 + i * 22
        draw.text((x + 24, yy), f, font=MONO, fill=mix((88, 101, 124), (196, 226, 255), active))
    sy = y + 48 + int(82 * scan)
    draw.rounded_rectangle((x + 18, sy, x + 192, sy + 6), radius=3, fill=CYAN)


def draw_stage(
    im: Image.Image,
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    number: int,
    title: str,
    body: str,
    active: float,
    color: tuple[int, int, int],
) -> None:
    x1, y1, x2, y2 = box
    if active > 0.05:
        add_glow(im, (x1 - 4, y1 - 4, x2 + 4, y2 + 4), color, radius=22, alpha=int(100 * active))
    fill = mix((9, 17, 32), (18, 32, 54), active)
    outline = mix((50, 67, 98), color, active)
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=2)
    draw.ellipse((x1 + 18, y1 + 18, x1 + 46, y1 + 46), fill=mix((31, 42, 61), color, active))
    draw.text((x1 + 29 - (6 if number >= 10 else 0), y1 + 20), str(number), font=SMALL, fill=(5, 10, 18))
    draw.text((x1 + 60, y1 + 18), title, font=LABEL, fill=mix(MUTED, TEXT, active))
    draw.text((x1 + 60, y1 + 54), body, font=BODY, fill=mix((98, 112, 138), (196, 212, 235), active))


def draw_arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], active: float, color: tuple[int, int, int]) -> None:
    col = mix((54, 69, 96), color, active)
    draw.line((*start, *end), fill=col, width=4)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 13
    pts = [
        end,
        (end[0] - size * math.cos(angle - 0.45), end[1] - size * math.sin(angle - 0.45)),
        (end[0] - size * math.cos(angle + 0.45), end[1] - size * math.sin(angle + 0.45)),
    ]
    draw.polygon(pts, fill=col)


def draw_output(im: Image.Image, draw: ImageDraw.ImageDraw, active: float) -> None:
    x, y = 940, 192
    if active > 0.05:
        add_glow(im, (x - 6, y - 6, x + 200, y + 224), VIOLET, radius=26, alpha=int(95 * active))
    draw.rounded_rectangle((x, y, x + 200, y + 224), radius=22, fill=mix((9, 17, 32), (21, 28, 50), active), outline=mix((50, 67, 98), VIOLET, active), width=2)
    draw.text((x + 28, y + 26), "DELIVER", font=LABEL, fill=mix(MUTED, TEXT, active))
    items = ["maps", "risks", "questions", "handoff"]
    for i, item in enumerate(items):
        yy = y + 72 + i * 33
        draw.rounded_rectangle((x + 28, yy + 2, x + 46, yy + 20), radius=4, fill=mix((43, 55, 78), GREEN, active))
        draw.text((x + 60, yy), item, font=BODY, fill=mix((98, 112, 138), TEXT, active))


def frame(progress: float) -> Image.Image:
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    draw = ImageDraw.Draw(im)
    draw_background(im, draw, progress)

    draw.text((72, 64), "Senior Architect Agent", font=TITLE, fill=TEXT)
    draw.text((74, 118), "A discipline layer that makes AI understand before it acts.", font=SUB, fill=MUTED)
    draw.line((74, 154, 1124, 154), fill=CYAN, width=3)

    stage_float = progress * 5.25
    active = [ease(stage_float - i) for i in range(5)]

    draw_chip(draw, 74, 178, "Evidence first", active[1], CYAN)
    draw_chip(draw, 232, 178, "No hallucination", active[2], GREEN)
    draw_chip(draw, 408, 178, "Right-sized pass", active[3], AMBER)

    draw_code_panel(draw, 74, 262, active[0], (progress * 2.8) % 1)

    stages = [
        ((330, 210, 520, 318), 1, "Inspect", "files, docs, history", CYAN),
        ((565, 210, 755, 318), 2, "Classify", "facts vs unknowns", GREEN),
        ((448, 372, 638, 480), 3, "Question", "risks before design", AMBER),
        ((684, 372, 874, 480), 4, "Map", "boundaries + flows", BLUE),
    ]
    for i, (box, num, title, body, color) in enumerate(stages):
        draw_stage(im, draw, box, num, title, body, active[i], color)

    draw_arrow(draw, (284, 337), (330, 264), active[0], CYAN)
    draw_arrow(draw, (520, 264), (565, 264), active[1], GREEN)
    draw_arrow(draw, (660, 318), (555, 372), active[2], AMBER)
    draw_arrow(draw, (638, 426), (684, 426), active[3], BLUE)
    draw_arrow(draw, (874, 426), (940, 304), active[4], VIOLET)
    draw_output(im, draw, active[4])

    gate_y = 526
    draw.text((74, gate_y), "checkpoint gates:", font=SMALL, fill=MUTED)
    gates = ["scope clear", "evidence traced", "status labeled", "safe handoff"]
    for i, gate in enumerate(gates):
        t = active[min(i + 1, 4)]
        x = 198 + i * 170
        draw.rounded_rectangle((x, gate_y - 5, x + 146, gate_y + 24), radius=14, fill=mix((10, 20, 36), (15, 46, 42), t), outline=mix((45, 61, 88), GREEN, t), width=1)
        draw.text((x + 16, gate_y + 1), gate, font=SMALL, fill=mix((112, 126, 152), TEXT, t))

    return im.convert("P", palette=Image.Palette.ADAPTIVE, colors=160)


def main() -> None:
    frames = [frame(i / 59) for i in range(60)]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=76,
        loop=0,
        optimize=True,
        disposal=2,
    )


if __name__ == "__main__":
    main()
