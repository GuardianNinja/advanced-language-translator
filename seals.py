"""
Seals Module
Archive and manage mystical seals and glyphs.
"""


class SealArchive:
    """Singleton archive for storing mystical seals."""
    _instance = None
    _seals = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SealArchive, cls).__new__(cls)
        return cls._instance
    
    def add_seal(self, name, description):
        """Add a seal to the archive."""
        seal_entry = {
            'name': name,
            'description': description
        }
        self._seals.append(seal_entry)
        return seal_entry
    
    def get_seals(self):
        """Get all archived seals."""
        return self._seals


def archive_seal(name, description):
    """
    Archive a mystical seal with its name and description.
    
    Args:
        name (str): Name of the seal
        description (str): Description of the seal's properties
    """
    archive = SealArchive()
    seal = archive.add_seal(name, description)
    print(f"Seal archived: '{seal['name']}' - {seal['description']}")
