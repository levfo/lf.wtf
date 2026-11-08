"""Writes the inline SVG diagrams for /research/circuit-grafts/ between <!-- dg:NAME:start/end --> markers.

Each diagram has two drawings: .dg-wide (desktop) and .dg-narrow (phones, vertical); CSS shows one.
SVG labels are short text nodes, so tools/i18n.py translates them like any other copy (no role="img"
or aria-hidden on the SVGs: the walker would skip their text). Facts used, nothing else:
30 layers (attention then MLP), hidden state 576 wide, 9 heads, ~134.5M weights; the read and both
switches tap layer 20's MLP input; the push is added to layer 29's MLP output before the output head;
three-digit addition joins layers 14, 20 and 21; grafts are 25,270 to 121,198 added weights.
The neuron dots are a sample per layer, not to scale, and the hero says so.

    PYTHONUTF8=1 python tools/diagrams/circuit_grafts.py
"""
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "research/circuit-grafts/index.html"
SCAN = Path(r"C:/Users/leviq/Projects/WspLoop/reports/tiny/read_scan.json")


def defs(i):
    return (f'<defs><marker id="ah{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ah"/></marker>'
            f'<marker id="ab{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahb"/></marker></defs>')


def badge(x, y, n):
    return (f'<g class="badge"><circle cx="{x:.1f}" cy="{y:.1f}" r="11"/>'
            f'<text x="{x:.1f}" y="{y+4.5:.1f}" text-anchor="middle">{n}</text></g>')


TITLE = "Where the graft sits in SmolLM2-135M"
DESC = ("Text enters as tokens, passes through 30 layers of neurons, and the output head picks the next token. "
        "The graft is a small added circuit beside the layers. It reads layer 20 and adds its push to the last "
        "layer, layer 29, just before the output head. The original neurons are unchanged.")


def graft_mini(x, y, w, h):
    """A tiny circuit inside the graft box: read nodes, table nodes, push node."""
    s = []
    cols = [(x + w * 0.18, 4), (x + w * 0.5, 3), (x + w * 0.82, 1)]
    pts = []
    for cx, n in cols:
        col = [(cx, y + h * (k + 1) / (n + 1)) for k in range(n)]
        pts.append(col)
    for a, b in zip(pts, pts[1:]):
        for p in a:
            for q in b:
                s.append(f'<line class="gw" x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}"/>')
    for col in pts:
        for p in col:
            s.append(f'<circle class="gn" cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="4"/>')
    return "".join(s)


