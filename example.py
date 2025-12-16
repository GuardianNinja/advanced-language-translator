"""
Example usage of the Advanced Language Translator.
"""

from translator import phonetic_map, chant


def main():
    print("Advanced Language Translator - Phonetic Mapping System")
    print("=" * 60)
    print()
    
    print("Available Phonetic Mappings:")
    print("-" * 40)
    for symbol, sound in sorted(phonetic_map.items()):
        print(f"  {symbol:15s} -> {sound}")
    print()
    
    print("Example Chants:")
    print("-" * 40)
    
    # Example 1: Simple chant
    tokens1 = ["spiral", "heart"]
    result1 = chant(tokens1)
    print(f"Input:  {tokens1}")
    print(f"Output: '{result1}'")
    print()
    
    # Example 2: Multiple tokens
    tokens2 = ["triangle_eye", "dot_cluster", "arc_wave"]
    result2 = chant(tokens2)
    print(f"Input:  {tokens2}")
    print(f"Output: '{result2}'")
    print()
    
    # Example 3: All symbols
    tokens3 = list(phonetic_map.keys())
    result3 = chant(tokens3)
    print(f"Input:  {tokens3}")
    print(f"Output: '{result3}'")
    print()
    
    # Example 4: Mixed known and unknown
    tokens4 = ["mandala", "unknown_symbol", "tear"]
    result4 = chant(tokens4)
    print(f"Input:  {tokens4}")
    print(f"Output: '{result4}'")
    print("         (unknown tokens are kept as-is)")
    print()


if __name__ == "__main__":
    main()
