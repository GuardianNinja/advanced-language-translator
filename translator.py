# Tokenizer + Mapping + Contextual Rules

glyph_map = {
    "spiral": "fly",
    "triangle_eye": "see",
    "dot_cluster": "spirit",
    "arc_wave": "flow",
    "heart": "love",
    "mandala": "balance",
    "tear": "weep"
}

def tokenize(symbols_str):
    return symbols_str.split()

def apply_context(tokens):
    result = []
    for i, tok in enumerate(tokens):
        if tok == "spiral" and i+1 < len(tokens) and tokens[i+1] == "spiral":
            result.append("fly fast")
        else:
            result.append(glyph_map.get(tok, f"[unknown:{tok}]"))
    return result

def render_output(tokens, mode="english"):
    if mode == "arcana":
        arcana_map = {
            "fly": "rep",
            "see": "see",
            "spirit": "script",
            "flow": "arc",
            "love": "love",
            "balance": "balance",
            "weep": "weep"
        }
        return " ".join([arcana_map.get(t, t) for t in tokens])
    elif mode == "phonetic":
        phonetic_map = {
            "fly": "flao",
            "see": "si",
            "spirit": "spir",
            "flow": "flo",
            "love": "luv",
            "balance": "balan",
            "weep": "wep"
        }
        return " ".join([phonetic_map.get(t, t) for t in tokens])
    else:
        return " ".join(tokens)
