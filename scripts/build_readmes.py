"""Render all 11 README editions from the structured case collection."""

import argparse
from collections import Counter
from html import escape
import json
from pathlib import Path
from urllib.parse import quote, urlencode

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = [
    ("en","README.md","English","111111"),
    ("es","README_es.md","Español","ffb703"),
    ("pt","README_pt.md","Português","2a9d8f"),
    ("ja","README_ja.md","日本語","52b788"),
    ("ko","README_ko.md","한국어","4ea8de"),
    ("de","README_de.md","Deutsch","f4a261"),
    ("fr","README_fr.md","Français","e76f51"),
    ("tr","README_tr.md","Türkçe","d62828"),
    ("zh-TW","README_zh-TW.md","繁體中文","8338ec"),
    ("zh-CN","README_zh-CN.md","简体中文","ef476f"),
    ("ru","README_ru.md","Русский","577590"),
]
CATEGORIES = [
    ("engineering","🛠️"),("graphics","🎨"),("games","🎮"),("knowledge","📚"),("evaluations","📈"),
]
TYPES = {"Demo","Tutorial","Evaluation","Integration","Benchmark","Limit"}
LICENSE = "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)"


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def markdown_label(value):
    return value.replace("[", "&#91;").replace("]", "&#93;").replace("|", "&#124;").replace("\n", " ")


def media_markup(item, title, index):
    alt = escape(f"{title} · {index}")
    if item["kind"] == "video":
        img = f'<img src="{escape(item["poster_url"])}" alt="{alt}" width="560">'
        return f'<a href="{escape(item["url"])}">{img}</a>'
    return f'<img src="{escape(item["url"])}" alt="{alt}" width="560">'


def case_block(item, wording, strings):
    number = item["public_number"]
    title = markdown_label(wording["title"])
    head = f'### Case {number}: [{title}]({item["source_url"]}) (by [{item["author_handle"]}]({item["author_url"]}))'
    lines = [
        f'<a id="case-{number}"></a>', head, "", f'**{wording["action"]}**', "",
        wording["takeaway"], "", wording["notes"], "",
    ]
    for url in item.get("supporting_urls", []):
        lines.extend([f'[{strings["supporting_source"]}]({url})', ""])
    if item["prompt_public"]:
        lines.extend(["**Prompt:**", "", "```", item["prompt_text"], "```", ""])
    visuals = [media_markup(asset,wording["title"],index) for index,asset in enumerate(item["media_assets"],1)]
    if item["kind"] == "comparison" and len(visuals) == 2:
        lines.extend(["<table>","<tr>",f"<td>{visuals[0]}</td>",f"<td>{visuals[1]}</td>","</tr>","</table>",""])
    else:
        lines.extend(visuals + [""])
    lines.extend([f'Type: {item["type"]} | Date: {item["date"]}', "", "---", ""])
    return lines


def heading(anchor, symbol, label):
    prefix = f"{symbol} " if symbol else ""
    return [f'<a id="{anchor}"></a>', f'## {prefix}{label}', ""]


def localized_cases(items, localization):
    fields = localization["cases"]
    expected = {f'case-{r["public_number"]}' for r in items}
    if set(fields) != expected:
        raise ValueError("Localized case set differs from the source inventory")
    for case, values in fields.items():
        if set(values) != {"title","takeaway","notes","action"} or not all(s.strip() for s in values.values()):
            raise ValueError(f"Incomplete case translation for {case}")
    return fields


