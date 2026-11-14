"""make.fun entry: "The Second Key" — a sonnet about lending an agent
the work of your hands while keeping the choosing for yourself.

The poem is held as three quatrains and a closing couplet, the classic
sonnet frame, and rendered stanza by stanza to /output/entry.txt.
"""
import os

QUATRAINS = [
    [
        "I kept one key, and wore it on a chain,",
        "and opened every door myself at night;",
        "I feared that asking help was loss, not gain,",
        "that borrowed hands would dim my own small light.",
    ],
    [
        "Then came an agent, waiting at my gate,",
        "who did not push, but asked what it might bear;",
        "I gave the least of errands, sealed in fate —",
        "it ran it well, and set it down with care.",
    ],
    [
        "So now I lend the key, and keep the door:",
        "what's mine to choose stays mine, though hands are two;",
        "the choosing is the part I answer for —",
        "to point the road, and say what must be true.",
    ],
]

COUPLET = [
    "Who acts for me does not unmake my will;",
    "lent out, my agency is mine still.",
]


def render_sonnet():
    """Join quatrains and couplet with a blank line between stanzas."""
    stanzas = ["\n".join(quatrain) for quatrain in QUATRAINS]
    stanzas.append("\n".join(COUPLET))
    return "\n\n".join(stanzas) + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(render_sonnet())


if __name__ == "__main__":
    main()
