import json
import urllib.parse
import urllib.request
from pathlib import Path

VAULT_PATH = r"C:\Users\lewis\Downloads\CVNLP"

# Structural dataset for 2 Peter sections
SECTIONS = [
    {
        "id": "2 Peter 1:1-4",
        "file_id": "2 Peter 1.1-4",
        "title": "Divine Power and Promises",
        "chapter": 1,
        "summary": "Believers receive everything necessary for life and godliness through knowing Christ, escaping worldly corruption to partake in divine nature.",
        "themes": ["Divine Nature", "Sanctification", "Faith"],
        "cross_refs": ["Titus 2:11-14", "Ephesians 1:3", "Hebrews 12:10"],
    },
    {
        "id": "2 Peter 1:5-11",
        "file_id": "2 Peter 1.5-11",
        "title": "The Ladder of Christian Virtues",
        "chapter": 1,
        "summary": "Supplying faith with virtue, knowledge, self-control, perseverance, godliness, brotherly affection, and love to ensure spiritual fruitfulness.",
        "themes": ["Christian Virtues", "Fruitfulness", "Assurance"],
        "cross_refs": ["Galatians 5:22-23", "Colossians 3:12-14"],
    },
    {
        "id": "2 Peter 1:12-21",
        "file_id": "2 Peter 1.12-21",
        "title": "Apostolic Eyewitness and the Prophetic Word",
        "chapter": 1,
        "summary": "Recalling the Transfiguration and affirming that no prophecy came by human initiative; individuals spoke from God guided by the Holy Spirit.",
        "themes": [
            "Inspiration of Scripture",
            "Eyewitness Testimony",
            "Prophecy",
        ],
        "cross_refs": ["Matthew 17:1-8", "2 Timothy 3:16-17", "Luke 1:70"],
    },
    {
        "id": "2 Peter 2:1-10a",
        "file_id": "2 Peter 2.1-10a",
        "api_ref": "2 Peter 2:1-10",
        "title": "False Teachers and Past Judgments",
        "chapter": 2,
        "summary": "Warnings concerning destructive teachings alongside historic demonstrations of judgment (fallen angels, the flood, Sodom) and rescue (Noah, Lot).",
        "themes": ["False Teachers", "Divine Judgment", "Deliverance"],
        "cross_refs": [
            "Jude 1:4-7",
            "Genesis 6:1-8",
            "Genesis 19:1-29",
            "1 Peter 3:19-20",
        ],
    },
    {
        "id": "2 Peter 2:10b-22",
        "file_id": "2 Peter 2.10b-22",
        "api_ref": "2 Peter 2:11-22",
        "title": "The Character of Apostates",
        "chapter": 2,
        "summary": "Description of deceitful motives, parallels to Balaam's pursuit of gain, and the danger of returning to worldly defilement.",
        "themes": ["Apostasy", "Spiritual Bondage", "Greed"],
        "cross_refs": [
            "Proverbs 26:11",
            "Numbers 22:1-35",
            "Jude 1:11-13",
            "Hebrews 6:4-6",
        ],
    },
    {
        "id": "2 Peter 3:1-7",
        "file_id": "2 Peter 3.1-7",
        "title": "Scoffers in the Last Days",
        "chapter": 3,
        "summary": "Addressing claims that the natural order has remained unchanged since creation, pointing back to the Deluge and forward to fire.",
        "themes": ["Scoffers", "Creation & Deluge", "Parousia & Eschatology"],
        "cross_refs": ["Jude 1:17-19", "Psalm 102:25-27", "2 Thessalonians 1:7-8"],
    },
    {
        "id": "2 Peter 3:8-13",
        "file_id": "2 Peter 3.8-13",
        "title": "The Day of the Lord and Holy Conduct",
        "chapter": 3,
        "summary": "A thousand years as a day; divine patience meant for repentance before the day of dissolution and the arrival of a new heaven and earth.",
        "themes": [
            "Patience of God",
            "Day of the Lord",
            "New Creation",
            "Parousia & Eschatology",
        ],
        "cross_refs": [
            "Psalm 90:4",
            "Isaiah 65:17",
            "1 Thessalonians 5:2",
            "Revelation 21:1",
        ],
    },
    {
        "id": "2 Peter 3:14-18",
        "file_id": "2 Peter 3.14-18",
        "title": "Final Exhortation and Paul's Letters",
        "chapter": 3,
        "summary": "Admonition toward steadfast holiness, acknowledging Paul's letters alongside other writings, and concluding with a call to grow in grace.",
        "themes": ["Canon & Pauline Corpus", "Spiritual Growth", "Steadfastness"],
        "cross_refs": ["Romans 2:4", "1 Thessalonians 4:13-18", "Hebrews 5:12-14"],
    },
]


def fetch_web_scripture(reference: str) -> str:
    """Fetch modern public-domain (World English Bible) text via free REST API."""
    encoded_ref = urllib.parse.quote(reference)
    url = f"https://bible-api.com/{encoded_ref}?translation=web"
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "ObsidianBibleBuilder/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
            verses = payload.get("verses", [])
            if not verses:
                return payload.get("text", "").strip()

            formatted = []
            for v in verses:
                formatted.append(f"> **{v['verse']}** {v['text'].strip()}")
            return "\n>\n".join(formatted)
    except Exception as err:
        return f"> *(Scripture text could not be loaded automatically: {err})*"


