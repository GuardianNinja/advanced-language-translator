"""
Phonetics Module
Converts mystical symbols into phonetic chants.
"""


def chant(tokens):
    """
    Convert a list of symbol tokens into a phonetic chant representation.
    
    Args:
        tokens (list): List of symbol tokens
        
    Returns:
        str: Phonetic chant string
    """
    phonetic_map = {
        'spiral': 'spi-RAL',
        'arc_wave': 'ARK-wayv',
        'triangle_eye': 'TRI-ang-EYE',
        'heart': 'HART'
    }
    
    chants = []
    for token in tokens:
        if token in phonetic_map:
            chants.append(phonetic_map[token])
        else:
            # Unknown tokens get a generic phonetic rendering
            chants.append(token.upper().replace('_', '-'))
    
    return ' ~ '.join(chants)
