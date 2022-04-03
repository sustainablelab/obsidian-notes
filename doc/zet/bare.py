"""Kindle -> Show Notebook -> Export -> Save As

;ob
    (keystrokes from anywhere in Vim, pneumonic: Obsidan)
    Runs this script (the one you are reading right now!):
    /cygwin64/home/mike/gitrepos/fpga/kindle-exports/kindleHTML-to-markdown/bare.py

        And this script hardcodes the i/o paths:

        - in: the exported Kindle Notebook HTML
        - out: the converted markdown

Open Obsidian vault:

    /cygwin64/home/mike/work/lumiode/gitrepos/simple-controller/doc/zettlekasten/

Notes are updated!
"""
import pathlib
from bs4 import BeautifulSoup

source = pathlib.Path('/cygwin64/home/mike/gitrepos/fpga/kindle-exports/FPGA Prototyping by SystemVerilog Examples-Notebook.html')
html = source.read_text(encoding='UTF-8')
soup = BeautifulSoup(html, 'html.parser')

# Dump to a file to see the HTML structure:
# print(soup.prettify())

tags = soup.find_all(True)
# print(len(tags))

# Dump to a file to see just the tags:
# _tags = pathlib.Path('tags.md')
# with _tags.open("w", encoding="utf-8") as o:
#     for tag in tags:
#         o.write(f"{tag.name} -- {tag.attrs}\n")

is_Highlight = False
is_Obsidian_front_matter = True

md = pathlib.Path(source.stem.strip('-Notebook').replace(' ','-') + '.md')
vault = pathlib.Path('/cygwin64/home/mike/work/lumiode/gitrepos/simple-controller/doc/zettlekasten/')
dest = vault.joinpath(md)
assert vault.exists(), f"Path to vault does not exist: {vault}"

with dest.open("w", encoding="utf-8") as o:
    for tag in tags:
        if tag.has_attr('class'):
            if tag['class'] == ['bookTitle']:
                # Title: {"class":"bookTitle"}
                o.write(f"# {tag.text.strip()}\n\n")
            elif tag['class'] == ['authors']:
                # Authors: {"class":"authors"}
                o.write(f"- Authors: {tag.text.strip()}\n")
            elif tag['class'] == ['sectionHeading']:
                # If I got here without encountering noteText, it
                # means there are no "additional notes" in Kindle
                # export. I use the "additional notes" as my
                # Obsidian front matter -- "internal links" and
                # category "tags".
                is_Obsidian_front_matter = False
                # Section: {"class":"sectionHeading"}
                o.write(f"\n## {tag.text.strip()}\n\n")
            elif tag['class'] == ['noteHeading']:
                # Heading: {"class":"noteHeading"}
                # Example heading:
                # "Highlight (yellow) - CHAPTER 1: GATE-LEVEL COMBINATIONAL CIRCUIT > Page 13  Location 1300"
                # First split at the '-'
                _text = tag.text.strip().partition('-')
                assert len(_text) == 3, f"{_text}: {len(_text)}"
                # Get type: "Highlight" or "Note"
                _type = _text[0].strip().split(' ')[0]
                # Now split at the '>'
                _text = _text[2].strip().partition('>')
                assert len(_text) == 3, f"{_text}: {len(_text)}"
                _spot = _text[2].strip()
                o.write(f"### {_type} at {_spot}\n\n")
                _chapter = _text[0].strip()
                o.write(f"From *{_chapter}*\n\n")
            elif tag['class'] == ['highlight_yellow']:
                is_Highlight = True
                o.write(f":::yellow\n\n")
            elif tag['class'] == ['highlight_pink']:
                is_Highlight = True
                o.write(f":::pink\n\n")
            elif tag['class'] == ['highlight_blue']:
                is_Highlight = True
                o.write(f":::blue\n\n")
            elif tag['class'] == ['highlight_orange']:
                is_Highlight = True
                o.write(f":::orange\n\n")
            elif tag['class'] == ['noteText']:
                # ?noteText: {"class":"noteText"}
                # o.write("\nnoteText\n\n")
                if is_Obsidian_front_matter:
                    # I use the "additional notes" as my Obsidian
                    # front matter -- "internal links" and
                    # category "tags".
                    Obsidian_front_matter = tag.text.strip()
                    is_Obsidian_front_matter = False
                elif is_Highlight:
                    for line in tag.text.split('\n'):
                        o.write(f"> {line}\n")
                    o.write("\n")
                    is_Highlight = False
                else:
                    o.write(f"{tag.text.strip()}\n\n")

main_doc = dest.read_text(encoding='UTF-8')
with dest.open("w", encoding="utf-8") as o:
    o.write(f"{Obsidian_front_matter}\n\n")
    o.write(main_doc)

