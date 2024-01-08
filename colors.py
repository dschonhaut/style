"""
formatting.py

Author
------
Daniel Schonhaut
Computational Memory Lab
University of Pennsylvania
daniel.schonhaut@gmail.com

Description
-----------
Functions for standardizing plot formatting and colors.

Last Edited
-----------
3/31/22
"""
from collections import OrderedDict as od
from pandas import Series


def get_colors(palette=None):
    """Return color and color palette dictionaries.
    Parameters
    ----------
    palette : str
        Options are:
        - economist_classic
        - economist_new

    Returns
    -------
    colors : Series
        Dictionary of individual colors.
    palettes : Series
        Dictionary of color palettes, each composed
        of a sequence of colors defined in the colors
        dictionary.
    """
    # Define colors.
    if palette == "economist_classic":
        colors = od(
            [
                ("red", "#E3120B"),
                ("blue", "#006BA2"),
                ("cyan", "#3EBCD2"),
                ("light_green", "#86E5D4"),
                ("yellow", "#EBB434"),
                ("green", "#379A8B"),
                ("dark_cyan", "#005F73"),
                ("plum", "#973C4C"),
                ("light_plum", "#AC8B96"),
                ("purple6", "#78405F"),
                ("purple5", "#925977"),
                ("purple4", "#AD7291"),
                ("purple3", "#C98CAC"),
                ("purple2", "#E6A6C7"),
                ("purple1", "#FFC2E3"),
                ("olive1", "#D7DB5A"),
                ("olive2", "#BAC03F"),
                ("olive3", "#9DA521"),
                ("olive4", "#818A00"),
                ("olive5", "#667100"),
                ("olive6", "#4C5900"),
                ("green6", "#005F52"),
                ("green5", "#00786B"),
                ("green4", "#2E9284"),
                ("green3", "#4DAD9E"),
                ("green2", "#69C9B9"),
                ("green1", "#86E5D4"),
                ("gold1", "#F2CF9A"),
                ("gold2", "#D5B480"),
                ("gold3", "#B99966"),
                ("gold4", "#9D7F4E"),
                ("gold5", "#826636"),
                ("gold6", "#674E1F"),
                ("cyan6", "#005F73"),
                ("cyan5", "#00788D"),
                ("cyan4", "#0092A7"),
                ("cyan3", "#25ADC2"),
                ("cyan2", "#4EC8DE"),
                ("cyan1", "#6FE4FB"),
                ("red1", "#FFA39F"),
                ("red2", "#FF8785"),
                ("red3", "#FF6B6C"),
                ("red4", "#E64E53"),
                ("red5", "#C7303C"),
                ("red6", "#A81829"),
                ("blue1", "#98DAFF"),
                ("blue2", "#7BBFFC"),
                ("blue3", "#5DA4DF"),
                ("blue4", "#3D89C3"),
                ("blue5", "#1270A8"),
                ("blue6", "#00588D"),
                ("black", "#000000"),
                ("gray4", "#3F5661"),
                ("gray3", "#758D99"),
                ("gray2", "#B7C6CF"),
                ("gray1", "#E9EDF0"),
                ("white", "#FFFFFF"),
            ]
        )
        color_aliases = od(
            [
                ("red", "r"),
                ("blue", "b"),
                ("cyan", "c"),
                ("light_green", "lg"),
                ("yellow", "y"),
                ("green", "g"),
                ("dark_cyan", "dc"),
                ("plum", "m"),
                ("light_plum", "lm"),
                ("purple6", "p6"),
                ("purple5", "p5"),
                ("purple4", "p4"),
                ("purple3", "p3"),
                ("purple2", "p2"),
                ("purple1", "p1"),
                ("olive1", "o1"),
                ("olive2", "o2"),
                ("olive3", "o3"),
                ("olive4", "o4"),
                ("olive5", "o5"),
                ("olive6", "o6"),
                ("green6", "g6"),
                ("green5", "g5"),
                ("green4", "g4"),
                ("green3", "g3"),
                ("green2", "g2"),
                ("green1", "g1"),
                ("gold1", "a1"),
                ("gold2", "a2"),
                ("gold3", "a3"),
                ("gold4", "a4"),
                ("gold5", "a5"),
                ("gold6", "a6"),
                ("cyan6", "c6"),
                ("cyan5", "c5"),
                ("cyan4", "c4"),
                ("cyan3", "c3"),
                ("cyan2", "c2"),
                ("cyan1", "c1"),
                ("red1", "r1"),
                ("red2", "r2"),
                ("red3", "r3"),
                ("red4", "r4"),
                ("red5", "r5"),
                ("red6", "r6"),
                ("black", "k"),
                ("gray4", "x4"),
                ("gray3", "x3"),
                ("gray2", "x2"),
                ("gray1", "x1"),
                ("white", "w"),
            ]
        )
        for color, alias in color_aliases.items():
            colors[alias] = colors[color]

        # Define color palettes.
        palettes = od(
            [
                (
                    "economist",
                    (
                        colors["blue"],
                        colors["cyan"],
                        colors["light_green"],
                        colors["yellow"],
                        colors["green"],
                        colors["dark_cyan"],
                        colors["plum"],
                        colors["light_plum"],
                    ),
                ),
                (
                    "po",
                    (
                        colors["purple6"],
                        colors["purple5"],
                        colors["purple4"],
                        colors["purple3"],
                        colors["purple2"],
                        colors["purple1"],
                        colors["olive1"],
                        colors["olive2"],
                        colors["olive3"],
                        colors["olive4"],
                        colors["olive5"],
                        colors["olive6"],
                    ),
                ),
                (
                    "op",
                    (
                        colors["olive6"],
                        colors["olive5"],
                        colors["olive4"],
                        colors["olive3"],
                        colors["olive2"],
                        colors["olive1"],
                        colors["purple1"],
                        colors["purple2"],
                        colors["purple3"],
                        colors["purple4"],
                        colors["purple5"],
                        colors["purple6"],
                    ),
                ),
                (
                    "ga",
                    (
                        colors["green6"],
                        colors["green5"],
                        colors["green4"],
                        colors["green3"],
                        colors["green2"],
                        colors["green1"],
                        colors["gold1"],
                        colors["gold2"],
                        colors["gold3"],
                        colors["gold4"],
                        colors["gold5"],
                        colors["gold6"],
                    ),
                ),
                (
                    "ag",
                    (
                        colors["gold6"],
                        colors["gold5"],
                        colors["gold4"],
                        colors["gold3"],
                        colors["gold2"],
                        colors["gold1"],
                        colors["green1"],
                        colors["green2"],
                        colors["green3"],
                        colors["green4"],
                        colors["green5"],
                        colors["green6"],
                    ),
                ),
                (
                    "cr",
                    (
                        colors["cyan6"],
                        colors["cyan5"],
                        colors["cyan4"],
                        colors["cyan3"],
                        colors["cyan2"],
                        colors["cyan1"],
                        colors["red1"],
                        colors["red2"],
                        colors["red3"],
                        colors["red4"],
                        colors["red5"],
                        colors["red6"],
                    ),
                ),
                (
                    "rc",
                    (
                        colors["red6"],
                        colors["red5"],
                        colors["red4"],
                        colors["red3"],
                        colors["red2"],
                        colors["red1"],
                        colors["cyan1"],
                        colors["cyan2"],
                        colors["cyan3"],
                        colors["cyan4"],
                        colors["cyan5"],
                        colors["cyan6"],
                    ),
                ),
                (
                    "kw",
                    (
                        colors["black"],
                        colors["gray4"],
                        colors["gray3"],
                        colors["gray2"],
                        colors["gray1"],
                        colors["white"],
                    ),
                ),
                (
                    "wk",
                    (
                        colors["white"],
                        colors["gray1"],
                        colors["gray2"],
                        colors["gray3"],
                        colors["gray4"],
                        colors["black"],
                    ),
                ),
            ]
        )

    elif palette == "economist_new":
        colors = {
            "blue3": "#141F52",
            "blue2": "#2E45B8",
            "blue1": "#D6DBF5",
            "red3": "#861320",
            "red2": "#E3120B",
            "red1": "#FFA39F",
            "cyan3": "#005F73",
            "cyan2": "#3EBCD2",
            "cyan1": "#6FE4FB",
            "green3": "#0E6452",
            "green2": "#1DC9A4",
            "green1": "#D2F9F0",
            "orange2": "#F97A1F",
            "orange1": "#FCB583",
            "yellow2": "#F9C31F",
            "yellow1": "#FCDE83",
            "beige1": "#E1DFD0",
            "teal1": "#D0E1E1",
            "black": "#000000",
            "gray5": "#333333",
            "gray4": "#595959",
            "gray3": "#B3B3B3",
            "gray2": "#D9D9D9",
            "gray1": "#F2F2F2",
            "white": "#FFFFFF",
        }
        color_aliases = od(
            [
                ("blue3", "b3"),
                ("blue2", "b2"),
                ("blue1", "b1"),
                ("red3", "r3"),
                ("red2", "r2"),
                ("red1", "r1"),
                ("cyan3", "c3"),
                ("cyan2", "c2"),
                ("cyan1", "c1"),
                ("green3", "g3"),
                ("green2", "g2"),
                ("green1", "g1"),
                ("orange2", "o2"),
                ("orange1", "o1"),
                ("yellow2", "y2"),
                ("yellow1", "y1"),
                ("beige1", "be1"),
                ("teal1", "t1"),
                ("black", "k"),
                ("gray4", "x5"),
                ("gray4", "x4"),
                ("gray3", "x3"),
                ("gray2", "x2"),
                ("gray1", "x1"),
                ("white", "w"),
            ]
        )
        for color, alias in color_aliases.items():
            colors[alias] = colors[color]

        # Define color palettes.
        palettes = od(
            [
                (
                    "economist16",
                    (
                        colors["blue3"],
                        colors["blue2"],
                        colors["blue1"],
                        colors["red3"],
                        colors["red2"],
                        colors["red1"],
                        colors["cyan3"],
                        colors["cyan2"],
                        colors["cyan1"],
                        colors["green3"],
                        colors["green2"],
                        colors["green1"],
                        colors["orange2"],
                        colors["orange1"],
                        colors["yellow2"],
                        colors["yellow1"],
                    ),
                ),
                (
                    "economist16b",
                    (
                        colors["blue2"],
                        colors["red2"],
                        colors["cyan2"],
                        colors["green2"],
                        colors["orange2"],
                        colors["yellow2"],
                        colors["blue3"],
                        colors["red3"],
                        colors["cyan3"],
                        colors["green3"],
                        colors["blue1"],
                        colors["red1"],
                        colors["cyan1"],
                        colors["green1"],
                        colors["orange1"],
                        colors["yellow1"],
                    ),
                ),
                (
                    "wk",
                    (
                        colors["white"],
                        colors["gray1"],
                        colors["gray2"],
                        colors["gray3"],
                        colors["gray4"],
                        colors["gray5"],
                        colors["black"],
                    ),
                ),
            ]
        )
    elif palette is None:
        colors = {
            "blue1": "#ABB4E2",  # "#D6DBF5",
            "blue2": "#2E45B8",
            "blue3": "#141F52",
            "cyan1": "#B1E4ED",  # "#6FE4FB",
            "cyan2": "#3EBCD2",
            "cyan3": "#005F73",
            "green1": "#7EC98B",  # "#D2F9F0",
            "green2": "#29A53E",  # "#1DC9A4",
            "green3": "#196726",  # "#0E6452",
            "yellow1": "#FCDE83",
            "yellow2": "#F9C31F",
            "yellow3": "#A58200",  # "#CFA300",
            "orange1": "#FCB583",
            "orange2": "#F97A1F",
            "orange3": "#C75400",
            "red1": "#FFA39F",
            "red2": "#E3120B",
            "red3": "#861320",
            "pink1": "#FFA4C2",
            "pink2": "#FF4983",
            "pink3": "#A80055",
            "violet1": "#BEAAE3",  # "#E6D4FA",
            "violet2": "#7D55C7",  # "#B38FE7",
            "violet3": "#4B3377",  # "#7D55C7",
            "white": "#FFFFFF",
            "gray1": "#F2F2F2",
            "gray2": "#D9D9D9",
            "gray3": "#B3B3B3",
            "gray4": "#595959",
            "gray5": "#333333",
            "gray6": "#1A1A1A",
            "black": "#000000",
        }
        color_aliases = od(
            [
                ("b", "blue2"),
                ("c", "cyan2"),
                ("g", "green2"),
                ("y", "yellow2"),
                ("o", "orange2"),
                ("r", "red2"),
                ("p", "pink2"),
                ("v", "violet2"),
                ("b1", "blue1"),
                ("b2", "blue2"),
                ("b3", "blue3"),
                ("c1", "cyan1"),
                ("c2", "cyan2"),
                ("c3", "cyan3"),
                ("g1", "green1"),
                ("g2", "green2"),
                ("g3", "green3"),
                ("y1", "yellow1"),
                ("y2", "yellow2"),
                ("y3", "yellow3"),
                ("o1", "orange1"),
                ("o2", "orange2"),
                ("o3", "orange3"),
                ("r1", "red1"),
                ("r2", "red2"),
                ("r3", "red3"),
                ("p1", "pink1"),
                ("p2", "pink2"),
                ("p3", "pink3"),
                ("v1", "violet1"),
                ("v2", "violet2"),
                ("v3", "violet3"),
                ("w", "white"),
                ("x1", "gray1"),
                ("x2", "gray2"),
                ("x3", "gray3"),
                ("x4", "gray4"),
                ("x5", "gray5"),
                ("x6", "gray6"),
                ("k", "black"),
            ]
        )

        for alias, color in color_aliases.items():
            colors[alias] = colors[color]

        # Define color palettes.
        # pal24 <- c(blue2, orange2, cyan2, rose2, green2, violet2, yellow2, beige2,
        #    blue3, orange3, cyan3, rose3, green3, violet3, yellow3, beige3,
        #    blue1, orange1, cyan1, rose1, green1, violet1, yellow1, beige1
        #    )
        _palettes = od(
            [
                (
                    "pal8",
                    [
                        "b2",
                        "o2",
                        "c2",
                        "p2",
                        "g2",
                        "v2",
                        "y2",
                        "r2",
                    ],
                ),
                (
                    "pal24",
                    [
                        "b2",
                        "o2",
                        "c2",
                        "p2",
                        "g2",
                        "v2",
                        "y2",
                        "r2",
                        "b3",
                        "o3",
                        "c3",
                        "p3",
                        "g3",
                        "v3",
                        "y3",
                        "r3",
                        "b1",
                        "o1",
                        "c1",
                        "p1",
                        "g1",
                        "v1",
                        "y1",
                        "r1",
                    ],
                ),
                (
                    "pal24b",
                    [
                        "b3",
                        "b2",
                        "b1",
                        "o3",
                        "o2",
                        "o1",
                        "c3",
                        "c2",
                        "c1",
                        "g3",
                        "g2",
                        "g1",
                        "p3",
                        "p2",
                        "p1",
                        "v3",
                        "v2",
                        "v1",
                        "y3",
                        "y2",
                        "y1",
                        "r3",
                        "r2",
                        "r1",
                    ],
                ),
            ]
        )
        palettes = od([])
        for k, v in _palettes.items():
            palettes[k] = [colors[c] for c in v]

    colors = Series(colors, name="code")
    palettes = Series(palettes, name="colors")

    return colors, palettes
