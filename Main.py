#!/usr/bin/python
# coding: utf-8
#
# Pursuit, copyright (c) 2016 Ben Kybartas <bkybartas@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# 29 November 2014

__author__ = 'Ben'

from GrammarLoader import GrammarLoader
from Builder import Builder

def get_word_count(novel):
    return len(novel.split())

word_count = 50000

#This will eventually be a 50k word novel
novel = ""

#Load our grammar
loader = GrammarLoader("NaNoGenMo2016_Grammar.txt")
loader.load_grammar()

#Set up the builder
builder = Builder()

#Our current story
story_number = 0

novel += "\\section*{0}\\textit{[A suspect escapes." + builder.expand_phrase_until_complete(loader, "#chase#") + "]}"
novel = novel.replace("& ", "\n")
while(get_word_count(novel) < word_count):

    #increment story number
    story_number += 1

    #Generate a line
    if (story_number == 1):
        new_line = "\\section*{" + str(story_number) + " \\small{hour after the escape}}\n\n"
    else:
        new_line = "\\section*{" + str(story_number) + " \\small{hours after the escape}}\n\n"

    new_line += builder.expand_phrase_until_complete(loader, "#main#")
    new_line += "\n\n\\textit{[" + builder.expand_phrase_until_complete(loader, "#chase#") + "]}\n\n"

    #Fix some stuff
    new_line = new_line.replace("  ", " ")

    #Yeah its a hack
    new_line = new_line.replace(" a a", " an a")
    new_line = new_line.replace(" a e", " an e")
    new_line = new_line.replace(" a i", " an i")
    new_line = new_line.replace(" a o", " an o")
    new_line = new_line.replace(" a u", " an u")
    new_line = new_line.replace(" A a", " An a")
    new_line = new_line.replace(" A e", " An e")
    new_line = new_line.replace(" A i", " An i")
    new_line = new_line.replace(" A o", " An o")
    new_line = new_line.replace(" A u", " An u")
    new_line = new_line.replace("\\n", "\n\n")
    new_line = new_line.replace("&", ":")

    novel += new_line + "\n"

story_number += 1
novel += "\\section*{-1}\\textit{"
novel += builder.expand_phrase_until_complete(loader, "#conclusion#")
novel += "}\n\n\nAfter " + str(story_number) + " hours the pursuit ends.\n\n"

filename = "Pursuit.tex"
filename2 = "Pursuit.txt"
title = "Pursuit\\\\A Paranoid Thriller"
author = "Ben Kybartas"
latex_header = "\\documentclass{report}\n\\setlength\\parindent{0pt}\n\\title{" + title + "}\n\\date{}\n\\begin{document}\n\\maketitle\n"
latex_footer = "\\end{document}"

file = open("Result\\" + filename, "w")
file.write(latex_header)
file.write(novel)
file.write(latex_footer)
file.close()