#!/usr/bin/python3
"""
Markdown to HTML Converter
Task 1: convert heading
"""

import sys
import os


def markdowntohtml():
    """convert file md to html task 0"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # task 1
    with open(markdown_file, 'r') as md, open(output_file, 'w') as html:
        for line in md:
            if line.startswith("#"):
                # Calcule le niveau de l'en-tête en comptant le nombre de '#'
                # par ex, '##' donne un lrvel de 2
                level = len(line.split()[0])

                # Enlève les caractères '#' et les espaces superflus de la ligne
                # pour obtenir uniquement le texte de l'en-tête
                content = line.lstrip("#").strip()

                # crée une balise HTML d'en-tête correspondante
                html.write(f"<h{level}>{content}</h{level}>\n")
            else:
           
                html.write(line)


if __name__ == "__main__":
    markdowntohtml()
