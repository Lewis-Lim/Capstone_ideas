cross_references = {
    "Romans 1:17": {
        "theme": "The righteous shall live by faith",
        "references": ["Habakkuk 2:4", "Galatians 3:11", "Hebrews 10:38"],
    },
    "Romans 3:23": {
        "theme": "All have sinned",
        "references": ["Ecclesiastes 7:20", "Isaiah 53:6", "1 John 1:8"],
    },
    "Romans 4:3": {
        "theme": "Abraham believed God",
        "references": ["Genesis 15:6", "James 2:23"],
    },
    "Romans 8:31": {
        "theme": "If God is for us",
        "references": ["Psalm 118:6", "Isaiah 54:17"],
    },
}


def find_references(verse):
    data = cross_references.get(verse)
    if not data:
        return f"No cross-references found for {verse}."

    refs = ", ".join(data["references"])
    return f"{verse} focuses on '{data['theme']}' and connects to: {refs}"


print(find_references("Romans 1:17"))