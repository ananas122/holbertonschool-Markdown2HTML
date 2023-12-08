#!/usr/bin/python3
"""Markdown to HTML Converter"""


import sys
import os


def markdowntohtml():
    # Vérifier si le nombre d'arguments est inférieur à 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Nom du fichier Markdown (premier argument)
    markdown_file = sys.argv[1]
    # Nom du fichier de sortie (deuxième argument)
    output_file = sys.argv[2]

    # Vérifier si le fichier Markdown existe
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Si ok, terminer  sortie 0
    sys.exit(0)


if __name__ == "__main__":
    main()