"""Test script for the advanced language translator implementation."""

from translator import tokenize, apply_context, render_output
from interpreter import NaytrunesInterpreter
from phonetics import chant
from seals import archive_seal

symbols = "spiral arc_wave triangle_eye heart"
tokens = tokenize(symbols)
mapped = apply_context(tokens)

print("English:", render_output(mapped, "english"))
print("ArcanaScript:", render_output(mapped, "arcana"))
print("Phonetic:", chant(tokens))

interp = NaytrunesInterpreter()
interp.execute(tokens)

archive_seal("Spiral Flight", "duplication glyph as 'fly'")
