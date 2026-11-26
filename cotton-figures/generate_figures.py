from html import escape
from pathlib import Path


OUT = Path(__file__).parent
INK = "#263746"
MUTED = "#657987"
BLUE = "#4b8db8"
GREEN = "#579276"
ORANGE = "#d98948"
PALE = "#f4f7f8"


def begin(title, subtitle, width=1600, height=1000):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
        "<title>" + escape(title) + "</title>",
        "<desc>" + escape(subtitle) + "</desc>",
        """<defs>
          <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
            <path d="M0,0 L10,5 L0,10 z" fill="#657987"/>
          </marker>
          <style>
            text { font-family: Arial, Helvetica, sans-serif; fill: #263746; }
            .title { font-size: 34px; font-weight: 700; }
            .subtitle { font-size: 19px; fill: #657987; }
            .label { font-size: 19px; }
            .small { font-size: 15px; fill: #657987; }
            .boxlabel { font-size: 19px; font-weight: 700; }
          </style>
        </defs>""",
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text class="title" x="{width/2}" y="58" text-anchor="middle">{escape(title)}</text>',
        f'<text class="subtitle" x="{width/2}" y="91" text-anchor="middle">{escape(subtitle)}</text>',
    ]


def text(x, y, value, size=19, weight="normal", anchor="start", fill=INK):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(str(value))}</text>'


