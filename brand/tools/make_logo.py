"""Generates the Fibro Gold logo SVG set. Text is outlined (no font dependency).
Run: python3 brand/tools/make_logo.py   (needs fonttools; fonts: Inter Display/Inter in /usr/share/fonts/opentype/inter)
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT_DIR = "/usr/share/fonts/opentype/inter/"
WORD_FONT = FONT_DIR + "InterDisplay-Bold.otf"
SUB_FONT = FONT_DIR + "Inter-SemiBold.otf"
OUT = os.path.join(os.path.dirname(__file__), "..", "logo")

C = dict(ink="#14161A", gold="#C8A24A", gold_deep="#9A7420", white="#FFFFFF",
         warm="#F6F3EC", mist="#B9BDC4")

_fonts = {}
def _font(p):
    if p not in _fonts:
        f = TTFont(p); _fonts[p] = (f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm)
    return _fonts[p]

def text_path(fp, text, size, tracking=0.0, x=0.0, y=0.0):
    f, gs, cmap, upm = _font(fp)
    s = size / upm
    cx, ds = x, []
    for i, ch in enumerate(text):
        g = cmap[ord(ch)]
        if ch != " ":
            pen = SVGPathPen(gs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip("."))
            gs[g].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
            ds.append(pen.getCommands())
        cx += gs[g].width * s + (tracking * size if i < len(text) - 1 else 0)
    return " ".join(ds), cx - x

def mark(uid, fill, tick_gap=13):
    """F built from three rebar segments; helical ribs knocked out via mask. 100x100 box."""
    shapes = ('<rect x="22" y="12" width="17" height="76" rx="8.5"/>'
              '<rect x="22" y="12" width="58" height="17" rx="8.5"/>'
              '<rect x="22" y="41" width="41" height="17" rx="8.5"/>')
    ticks = "" if tick_gap == 0 else "".join(f'<line x1="{x}" y1="0" x2="{x-100}" y2="100"/>' for x in range(-20, 260, tick_gap))
    return (f'<defs><mask id="m{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100">'
            f'<g fill="#fff">{shapes}</g>'
            f'<g stroke="#000" stroke-width="3.4" fill="none">{ticks}</g></mask></defs>'
            f'<rect width="100" height="100" fill="{fill}" mask="url(#m{uid})"/>')

def svg(w, h, body, bg=None):
    b = f'<rect width="{w:.0f}" height="{h:.0f}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="Fibro Gold by Fibrotech FRP">{b}{body}</svg>')

def horizontal(theme, uid):
    t = THEMES[theme]
    pad = 14
    WS, SS = 40, 11.5
    d1, w1 = text_path(WORD_FONT, "FIBRO", WS, 0.07, 0, 0)
    gap = WS * 0.36
    d2, w2 = text_path(WORD_FONT, "GOLD", WS, 0.07, 0, 0)
    ww = w1 + gap + w2
    sub, sw = text_path(SUB_FONT, "BY FIBROTECH FRP", SS, 0.26, 0, 0)
    tx = 58 + 26
    base1, base2 = 55, 77
    rule_x1 = tx + sw + 12
    rule_x2 = tx + ww
    body = (f'<g transform="translate({pad},{pad})">'
            + f'<g transform="translate(-22,0)">{mark(uid, t["mark"])}</g>' +
            f'<g transform="translate({tx},0)">'
            f'<path fill="{t["fibro"]}" d="{text_path(WORD_FONT,"FIBRO",WS,0.07,0,base1)[0]}"/>'
            f'<path fill="{t["gold"]}" d="{text_path(WORD_FONT,"GOLD",WS,0.07,w1+gap,base1)[0]}"/>'
            f'<path fill="{t["sub"]}" d="{text_path(SUB_FONT,"BY FIBROTECH FRP",SS,0.26,0,base2)[0]}"/>'
            f'<rect x="{sw+12}" y="{base2-4.3}" width="{max(ww-sw-12,0):.1f}" height="1.2" fill="{t["gold"]}"/>'
            f'</g></g>')
    W = pad * 2 + tx + ww
    return svg(W, 100 + pad * 2, body, t.get("bg"))

def stacked(theme, uid):
    t = THEMES[theme]
    pad = 16
    WS, SS = 40, 11.5
    _, w1 = text_path(WORD_FONT, "FIBRO", WS, 0.07)
    gap = WS * 0.36
    _, w2 = text_path(WORD_FONT, "GOLD", WS, 0.07)
    ww = w1 + gap + w2
    _, sw = text_path(SUB_FONT, "BY FIBROTECH FRP", SS, 0.26)
    W = ww + pad * 2
    cx = W / 2
    mark_y = pad
    base1 = pad + 100 + 38
    base2 = base1 + 26
    sx = cx - sw / 2
    rl = sx - 10 - 26
    body = (f'<g transform="translate({cx-51},{mark_y})">{mark(uid, t["mark"])}</g>'
            f'<path fill="{t["fibro"]}" d="{text_path(WORD_FONT,"FIBRO",WS,0.07,pad,base1)[0]}"/>'
            f'<path fill="{t["gold"]}" d="{text_path(WORD_FONT,"GOLD",WS,0.07,pad+w1+gap,base1)[0]}"/>'
            f'<path fill="{t["sub"]}" d="{text_path(SUB_FONT,"BY FIBROTECH FRP",SS,0.26,sx,base2)[0]}"/>'
            f'<rect x="{sx-10-26:.1f}" y="{base2-4.3}" width="26" height="1.2" fill="{t["gold"]}"/>'
            f'<rect x="{sx+sw+10:.1f}" y="{base2-4.3}" width="26" height="1.2" fill="{t["gold"]}"/>')
    return svg(W, base2 + pad, body, t.get("bg"))

def mark_only(theme, uid, tile=False, solid=False):
    t = THEMES[theme]
    gap = 0 if solid else 13
    if tile:
        body = (f'<rect width="120" height="120" rx="26" fill="{t["tile"]}"/>'
                f'<g transform="translate(9,10)">{mark(uid, t["mark"], gap)}</g>')
        return svg(120, 120, body)
    return svg(100, 100, mark(uid, t["mark"], gap))

THEMES = {
    # on dark / charcoal backgrounds
    "dark":  dict(mark=C["gold"], fibro=C["white"], gold=C["gold"], sub=C["mist"], tile=C["ink"]),
    # on light / warm white backgrounds
    "light": dict(mark=C["gold_deep"], fibro=C["ink"], gold=C["gold_deep"], sub="#4A4F57", tile=C["warm"]),
    "mono-black": dict(mark="#000000", fibro="#000000", gold="#000000", sub="#000000", tile="#FFFFFF"),
    "mono-white": dict(mark="#FFFFFF", fibro="#FFFFFF", gold="#FFFFFF", sub="#FFFFFF", tile="#000000"),
    "mono-gold": dict(mark=C["gold"], fibro=C["gold"], gold=C["gold"], sub=C["gold"], tile=C["ink"]),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for theme in THEMES:
        for name, fn in (("horizontal", horizontal), ("stacked", stacked)):
            n += 1
            open(f"{OUT}/fibro-gold-{name}-{theme}.svg", "w").write(fn(theme, f"{n}"))
        n += 1
        open(f"{OUT}/fibro-gold-mark-{theme}.svg", "w").write(mark_only(theme, f"{n}"))
    for theme in ("dark", "light"):
        n += 1
        open(f"{OUT}/fibro-gold-app-icon-{theme}.svg", "w").write(mark_only(theme, f"{n}", tile=True))
    for theme in ("dark", "light"):
        n += 1
        open(f"{OUT}/fibro-gold-favicon-{theme}.svg", "w").write(mark_only(theme, f"{n}", tile=True, solid=True))
    print("wrote", len(os.listdir(OUT)), "files")
