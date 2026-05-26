"""SHA-256 tamper-evidence layer for archival records."""

import hashlib
import json
import os


class ChecksumValidator:
    """Generate and verify SHA-256 checksums for tamper evidence."""
    
    def __init__(self, checksum_file: str = "checksums.json"):
        self.checksum_file = checksum_file
        self.checksums = self._load()
    
    def _load(self) -> dict:
        if os.path.exists(self.checksum_file):
            with open(self.checksum_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save(self):
        with open(self.checksum_file, 'w') as f:
            json.dump(self.checksums, f, indent=2)
    
    def compute(self, filepath: str) -> str:
        """Compute SHA-256 checksum of file."""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def register(self, filepath: str) -> str:
        """Register file and compute its checksum."""
        checksum = self.compute(filepath)
        self.checksums[filepath] = checksum
        self._save()
        return checksum
    
    def verify(self, filepath: str) -> tuple:
        """Verify file integrity against registered checksum."""
        if filepath not in self.checksums:
            return False, "File not registered"
        
        current = self.compute(filepath)
        original = self.checksums[filepath]
        
        if current == original:
            return True, "Integrity verified"
        return False, f"Tamper detected!"
