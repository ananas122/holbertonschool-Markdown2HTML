#!/usr/bin/python3
"""
Markdown to HTML Converter
Task 1: Ce script est destiné à convertir un fichier Markdown en fichier HTML.
"""

import sys
import os


def markdowntohtml():
    """convert file md to html"""
    # Vérifier si le nombre d'arguments est inférieur à 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Nom du fichier Markdown (1er argument)
    markdown_file = sys.argv[1]
    # Nom du fichier de sortie (2eme argument)
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)


    # Si ok, terminer avec sortie 0
    sys.exit(0)



    if line.startswith("#"):
        level = len(line.split()[0])
        content = line.strip("#").strip()
        return f"<h{level}>{content}</h{level}>"
    return line


if __name__ == "__main__":
    markdowntohtml()