def sanitize_filename(name: str) -> str:
    """Make reference strings safe for Windows file paths."""
    return name.replace(":", ".")


def build_obsidian_notes(vault_root: str):
    base = Path(vault_root) / "2 Peter Study"
    passages_dir = base / "Passages"
    themes_dir = base / "Themes"
    xrefs_dir = base / "Cross References"

    for directory in [passages_dir, themes_dir, xrefs_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    theme_to_passages = {}
    xref_to_passages = {}

    print("Building notes and retrieving public-domain scripture text...")

    # 1. Generate Passage Notes
    for item in SECTIONS:
        filename = f"{item['file_id']} - {item['title']}.md"
        filepath = passages_dir / filename

        lookup_query = item.get("api_ref", item["id"])
        print(f"  -> Fetching: {lookup_query} (WEB)")
        scripture_body = fetch_web_scripture(lookup_query)

        for theme in item["themes"]:
            theme_to_passages.setdefault(theme, []).append(
                (item["file_id"], item["title"])
            )

        for xref in item["cross_refs"]:
            clean_ref = sanitize_filename(xref)
            xref_to_passages.setdefault(clean_ref, []).append(
                (item["file_id"], item["title"])
            )

        themes_wikilinks = "\n".join([f"- [[{t}]]" for t in item["themes"]])
        xrefs_wikilinks = "\n".join(
            [f"- [[{sanitize_filename(x)}]]" for x in item["cross_refs"]]
        )

        content = f"""---
type: scripture-passage
book: 2 Peter
chapter: {item['chapter']}
passage: "{item['id']}"
translation: World English Bible (Public Domain)
tags:
  - bible/2peter
  - study/passage
---

# [[2 Peter - MOC|⬅ 2 Peter MOC]] | {item['id']}: {item['title']}

### Section Summary
{item['summary']}

---

### 📖 Scripture Text (WEB - Public Domain)
{scripture_body}

---

## 🏷️ Connected Themes
{themes_wikilinks}

---

## 🔗 Cross-References
{xrefs_wikilinks}

---

## ✍️ Exegetical Notes
- **Context & Structure:** 
- **Word Study / Greek Notes:** 
- **Theological Significance:** 
- **Personal Reflection:** 
"""
        filepath.write_text(content, encoding="utf-8")

    # 2. Generate Theme Notes
    for theme, linked_passages in theme_to_passages.items():
        theme_path = themes_dir / f"{theme}.md"
        passages_list = "\n".join(
            [f"- [[{pid} - {ptitle}|{pid}]]" for pid, ptitle in linked_passages]
        )

        content = f"""---
type: theological-theme
tags:
  - theology/theme
---

# Theme: {theme}

### 📖 Occurrences in 2 Peter
{passages_list}

---

### 📝 Thematic Synthesis
*Trace the theological trajectory, biblical theology connections, and practical implications.*
"""
        theme_path.write_text(content, encoding="utf-8")

    # 3. Generate Cross-Reference Placeholder Notes
    for xref, linked_passages in xref_to_passages.items():
        xref_path = xrefs_dir / f"{xref}.md"
        passages_list = "\n".join(
            [f"- [[{pid} - {ptitle}|{pid}]]" for pid, ptitle in linked_passages]
        )

        content = f"""---
type: scripture-reference
reference: "{xref.replace('.', ':')}"
tags:
  - bible/cross-ref
---

# {xref.replace('.', ':')}

### 🔗 Connected Passages in 2 Peter
{passages_list}

---

### Text & Comparison
*Examine how 2 Peter utilizes, alludes to, or parallels this text.*
"""
        xref_path.write_text(content, encoding="utf-8")

    # 4. Generate Main Map of Content (MOC)
    moc_path = base / "2 Peter - MOC.md"
    passage_index = ""
    for ch in [1, 2, 3]:
        passage_index += f"\n### Chapter {ch}\n"
        ch_passages = [s for s in SECTIONS if s["chapter"] == ch]
        for p in ch_passages:
            passage_index += f"- [[{p['file_id']} - {p['title']}|{p['file_id']} - {p['title']}]] — *{p['summary'][:70]}...*\n"

    all_themes = "\n".join(
        [
            f"- [[{t}]] ({len(theme_to_passages[t])} sections)"
            for t in sorted(theme_to_passages.keys())
        ]
    )

    moc_content = f"""---
type: moc
book: 2 Peter
tags:
  - bible/moc
---

# 📜 2 Peter: Map of Content (MOC)

> **Translation Base:** World English Bible (Modern English, Public Domain)  
> **Core Focus:** Standing firm against antinomian teachers and scoffers through true spiritual knowledge (*epignosis*) and the reality of the Lord's return.

---

## 📑 Structure by Chapter
{passage_index}

---

## 🧭 Thematic Index
{all_themes}
"""
    moc_path.write_text(moc_content, encoding="utf-8")
    print(f"\nCompleted! 2 Peter folder is ready at:\n{base.resolve()}")


if __name__ == "__main__":
    build_obsidian_notes(VAULT_PATH)