def hero_wide():
    rnd = random.Random(7)
    s = [f'<svg class="dg dg-wide hero-dg" viewBox="0 0 1000 400" aria-labelledby="dg1-t dg1-d">',
         f'<title id="dg1-t">{TITLE}</title><desc id="dg1-d">{DESC}</desc>', defs(1)]
    x0, x1, y0, y1, rows = 112, 772, 150, 318, 15
    step = (x1 - x0) / 29
    cx = lambda i: x0 + i * step
    mid = (y0 + y1) / 2
    # field of neurons, a sample per layer
    for i in range(30):
        s.append(f'<rect class="lcol" x="{cx(i)-8:.1f}" y="{y0-10}" width="16" height="{y1-y0+20}"/>')
        for k in range(rows):
            yy = y0 + k * (y1 - y0) / (rows - 1) + rnd.uniform(-2.5, 2.5)
            s.append(f'<circle class="nd" cx="{cx(i)+rnd.uniform(-2.5, 2.5):.1f}" cy="{yy:.1f}" r="2.4"/>')
    for i in (0, 14, 20, 21, 29):
        s.append(f'<text class="num" x="{cx(i):.1f}" y="{y1+30}" text-anchor="middle">{i}</text>')
    s.append(f'<text class="small" x="{x0-8}" y="{y1+54}">Layers 0 to 29. Dots are a sample of each layer, not to scale.</text>')
    # tokens in, output head, next token
    s.append(f'<text class="lbl" x="14" y="{mid-6}">Tokens</text><text class="small" x="14" y="{mid+14}">in</text>')
    s.append(f'<line class="spine" x1="60" y1="{mid+30}" x2="{x0-14}" y2="{mid+30}" marker-end="url(#ah1)"/>')
    s.append(f'<line class="spine" x1="{x1+14}" y1="{mid+30}" x2="{x1+40}" y2="{mid+30}" marker-end="url(#ah1)"/>')
    s.append(f'<rect class="box" x="{x1+44}" y="{mid-6}" width="82" height="72"/>')
    s.append(f'<text class="lbl" x="{x1+85}" y="{mid+24}" text-anchor="middle">Output</text>')
    s.append(f'<text class="lbl" x="{x1+85}" y="{mid+44}" text-anchor="middle">head</text>')
    s.append(f'<line class="spine" x1="{x1+126}" y1="{mid+30}" x2="{x1+150}" y2="{mid+30}" marker-end="url(#ah1)"/>')
    s.append(f'<text class="lbl" x="{x1+156}" y="{mid+24}">Next</text><text class="lbl" x="{x1+156}" y="{mid+44}">token</text>')
    # the graft
    gx, gy, gw, gh = 470, 14, 330, 92
    s.append(f'<rect class="graft" x="{gx}" y="{gy}" width="{gw}" height="{gh}"/>')
    s.append(f'<text class="gt" x="{gx+14}" y="{gy+26}">Graft</text>')
    s.append(f'<text class="small" x="{gx+14}" y="{gy+46}">25,270 to 121,198</text>')
    s.append(f'<text class="small" x="{gx+14}" y="{gy+64}">added weights,</text>')
    s.append(f'<text class="small" x="{gx+14}" y="{gy+82}">under 0.1%</text>')
    s.append(graft_mini(gx + 150, gy + 4, 170, gh - 8))
    # wiring: read from 20, lighter reads from 14 and 21, write into 29
    s.append(f'<rect class="tap" x="{cx(20)-9:.1f}" y="{y0-12}" width="18" height="{y1-y0+24}"/>')
    s.append(f'<line class="flow" x1="{cx(20):.1f}" y1="{y0-12}" x2="{cx(20):.1f}" y2="{gy+gh}" marker-end="url(#ab1)"/>')
    s.append(badge(cx(20) - 24, 128, 1))
    s.append(f'<path class="flow dash" d="M{cx(14):.1f},{y0-12} V{gy+gh/2} H{gx}" marker-end="url(#ab1)"/>')
    s.append(f'<line class="flow dash" x1="{cx(21):.1f}" y1="{y0-12}" x2="{cx(21):.1f}" y2="{gy+gh}"/>')
    s.append(badge(cx(14) - 24, 128, 3))
    wx = cx(29) + 14
    s.append(f'<rect class="tap" x="{cx(29)-9:.1f}" y="{y0-12}" width="18" height="{y1-y0+24}"/>')
    s.append(f'<path class="flow" d="M{gx+gw-30},{gy+gh} V{y0-24} H{wx:.1f} V{mid+24}" marker-end="url(#ab1)"/>')
    s.append(badge(wx + 26, y0 - 24, 2))
    # legend
    ly = 388
    s.append(f'<circle class="nd" cx="{x0}" cy="{ly-4}" r="3.5"/><text class="small" x="{x0+12}" y="{ly}">Original neurons, unchanged</text>')
    s.append(f'<circle class="gn" cx="{x0+300}" cy="{ly-4}" r="4"/><text class="small" x="{x0+312}" y="{ly}">Graft, added beside the layers</text>')
    s.append('</svg>')
    return "".join(s)


