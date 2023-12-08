#!/usr/bin/python3
"""Markdown to HTML Converter"""

import sys
import os
import markdown

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

    # Ajouter ici le code pour lire le fichier Markdown et le convertir en HTML

    # Si ok, terminer avec sortie 0
    sys.exit(0)


def convert_heading(line):
    if line.startswith("#"):
        level = len(line.split()[0])
        content = line.strip("#").strip()
        return f"<h{level}>{content}</h{level}>"
    return line


if __name__ == "__main__":
    markdowntohtml()