def render(data, presentation, localization):
    items = data["items"]
    wording = localized_cases(items,localization)
    s = localization["strings"]
    count = Counter(item["category_key"] for item in items)
    media_count = sum(len(item["media_assets"]) for item in items)
    utm = urlencode({"utm_source":"github","utm_medium":"banner","utm_campaign":presentation["campaign"],"utm_content":"readme_banner"})
    banner_target = escape(f'{presentation["landing_url"]}?{utm}')
    banner_image = escape(presentation["banner_url"])
    lines = ["<div align=\"center\">", "",
             f'<a href="{banner_target}"><img src="{banner_image}" alt="Gemini 4 Neon Use Cases" width="760"></a>',
             "",LICENSE,""]
    lines.extend(
        f'[![{name}](https://img.shields.io/badge/{quote(name, safe="")}-{color})]({filename})'
        for _,filename,name,color in LANGUAGES
    )
    lines.extend(["","</div>",""])
    lines.extend(heading("introduction","🍌",s["introduction"]) + [f'**{s["scope"]}**',""])
    lines.extend(heading("overview","📊",s["overview"]) + [s["overview_sentence"].format(cases=len(items),visuals=media_count),""])
    for category,_ in CATEGORIES:
        lines.append(f"- {s[category]} · {count[category]}")
    lines.extend(["", "> [!NOTE]", f'> {s["evidence_note"]}', ""])
    lines.extend(heading("quick-start","⚡",s["quick_start"]) + [f'{i}. {s[f"step_{i}"]}' for i in range(1,4)] + [""])
    lines.extend(heading("menu","📑",s["menu"]) + [
        f'| {s["case"]} | {s["category"]} | {s["what_it_shows"]} | {s["type"]} |',
        "|---|---|---|---|",
    ])
    for item in items:
        case_id = f'case-{item["public_number"]}'
        case_text = wording[case_id]
        lines.append(
            f'| [{markdown_label(case_text["title"])}](#{case_id}) | {s[item["category_key"]]} | '
            f'{markdown_label(case_text["takeaway"])} | {item["type"]} |'
        )
    lines.extend([
        "", f'| {s["section"]} | {s["contents"]} |', "|---|---|",
        f'| [{s["related"]}](#related-repositories) | {s["other_collections"]} |',
        f'| [{s["quick_start"]}](#quick-start) | {s["reading_cases"]} |',
        f'| [{s["acknowledge"]}](#acknowledge) | {s["credits"]} |', "",
    ])
    for category,symbol in CATEGORIES:
        lines.extend([f'## {symbol} {s[category]}', f'<a id="{category}"></a>', ""])
        for item in items:
            if item["category_key"] == category:
                lines.extend(case_block(item,wording[f'case-{item["public_number"]}'],s))
    lines.extend(heading("related-repositories","",s["related"]) + [
        f'- [{s["carbon"]}](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases)',
        f'- [{s["hydrogen"]}](https://github.com/Evolink-AI/awesome-gemini-4-hydrogen-use-cases)',"",
    ])
    lines.extend(heading("acknowledge","🙏",s["acknowledge"]) + [s["thanks"],""])
    credits = {}
    for item in items:
        credits.setdefault(item["author_url"],item["author_handle"])
    lines.extend([", ".join(f'[{name}]({url})' for url,name in credits.items()),"",f'*{s["corrections"]}*',""])
    return "\n".join(lines)


def render_catalog(data):
    lines = [
        "# Gemini 4 Neon Case Catalog", "",
        "This catalog indexes the structured case records used to build the README editions.", "",
        "| Case | Source | Creator | Category | Type | Date |", "|---|---|---|---|---|---|",
    ]
    for item in data["items"]:
        n = item["public_number"]
        lines.append(
            f'| [Case {n}](../README.md#case-{n}) | [{markdown_label(item["title"])}]({item["source_url"]}) | '
            f'[{item["author_handle"]}]({item["author_url"]}) | {data["category_names"][item["category_key"]]} | '
            f'{item["type"]} | {item["date"]} |'
        )
    return "\n".join(lines) + "\n"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",action="store_true",help="Validate generated files without writing them")
    args=parser.parse_args()
    data=load("data/use-cases.json")
    presentation=load("data/presentation.json")
    items=data["items"]
    if [row["public_number"] for row in items] != list(range(1,len(items)+1)) or not items:
        raise ValueError("Case numbering is not contiguous")
    if len({row["source_url"] for row in items}) != len(items) or len({row["dedup_key"] for row in items}) != len(items):
        raise ValueError("Duplicate case sources or deduplication keys")
    for row in items:
        if row["type"] not in TYPES or not row["media_assets"]:
            raise ValueError(f'Invalid type or missing media for case {row["public_number"]}')
        if row["prompt_public"] != bool(row["prompt_text"]):
            raise ValueError(f'Prompt evidence inconsistent for case {row["public_number"]}')
    pages = {"docs/usecase-catalog.md":render_catalog(data)}
    for locale,file,_,_ in LANGUAGES:
        pages[file]=render(data,presentation,load(f"data/localizations/{locale}.json"))
    changed=[]
    for filename,contents in pages.items():
        path=ROOT/filename
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8")!=contents:
                changed.append(filename)
        else:
            path.write_text(contents,encoding="utf-8")
    if changed:
        raise SystemExit("Generated output differs: "+", ".join(changed))
    print(f'{len(items)} cases across {len(LANGUAGES)} README editions')


if __name__ == "__main__":
    main()