def hero_narrow():
    rnd = random.Random(11)
    s = [f'<svg class="dg dg-narrow hero-dg" viewBox="0 0 360 730" aria-labelledby="dg1n-t dg1n-d">',
         f'<title id="dg1n-t">{TITLE}</title><desc id="dg1n-d">{DESC}</desc>', defs(2)]
    lx0, lx1, y0, step, dots = 30, 178, 70, 15.5, 11
    cy = lambda i: y0 + i * step
    s.append(f'<text class="lbl" x="{(lx0+lx1)/2}" y="24" text-anchor="middle">Tokens in</text>')
    s.append(f'<line class="spine" x1="{(lx0+lx1)/2}" y1="32" x2="{(lx0+lx1)/2}" y2="{y0-12}" marker-end="url(#ah2)"/>')
    for i in range(30):
        s.append(f'<rect class="lcol" x="{lx0-6}" y="{cy(i)-6}" width="{lx1-lx0+12}" height="12"/>')
        for k in range(dots):
            xx = lx0 + k * (lx1 - lx0) / (dots - 1) + rnd.uniform(-2, 2)
            s.append(f'<circle class="nd" cx="{xx:.1f}" cy="{cy(i)+rnd.uniform(-1.5, 1.5):.1f}" r="2.2"/>')
    for i in (0, 14, 20, 21, 29):
        s.append(f'<text class="num" x="{lx0-10}" y="{cy(i)+4:.1f}" text-anchor="end">{i}</text>')
    hy = cy(29) + 22
    s.append(f'<line class="spine" x1="{(lx0+lx1)/2}" y1="{cy(29)+8}" x2="{(lx0+lx1)/2}" y2="{hy-2}" marker-end="url(#ah2)"/>')
    s.append(f'<rect class="box" x="{lx0-6}" y="{hy}" width="{lx1-lx0+12}" height="34"/>')
    s.append(f'<text class="lbl" x="{(lx0+lx1)/2}" y="{hy+22}" text-anchor="middle">Output head</text>')
    s.append(f'<line class="spine" x1="{(lx0+lx1)/2}" y1="{hy+34}" x2="{(lx0+lx1)/2}" y2="{hy+54}" marker-end="url(#ah2)"/>')
    s.append(f'<text class="lbl" x="{(lx0+lx1)/2}" y="{hy+74}" text-anchor="middle">Next token</text>')
    # graft
    gx, gy, gw, gh = 204, cy(15), 152, 150
    s.append(f'<rect class="graft" x="{gx}" y="{gy}" width="{gw}" height="{gh}"/>')
    s.append(f'<text class="gt" x="{gx+12}" y="{gy+26}">Graft</text>')
    s.append(f'<text class="small" x="{gx+12}" y="{gy+46}">25,270 to 121,198</text>')
    s.append(f'<text class="small" x="{gx+12}" y="{gy+64}">added weights,</text>')
    s.append(f'<text class="small" x="{gx+12}" y="{gy+82}">under 0.1%</text>')
    s.append(graft_mini(gx + 8, gy + 90, gw - 16, 56))
    s.append(f'<rect class="tap" x="{lx0-8}" y="{cy(20)-8}" width="{lx1-lx0+16}" height="16"/>')
    s.append(f'<path class="flow" d="M{lx1+8},{cy(20)} H{gx}" marker-end="url(#ab2)"/>')
    s.append(badge(lx1 + 22, cy(20) - 16, 1))
    s.append(f'<path class="flow dash" d="M{lx1+8},{cy(14)} H{gx+gw/2} V{gy}" marker-end="url(#ab2)"/>')
    s.append(f'<path class="flow dash" d="M{lx1+8},{cy(21)} H{gx}"/>')
    s.append(badge(lx1 + 22, cy(14) - 16, 3))
    s.append(f'<rect class="tap" x="{lx0-8}" y="{cy(29)-8}" width="{lx1-lx0+16}" height="16"/>')
    s.append(f'<path class="flow" d="M{gx+gw/2},{gy+gh} V{cy(29)} H{lx1+10}" marker-end="url(#ab2)"/>')
    s.append(badge(gx + gw / 2 + 22, cy(29) - 16, 2))
    ly = hy + 106
    s.append(f'<circle class="nd" cx="{lx0-6}" cy="{ly-4}" r="3.5"/><text class="small" x="{lx0+6}" y="{ly}">Original neurons, unchanged</text>')
    s.append(f'<circle class="gn" cx="{lx0-6}" cy="{ly+18}" r="4"/><text class="small" x="{lx0+6}" y="{ly+22}">Graft, added beside the layers</text>')
    s.append(f'<text class="small" x="{lx0-10}" y="{ly+48}">Dots are a sample of each layer, not to scale.</text>')
    s.append('</svg>')
    return "".join(s)


