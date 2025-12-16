"""
Naytrunes Interpreter Module
Executes mystical symbol sequences with elemental interpretations.
"""


class NaytrunesInterpreter:
    """
    Interpreter for Naytrunes mystical symbol language.
    Executes token sequences and provides elemental interpretations.
    """
    
    def __init__(self):
        """Initialize the interpreter with an empty execution log."""
        self.execution_log = []
        self.element_mapping = {
            'spiral': 'air',
            'arc_wave': 'water',
            'triangle_eye': 'fire',
            'heart': 'earth'
        }
    
    def execute(self, tokens):
        """
        Execute a sequence of tokens and interpret their mystical meaning.
        
        Args:
            tokens (list): List of symbol tokens to execute
        """
        print("=== Naytrunes Interpretation ===")
        
        for i, token in enumerate(tokens):
            element = self.element_mapping.get(token, 'void')
            self.execution_log.append({
                'step': i + 1,
                'token': token,
                'element': element
            })
            print(f"Step {i + 1}: {token} [{element}]")
        
        print(f"\nExecution complete: {len(tokens)} symbols processed")
        self._analyze_elemental_balance()
    
    def _analyze_elemental_balance(self):
        """Analyze and display the elemental balance of the executed sequence."""
        element_counts = {}
        for entry in self.execution_log:
            element = entry['element']
            element_counts[element] = element_counts.get(element, 0) + 1
        
        print(f"Elemental Balance: {element_counts}")
    
    def get_log(self):
        """
        Get the execution log.
        
        Returns:
            list: Execution log entries
        """
        return self.execution_log
