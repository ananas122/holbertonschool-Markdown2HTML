#!/usr/bin/python3
"""
Markdown to HTML Converter
task
"""

import sys
import os


def convertmdtohtml():
    """ Main function that converts a Markdown file to an HTML file """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(markdown_file, 'r') as md, open(output_file, 'w') as html:
            in_unordered_list = False
            in_ordered_list = False

            for line in md:
                if line.startswith("#"):
                    level = len(line.split()[0])
                    content = line.lstrip("#").strip()
                    html.write(f"<h{level}>{content}</h{level}>\n")
                elif line.startswith("- "):
                    if not in_unordered_list:
                        html.write("<ul>\n")
                        in_unordered_list = True
                    content = line.lstrip("- ").strip()
                    html.write(f"    <li>{content}</li>\n")
                elif line.startswith("* "):
                    if not in_ordered_list:
                        html.write("<ol>\n")
                        in_ordered_list = True
                    content = line.lstrip("* ").strip()
                    html.write(f"    <li>{content}</li>\n")
                else:
                    if in_unordered_list:
                        html.write("</ul>\n")
                        in_unordered_list = False
                    if in_ordered_list:
                        html.write("</ol>\n")
                        in_ordered_list = False
                    html.write(line)

            if in_unordered_list:
                html.write("</ul>\n")
            if in_ordered_list:
                html.write("</ol>\n")
    except IOError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    convertmdtohtml()