# ---------------------------------------------------------------- 2. inside the graft, 38 + 47
STEPS = [
    ("1", "Read", ["first number: 3, 8", "second number: 4, 7", "answer digits left: 2"]),
    ("2", "Rules", ["units: 8 + 7 = 15", "write 5, carry 1", "tens: 3 + 4 + 1 = 8"]),
    ("3", "Write", ["first answer digit:", "push 8", "next answer digit:", "push 5"]),
    ("4", "Switches", ["push × switch × switch", "on: writing this answer", "off: other text"]),
]
T2 = "Inside the graft, for 38 + 47"
D2 = ("Read the digits, apply the rules, push the right digit, and let the two switches decide when the push is on. "
      "The push is added at layer 29 and the model writes 85.")
END2 = "Added at layer 29. The model writes 85."


def inside_wide():
    s = [f'<svg class="dg dg-wide" viewBox="0 0 1000 262" aria-labelledby="dg2-t dg2-d">',
         f'<title id="dg2-t">{T2}</title><desc id="dg2-d">{D2}</desc>', defs(3)]
    bw, gap = 226, 30
    for k, (n, head, lines) in enumerate(STEPS):
        x = 4 + k * (bw + gap)
        s.append(f'<rect class="{"graft" if k == 2 else "box"}" x="{x}" y="10" width="{bw}" height="168"/>')
        s.append(badge(x + 24, 36, n))
        s.append(f'<text class="gt" x="{x+44}" y="42">{head}</text>')
        for j, line in enumerate(lines):
            big = line.startswith("push ") and "×" not in line
            s.append(f'<text class="{"big" if big else "lbl"}" x="{x+16}" y="{78+j*26}">{line}</text>')
        if k < 3:
            s.append(f'<line class="spine" x1="{x+bw+2}" y1="94" x2="{x+bw+gap-4}" y2="94" marker-end="url(#ah3)"/>')
    s.append('<line class="flow" x1="500" y1="178" x2="500" y2="206" marker-end="url(#ab3)"/>')
    s.append('<rect class="box" x="250" y="210" width="500" height="44"/>')
    s.append(f'<text class="lbl" x="500" y="237" text-anchor="middle">{END2}</text>')
    s.append('</svg>')
    return "".join(s)


def inside_narrow():
    bh, gap = 132, 24
    H = 4 * (bh + gap) + 52
    s = [f'<svg class="dg dg-narrow" viewBox="0 0 360 {H}" aria-labelledby="dg2n-t dg2n-d">',
         f'<title id="dg2n-t">{T2}</title><desc id="dg2n-d">{D2}</desc>', defs(4)]
    for k, (n, head, lines) in enumerate(STEPS):
        y = 4 + k * (bh + gap)
        s.append(f'<rect class="{"graft" if k == 2 else "box"}" x="4" y="{y}" width="352" height="{bh}"/>')
        s.append(badge(28, y + 26, n))
        s.append(f'<text class="gt" x="48" y="{y+32}">{head}</text>')
        if k == 2:
            lines = [lines[0] + " " + lines[1], lines[2] + " " + lines[3]]
        for j, line in enumerate(lines):
            s.append(f'<text class="lbl" x="18" y="{y+64+j*24}">{line}</text>')
        s.append(f'<line class="{"flow" if k == 3 else "spine"}" x1="180" y1="{y+bh}" x2="180" y2="{y+bh+gap-3}" '
                 f'marker-end="url(#{"ab4" if k == 3 else "ah4"})"/>')
    y = 4 + 4 * (bh + gap)
    s.append(f'<rect class="box" x="4" y="{y}" width="352" height="44"/>')
    s.append(f'<text class="lbl fit" x="180" y="{y+27}" text-anchor="middle">{END2}</text>')
    s.append('</svg>')
    return "".join(s)


# ---------------------------------------------------------------- 3. the rule finder
T3 = "How the rule finder works"
D3 = ("340 solved problems go in. For each answer digit the program finds the smallest set of inputs that decides it, "
      "finds that the tens digit reuses the units rule plus a carry, and compiles the rules into lookup tables.")
