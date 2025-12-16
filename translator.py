"""
Advanced Language Translator - Phonetic Mapping System

This module provides phonetic translation for symbolic language tokens.
"""

phonetic_map = {
    "spiral": "flao",
    "triangle_eye": "si",
    "dot_cluster": "spir",
    "arc_wave": "flo",
    "heart": "luv",
    "mandala": "balan",
    "tear": "wep"
}

def chant(tokens):
    """
    Convert a list of tokens to their phonetic representations.
    
    Args:
        tokens: A list of token strings to be translated
        
    Returns:
        A space-separated string of phonetic sounds
        
    Example:
        >>> chant(["spiral", "heart"])
        'flao luv'
        >>> chant(["triangle_eye", "dot_cluster"])
        'si spir'
    """
    return " ".join([phonetic_map.get(t, t) for t in tokens])
