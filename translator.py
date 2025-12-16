"""
Advanced Language Translator Module
Provides tokenization, context mapping, and output rendering for mystical symbols.
"""


def tokenize(symbols):
    """
    Tokenize a string of space-separated symbols into a list of tokens.
    
    Args:
        symbols (str): Space-separated symbol names
        
    Returns:
        list: List of symbol tokens
    """
    return symbols.strip().split()


def apply_context(tokens):
    """
    Apply contextual mapping to tokens, enriching them with metadata.
    
    Args:
        tokens (list): List of symbol tokens
        
    Returns:
        list: List of context-enriched token dictionaries
    """
    context_map = {
        'spiral': {'meaning': 'journey', 'arcana': '⟲', 'element': 'air'},
        'arc_wave': {'meaning': 'flow', 'arcana': '⌇', 'element': 'water'},
        'triangle_eye': {'meaning': 'vision', 'arcana': '△👁', 'element': 'fire'},
        'heart': {'meaning': 'emotion', 'arcana': '♥', 'element': 'earth'}
    }
    
    mapped = []
    for token in tokens:
        if token in context_map:
            mapped.append({
                'token': token,
                'meaning': context_map[token]['meaning'],
                'arcana': context_map[token]['arcana'],
                'element': context_map[token]['element']
            })
        else:
            # Handle unknown tokens gracefully
            mapped.append({
                'token': token,
                'meaning': 'unknown',
                'arcana': '?',
                'element': 'void'
            })
    
    return mapped


def render_output(mapped, format_type):
    """
    Render the mapped tokens in a specific output format.
    
    Args:
        mapped (list): List of context-enriched token dictionaries
        format_type (str): Output format ('english' or 'arcana')
        
    Returns:
        str: Formatted output string
    """
    if format_type == 'english':
        meanings = [item['meaning'] for item in mapped]
        return ' '.join(meanings)
    elif format_type == 'arcana':
        arcana_symbols = [item['arcana'] for item in mapped]
        return ' '.join(arcana_symbols)
    else:
        return f"Unknown format: {format_type}"