EXAMPLES = ["38 + 47 = 85", "16 + 29 = 45", "52 + 31 = 83", "..."]
TABLE = ["8, 7 → 5, carry 1", "6, 9 → 5, carry 1", "2, 1 → 3, carry 0", "..."]
MID = ["units digit ← the two units digits", "tens digit ← the two tens digits", "+ carry from the units"]
NOTE3 = "The units rule, reused one place up"


def finder_wide():
    s = [f'<svg class="dg dg-wide" viewBox="0 0 1000 220" aria-labelledby="dg3-t dg3-d">',
         f'<title id="dg3-t">{T3}</title><desc id="dg3-d">{D3}</desc>', defs(5)]
    s.append('<rect class="box" x="4" y="10" width="230" height="200"/>')
    s.append('<text class="gt" x="20" y="40">340 solved problems</text>')
    s += [f'<text class="lbl" x="20" y="{78+j*28}">{t}</text>' for j, t in enumerate(EXAMPLES)]
    s.append('<line class="spine" x1="236" y1="110" x2="276" y2="110" marker-end="url(#ah5)"/>')
    s.append('<rect class="box" x="280" y="10" width="440" height="200"/>')
    s.append('<text class="gt" x="296" y="40">Smallest inputs per answer digit</text>')
    s.append(f'<text class="lbl" x="296" y="82">{MID[0]}</text>')
    s.append(f'<text class="lbl" x="296" y="116">{MID[1]}</text>')
    s.append(f'<text class="lbl" x="296" y="140">{MID[2]}</text>')
    s.append(f'<text class="small hi" x="296" y="184">{NOTE3}</text>')
    s.append('<line class="spine" x1="722" y1="110" x2="760" y2="110" marker-end="url(#ah5)"/>')
    s.append('<rect class="graft" x="764" y="10" width="232" height="200"/>')
    s.append('<text class="gt" x="780" y="40">Lookup tables</text>')
    s += [f'<text class="lbl" x="780" y="{78+j*28}">{t}</text>' for j, t in enumerate(TABLE)]
    s.append('</svg>')
    return "".join(s)


def finder_narrow():
    s = [f'<svg class="dg dg-narrow" viewBox="0 0 360 572" aria-labelledby="dg3n-t dg3n-d">',
         f'<title id="dg3n-t">{T3}</title><desc id="dg3n-d">{D3}</desc>', defs(6)]
    s.append('<rect class="box" x="4" y="4" width="352" height="150"/>')
    s.append('<text class="gt" x="18" y="32">340 solved problems</text>')
    s += [f'<text class="lbl" x="18" y="{62+j*24}">{t}</text>' for j, t in enumerate(EXAMPLES)]
    s.append('<line class="spine" x1="180" y1="156" x2="180" y2="180" marker-end="url(#ah6)"/>')
    s.append('<rect class="box" x="4" y="184" width="352" height="184"/>')
    s.append('<text class="gt" x="18" y="212">Smallest inputs per answer digit</text>')
    s.append(f'<text class="lbl" x="18" y="248">{MID[0]}</text>')
    s.append(f'<text class="lbl" x="18" y="282">{MID[1]}</text>')
    s.append(f'<text class="lbl" x="18" y="304">{MID[2]}</text>')
    s.append(f'<text class="small hi" x="18" y="346">{NOTE3}</text>')
    s.append('<line class="spine" x1="180" y1="370" x2="180" y2="394" marker-end="url(#ah6)"/>')
    s.append('<rect class="graft" x="4" y="398" width="352" height="168"/>')
    s.append('<text class="gt" x="18" y="426">Lookup tables</text>')
    s += [f'<text class="lbl" x="18" y="{458+j*24}">{t}</text>' for j, t in enumerate(TABLE)]
    s.append('</svg>')
    return "".join(s)