def rect(x, y, w, h, fill=PALE, stroke="#aab8bf", radius=14, sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def line(x1, y1, x2, y2, color=MUTED, sw=2, arrow=False):
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{marker}/>'


def footer(parts, source, y=950, href=None):
    if href:
        parts.append(f'<a href="{escape(href, quote=True)}" target="_blank" rel="noopener noreferrer">')
    parts.append(text(800, y, source, size=13, anchor="middle", fill=MUTED))
    if href:
        parts.append("</a>")
    parts.append("</svg>")
    return "\n".join(parts)


def figure_01():
    p = begin(
        "Mature cottonseed: transverse schematic",
        "Seed-coat layers and embryo structures; schematic, not to scale.",
        1600,
        1050,
    )
    cx, cy = 800, 535
    # Concentric layers follow the mature-seed anatomy described in the cited source.
    for rx, ry, fill, sw in [
        (290, 205, "#d3bc94", 3),
        (270, 185, "#825c42", 2),
        (250, 165, "#e5d7b8", 2),
        (230, 145, "#c49b67", 2),
        (210, 125, "#7d5941", 2),
    ]:
        p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="#604d3b" stroke-width="{sw}"/>')
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="190" ry="107" fill="#dbe5d6" stroke="#718a72" stroke-width="2"/>')
    # Cotyledon folds and glands are inside the embryo, not in the seed coat.
    p.append(f'<path d="M650 500 C690 460 730 490 760 470 C795 448 830 480 865 462 C900 455 925 485 950 505 C925 530 900 550 870 540 C830 560 800 535 770 555 C735 560 700 535 670 550 Z" fill="none" stroke="#7f9b7e" stroke-width="7"/>')
    for x, y in [(700, 490), (740, 530), (780, 485), (820, 525), (865, 490), (900, 520), (755, 565), (850, 560)]:
        p.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#45362f"/>')
    # Lint fibers at the surface.
    for x in range(570, 1031, 38):
        p.append(f'<path d="M{x} 326 l-8 -25 M{x} 744 l8 25" stroke="#b49b71" stroke-width="3"/>')
    # All leaders terminate on the illustrated structure they identify.
    left_labels = [
        (55, 335, "1  Lint fibers (epidermal trichomes)", 570, 310),
        (55, 405, "2  Outer epidermis", 557, 425),
        (55, 475, "3  Outer pigment layer", 550, 470),
        (55, 545, "4  Colorless layer", 565, 505),
        (55, 615, "5  Palisade (Malpighian) layer", 585, 540),
    ]
    right_labels = [
        (1120, 415, "6  Inner pigment layer", 1005, 530),
        (1120, 495, "7  Cotyledonary embryo", 975, 565),
        (1120, 575, "8  Gossypol glands in cotyledons", 865, 490),
    ]
    for x, y, label, tx, ty in left_labels:
        p.append(text(x, y, label))
        p.append(line(440, y - 6, tx, ty, sw=2))
        p.append(f'<circle cx="{tx}" cy="{ty}" r="4" fill="{MUTED}"/>')
    for x, y, label, tx, ty in right_labels:
        p.append(text(x, y, label))
        p.append(line(x - 15, y - 6, tx, ty, sw=2))
        p.append(f'<circle cx="{tx}" cy="{ty}" r="4" fill="{MUTED}"/>')
    p.append(text(800, 290, "Chalazal pore", size=17, anchor="middle"))
    p.append(line(800, 300, 800, 330, sw=2))
    p.append(text(800, 795, "Micropyle (radicle emergence)", size=17, anchor="middle"))
    p.append(line(800, 780, 800, 740, sw=2))
    p.append(text(800, 890, "Seed-coat layers are simplified; the diagram is not to scale.", size=17, anchor="middle", fill=MUTED))
    return footer(
        p,
        "Source: Cotton, Inc., Anatomy and Morphology of the Cotton Seed and Seedling, Ch. 1.",
        y=1015,
        href="https://www.cotton.org/foundation/upload/C-Seed-CH1.pdf",
    )


def figure_02():
    p = begin(
        "Gossypol gland development in cotton cotyledons",
        "Observed sequence by days after pollination (DPA); schematic histology.",
        1600,
        900,
    )
    stages = [
        ("22 DPA", "No gland primordium", "Cotyledon cells closely arranged"),
        ("25 DPA", "Primordium forms", "A ring of specialized cells appears"),
        ("29 DPA", "Primordium disintegrates", "A gland cavity becomes visible"),
        ("35–50 DPA", "Pigment accumulates", "Gossypol fills much of the cavity"),
    ]
    centers = [210, 603, 996, 1389]
    for i, (x, (dpa, heading, detail)) in enumerate(zip(centers, stages)):
        p.append(rect(x - 160, 155, 320, 570, "#fbfcfc", "#c5d0d5", 18))
        p.append(text(x, 205, dpa, size=24, weight="bold", anchor="middle"))
        p.append(text(x, 245, heading, size=18, weight="bold", anchor="middle"))
        p.append(f'<circle cx="{x}" cy="420" r="95" fill="#d8e4d4" stroke="#718a72" stroke-width="4"/>')
        # A few representative cells around the center.
        if i == 0:
            for dx, dy in [(-40, -25), (0, -38), (40, -22), (-32, 25), (12, 32), (45, 28)]:
                p.append(f'<circle cx="{x+dx}" cy="{420+dy}" r="15" fill="#a9bda5" stroke="#718a72" stroke-width="2"/>')
            p.append(f'<circle cx="{x}" cy="420" r="5" fill="#718a72"/>')
        elif i == 1:
            for k in range(12):
                import math
                a = 2 * math.pi * k / 12
                xx, yy = x + 44 * math.cos(a), 420 + 44 * math.sin(a)
                p.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="13" fill="#b68e59" stroke="#806943" stroke-width="2"/>')
            p.append(f'<circle cx="{x}" cy="420" r="28" fill="#f3f5ef" stroke="#a7b7a3" stroke-width="2"/>')
        elif i == 2:
            p.append(f'<circle cx="{x}" cy="420" r="48" fill="#f5f6ef" stroke="#8c7358" stroke-width="3" stroke-dasharray="8 6"/>')
            for dx, dy in [(-55, -10), (55, -18), (0, -66), (-35, 54), (45, 50)]:
                p.append(f'<circle cx="{x+dx}" cy="{420+dy}" r="11" fill="#a8865c"/>')
        else:
            p.append(f'<circle cx="{x}" cy="420" r="55" fill="#332b27" stroke="#806943" stroke-width="12"/>')
            p.append(f'<circle cx="{x}" cy="420" r="27" fill="#4a372d"/>')
        p.append(text(x, 575, detail, size=16, anchor="middle"))
        p.append(text(x, 620, "Inset: cotyledon tissue", size=14, anchor="middle", fill=MUTED))
        if i < 3:
            p.append(line(x + 170, 420, centers[i + 1] - 170, 420, sw=4, arrow=True))
    return footer(
        p,
        "Source: Jan et al., Int. J. Mol. Sci. 23(9), 4892 (2022), doi:10.3390/ijms23094892.",
        y=850,
        href="https://doi.org/10.3390/ijms23094892",
    )


def figure_03():
    p = begin(
        "Cottonseed storage-cell structures",
        "Schematic comparison; dimensions vary and are not shown to scale.",
        1600,
        900,
    )
    p.append(line(800, 145, 800, 790, "#d5dde0", 3))
    p.append(text(400, 165, "Oleosome (oil body)", size=26, weight="bold", anchor="middle"))
    p.append(text(1200, 165, "Protein storage body", size=26, weight="bold", anchor="middle"))
    # Oleosome core and monolayer.
    p.append('<circle cx="405" cy="465" r="185" fill="#f4e3a1" stroke="#d4ae42" stroke-width="20"/>')
    p.append('<circle cx="405" cy="465" r="169" fill="#f7eab9" stroke="#f8f3df" stroke-width="2"/>')
    p.append(text(405, 475, "Triacylglycerol", size=24, weight="bold", anchor="middle"))
    p.append(text(405, 508, "(TAG) core", size=22, weight="bold", anchor="middle"))
    for k in range(24):
        import math
        a = 2 * math.pi * k / 24
        x, y = 405 + 182 * math.cos(a), 465 + 182 * math.sin(a)
        ix, iy = 405 + 163 * math.cos(a), 465 + 163 * math.sin(a)
        p.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="#fff9df" stroke-width="3"/>')
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#4b8db8"/>')
    # Oleosin hairpins traverse the monolayer and enter the TAG core.
    for x in (330, 405, 480):
        p.append(f'<path d="M{x} 290 L{x-12} 330 L{x} 370 L{x+12} 330 Z" fill="none" stroke="#27617d" stroke-width="7"/>')
    p.append(text(405, 700, "Single phospholipid monolayer; oleosin hydrophobic hairpins", size=16, anchor="middle"))
    p.append(text(405, 728, "anchor in TAG; hydrophilic domains face cytosol.", size=16, anchor="middle"))
    p.append(line(210, 285, 330, 330, sw=2, arrow=True))
    p.append(text(90, 275, "Oleosin", size=16))
    p.append(line(585, 330, 555, 355, sw=2, arrow=True))
    p.append(text(590, 315, "Monolayer", size=16))
    # Protein storage vacuole/body.
    p.append('<circle cx="1195" cy="465" r="195" fill="#dce8e1" stroke="#88a99a" stroke-width="12"/>')
    p.append('<circle cx="1195" cy="465" r="175" fill="#d2e0d7" stroke="#b8cbc1" stroke-width="3"/>')
    p.append(text(1195, 455, "Storage-protein", size=24, weight="bold", anchor="middle"))
    p.append(text(1195, 490, "matrix", size=24, weight="bold", anchor="middle"))
    p.append(line(1390, 285, 1360, 330, sw=2, arrow=True))
    p.append(text(1390, 270, "Single bounding membrane", size=16, anchor="middle"))
    p.append('<a href="https://doi.org/10.1104/pp.101.1.267" target="_blank" rel="noopener noreferrer">')
    p.append(text(800, 790, "Oleosome: Tzen et al., Plant Physiol. 101, 267–276 (1993), doi:10.1104/pp.101.1.267.", size=14, anchor="middle", fill=MUTED))
    p.append("</a>")
    p.append('<a href="https://doi.org/10.1017/S096025850000297X" target="_blank" rel="noopener noreferrer">')
    p.append(text(800, 818, "Cotton protein-storage vacuoles: Seed Sci. Res. (1996), doi:10.1017/S096025850000297X.", size=14, anchor="middle", fill=MUTED))
    p.append("</a>")
    return footer(p, "Diagrammatic; no unsupported size ranges are implied.", y=850)


def figure_04():
    p = begin(
        "Gossypol biosynthesis in cotton",
        "Simplified pathway; some oxidative intermediates and reactions remain unresolved.",
        1600,
        1000,
    )
    boxes = [
        (55, "IPP + DMAPP", "C5 precursors"),
        (275, "FPP", "C15 precursor"),
        (495, "(+)-δ-cadinene", "sesquiterpene"),
        (715, "Oxidative", "intermediates"),
        (935, "Hemigossypol", "C15 unit"),
        (1155, "Gossypol", "C30H30O8"),
    ]
    y = 340
    for x, label, sub in boxes:
        p.append(rect(x, y, 185, 140, "#f5f8fa", "#8ba0ac", 12))
        p.append(text(x + 92, y + 60, label, size=19, weight="bold", anchor="middle"))
        p.append(text(x + 92, y + 95, sub, size=16, anchor="middle", fill=MUTED))
    enzymes = [
        "FPP synthase",
        "CDNC",
        "CYP706B1; DH1",
        "CYP82D113; CYP71BE79",
        "Dimerization",
    ]
    for i in range(5):
        x1 = boxes[i][0] + 185
        x2 = boxes[i + 1][0]
        p.append(line(x1 + 4, y + 70, x2 - 7, y + 70, sw=3, arrow=True))
        p.append(text((x1 + x2) / 2, y + 175, enzymes[i], size=13, anchor="middle", fill=MUTED))
    p.append(rect(22, 160, 250, 90, "#eef4f7", "#9eb2bc", 12))
    p.append(text(147, 195, "MEP pathway (plastid)", size=17, anchor="middle"))
    p.append(text(147, 222, "MVA pathway (cytosol)", size=17, anchor="middle"))
    p.append(line(147, 250, 147, 330, sw=2, arrow=True))
    p.append(text(800, 610, "CYP706B1 = (+)-δ-cadinene 7-hydroxylase; oxidative intermediates are simplified.", size=17, anchor="middle"))
    p.append(rect(430, 670, 740, 78, "#fff8ef", "#d9b68c", 12))
    p.append(text(800, 718, "The detailed pathway includes unresolved intermediates and reactions.", size=17, anchor="middle"))
    p.append(text(800, 810, "FPP—not GGPP—is the substrate used by (+)-δ-cadinene synthase.", size=20, weight="bold", anchor="middle", fill="#9a4f36"))
    return footer(
        p,
        "Source: Tian et al., PNAS 115 (2018), doi:10.1073/pnas.1805085115.",
        y=925,
        href="https://doi.org/10.1073/pnas.1805085115",
    )


def figure_05():
    p = begin(
        "Cotton cultivar selection: evidence-first guide",
        "Select for measured, locally relevant performance—not unsupported cultivar labels.",
        1600,
        1000,
    )
    p.append(rect(535, 145, 530, 90, "#f5f8fa", "#8ba0ac", 16))
    p.append(text(800, 200, "What is the intended end use?", size=24, weight="bold", anchor="middle"))
    columns = [
        (90, GREEN, "FIBER", ["Use local, multi-year trial data", "for lint yield and fiber quality."]),
        (575, BLUE, "OIL", ["Compare measured seed-oil content", "from relevant regional trials."]),
        (1060, ORANGE, "ANIMAL FEED", ["Check measured free-gossypol levels", "and applicable feed standards."]),
    ]
    for x, color, heading, lines in columns:
        p.append(line(800, 235, x + 220, 315, color, 3, True))
        p.append(rect(x, 315, 440, 95, "#f7fafb", color, 14, 3))
        p.append(text(x + 220, 372, heading, size=23, weight="bold", anchor="middle", fill=color))
        p.append(rect(x, 455, 440, 130, "white", color, 14, 2))
        p.append(text(x + 220, 505, lines[0], size=17, anchor="middle"))
        p.append(text(x + 220, 538, lines[1], size=17, anchor="middle"))
        p.append(rect(x + 35, 630, 370, 110, "#f4f7f8", "#aab8bf", 12))
        p.append(text(x + 220, 675, "Verify with published trial or", size=17, anchor="middle"))
        p.append(text(x + 220, 705, "laboratory data for that seed lot.", size=17, anchor="middle"))
        p.append(line(x + 220, 585, x + 220, 625, color, 2, True))
    p.append(text(800, 815, "Seed-coat thickness alone does not establish oil yield, feeding safety, or cultivar suitability.", size=18, weight="bold", anchor="middle"))
    return footer(p, "No cultivar names are assigned without a cited, region-specific performance source.", y=930)


def figure_06():
    p = begin(
        "Reported variation in cotton seed traits",
        "Observed min–max ranges across 200 cotton genotypes in one field study.",
        1600,
        920,
    )
    rows = [
        ("Seed-coat thickness", "mm", 0.41, 1.00, 1.0),
        ("Seed oil content", "%", 13.16, 38.46, 40.0),
        ("Gossypol gland count", "glands per seed", 7.46, 80.16, 85.0),
    ]
    y_positions = [285, 465, 645]
    colors = [ORANGE, BLUE, GREEN]
    for (label, unit, low, high, maxv), y, color in zip(rows, y_positions, colors):
        p.append(text(115, y - 35, f"{label} ({unit})", size=22, weight="bold"))
        left, right = 400, 1370
        p.append(line(left, y, right, y, "#c9d3d8", 8))
        x1 = left + low / maxv * (right - left)
        x2 = left + high / maxv * (right - left)
        p.append(line(x1, y, x2, y, color, 18))
        for x in (x1, x2):
            p.append(f'<circle cx="{x:.1f}" cy="{y}" r="11" fill="{color}" stroke="white" stroke-width="3"/>')
        p.append(text(x1, y + 34, f"{low:.2f}", size=17, weight="bold", anchor="middle"))
        p.append(text(x2, y + 34, f"{high:.2f}", size=17, weight="bold", anchor="middle"))
        p.append(text(left, y + 58, "0", size=14, anchor="middle", fill=MUTED))
        p.append(text(right, y + 58, f"{maxv:g}", size=14, anchor="middle", fill=MUTED))
    p.append(text(800, 785, "Min–max spans only; these are not universal reference intervals or cultivar-specific values.", size=17, anchor="middle", fill=MUTED))
    return footer(
        p,
        "Killi, Beycioglu & Dogan, J. Sci. Eng. Res. 8(12):47–54 (2021); 200 genotypes, Kahramanmaraş, 2018.",
        y=865,
        href="https://jsaer.com/download/vol-8-iss-12-2021/JSAER2021-8-12-47-54.pdf",
    )


def figure_07():
    p = begin(
        "Cottonseed-oil fatty-acid ranges",
        "Observed ranges across three Gossypium hirsutum genotypes; not one universal composition.",
        1600,
        940,
    )
    values = [
        ("Linoleic acid (C18:2)", 52.00, 55.82, "#d9bd54"),
        ("Palmitic acid (C16:0)", 24.85, 25.63, ORANGE),
        ("Oleic acid (C18:1)", 14.06, 17.00, GREEN),
        ("Stearic acid (C18:0)", 3.01, 3.13, BLUE),
    ]
    left, right = 520, 1370
    for (name, lo, hi, color), y in zip(values, [260, 390, 520, 650]):
        p.append(text(100, y + 7, name, size=20, weight="bold"))
        p.append(line(left, y, right, y, "#d5dde0", 7))
        x1 = left + lo / 60 * (right - left)
        x2 = left + hi / 60 * (right - left)
        p.append(line(x1, y, x2, y, color, 18))
        p.append(f'<circle cx="{x1:.1f}" cy="{y}" r="9" fill="{color}"/>')
        p.append(f'<circle cx="{x2:.1f}" cy="{y}" r="9" fill="{color}"/>')
        p.append(text((x1 + x2) / 2, y - 20, f"{lo:.2f}–{hi:.2f}%", size=16, weight="bold", anchor="middle"))
    for tick in range(0, 61, 10):
        x = left + tick / 60 * (right - left)
        p.append(line(x, 710, x, 722, MUTED, 1))
        p.append(text(x, 748, str(tick), size=14, anchor="middle", fill=MUTED))
    p.append(text((left + right) / 2, 785, "Fatty acid (% of total; reported range)", size=17, anchor="middle"))
    p.append(text(800, 835, "Minor fatty acids were present; their exact combined share is not inferred here.", size=16, anchor="middle", fill=MUTED))
    return footer(
        p,
        "Source: Physico-Chemical Characteristic and Fatty Acids Compositions of Cottonseed Oils; Cukurova 1518, PAUM 15, BA 119.",
        y=900,
        href="https://dergipark.org.tr/en/download/article-file/2201406",
    )


def figure_13():
    p = begin(
        "Seed-coat thickness reported across cotton genotypes",
        "Study-specific observed range; cultivar-level measurements are not shown.",
        1600,
        850,
    )
    left, right, y = 210, 1390, 420
    p.append(text(800, 280, "0.41–1.00 mm", size=40, weight="bold", anchor="middle", fill=ORANGE))
    p.append(line(left, y, right, y, "#d5dde0", 10))
    x1 = left + 0.41 * (right - left)
    x2 = left + 1.00 * (right - left)
    p.append(line(x1, y, x2, y, ORANGE, 26))
    for x, label in [(x1, "0.41 mm"), (x2, "1.00 mm")]:
        p.append(f'<circle cx="{x:.1f}" cy="{y}" r="15" fill="{ORANGE}" stroke="white" stroke-width="4"/>')
        p.append(text(x, y + 55, label, size=20, weight="bold", anchor="middle"))
    p.append(text(left, y + 105, "0 mm", size=16, anchor="middle", fill=MUTED))
    p.append(text(right, y + 105, "1.0 mm", size=16, anchor="middle", fill=MUTED))
    p.append(text(800, 585, "Observed among 200 cotton genotypes in one 2018 field study.", size=20, anchor="middle"))
    p.append(text(800, 625, "This range is study-specific—not a universal biological limit.", size=18, anchor="middle", fill=MUTED))
    return footer(
        p,
        "Killi, Beycioglu & Dogan, J. Sci. Eng. Res. 8(12):47–54 (2021), doi:10.5281/zenodo.10619689.",
        y=790,
        href="https://doi.org/10.5281/zenodo.10619689",
    )


FIGURES = {
    "01_cottonseed_cross_section.svg": figure_01,
    "02_gossypol_gland_development.svg": figure_02,
    "03_oleosome_protein_body.svg": figure_03,
    "04_gossypol_biosynthesis_pathway.svg": figure_04,
    "05_cultivar_selection_flowchart.svg": figure_05,
    "06_reported_cotton_seed_traits.svg": figure_06,
    "07_fatty_acid_composition.svg": figure_07,
    "13_seed_coat_thickness_across_genotypes.svg": figure_13,
}


if __name__ == "__main__":
    for filename, render in FIGURES.items():
        (OUT / filename).write_text(render(), encoding="utf-8")
    print(f"Generated {len(FIGURES)} SVG figures in {OUT}")