# ---------------------------------------------------------------- 4. where the digits live
def scan_chart():
    d = json.loads(SCAN.read_text())
    vals = [d["layers"][str(i)]["all_six"] for i in range(30)]
    j15 = d["best three [21, 14, 20] fit1500"]["all_six"]
    j30 = d["best three [21, 14, 20] fit3000"]["all_six"]
    cols = []
    for i, v in enumerate(vals):
        hot = ' class="hot"' if i in (14, 20, 21) else ''
        lab = f'<span>{i}</span>' if i in (0, 5, 10, 14, 20, 25, 29) else ''
        cols.append(f'<div{hot} style="--v:{v}"><i></i>{lab}</div>')
    rows = "".join(f'<tr><td>{i}</td><td>{v}%</td></tr>' for i, v in enumerate(vals))
    return f'''<figure class="chart scan">
    <figcaption>Where the digits live</figcaption>
    <p class="sub">Three-digit addition. Share of fresh problems where a linear read gets all six digits of the two numbers right, reading one layer at a time, then layers 14, 20 and 21 joined. Each read is fit on 1,500 problems.</p>
    <div class="sc" aria-hidden="true">
      <div class="sc-cols">{"".join(cols)}</div>
      <div class="sc-join"><div style="--v:{j15}"><i></i><span>14+20+21</span></div></div>
    </div>
    <div class="sc-keys">
      <p><b>{vals[21]}%</b> Best single layer, layer 21</p>
      <p><b>{vals[29]}%</b> Last layer, layer 29</p>
      <p class="win"><b>{j15}%</b> Layers 14, 20 and 21 joined, and {j30}% when that read is fit on 3,000 problems</p>
    </div>
    <details class="sc-table"><summary>All 30 layers as a table</summary>
      <table><thead><tr><th scope="col">Layer</th><th scope="col">All six digits right</th></tr></thead><tbody>{rows}</tbody></table>
    </details>
  </figure>'''


FIG = {
    "hero": lambda: f'''<figure class="diagram hero-fig">
    {hero_wide()}
    {hero_narrow()}
    <figcaption>Where the graft sits. SmolLM2-135M has 30 layers, each an attention block (9 heads) followed by an MLP block, working on a hidden state 576 numbers wide, about 134.5M weights in all. The graft is a small circuit added beside the layers, like a bypass. None of the original neurons or weights change.</figcaption>
    <ol class="dg-key">
      <li>The read and both switches tap the hidden state at the input of layer 20's MLP, at the position where the model is about to write its next answer digit.</li>
      <li>The graft's push is added to the MLP output of layer 29, the last layer, at that same position, just before the output head picks the next token.</li>
      <li>For three-digit addition the read also joins layers 14 and 21 (1,728 numbers in all). The write still goes in at the last layer.</li>
    </ol>
  </figure>''',
    "inside": lambda: f'''<figure class="diagram">
    {inside_wide()}
    {inside_narrow()}
    <figcaption>Inside the graft, with 38 + 47 as an illustration. The read finds 3, 8, 4 and 7, and that two answer digits are left. The rules give 8 + 7 = 15, so the units digit is 5 with a carry of 1, and the tens digit is 3 + 4 + 1 = 8. At the first answer position the graft pushes 8, and at the next it pushes 5. The push is scaled for each digit place. Two switches multiply the push, so it is only on while the model writes the answer to this kind of problem. The model still writes its own reply.</figcaption>
  </figure>''',
    "finder": lambda: f'''<figure class="diagram">
    {finder_wide()}
    {finder_narrow()}
    <figcaption>The rule finder. It gets 340 solved problems as digits and answers. For each answer digit it finds the smallest set of inputs that decides it: the units digit depends only on the two units digits. It finds that the tens digit reuses the units rule plus a carry, and compiles the rules into lookup tables. The example rows are for illustration.</figcaption>
  </figure>''',
    "scan": scan_chart,
}


def main():
    s = PAGE.read_text(encoding="utf-8")
    for name, fn in FIG.items():
        pat = re.compile(rf"(<!-- dg:{name}:start -->).*?(<!-- dg:{name}:end -->)", re.S)
        assert pat.search(s), name
        body = fn()
        s = pat.sub(lambda m: m.group(1) + "\n  " + body + "\n  " + m.group(2), s)
    PAGE.write_text(s, encoding="utf-8")
    print("diagrams written")


if __name__ == "__main__":
    main()
