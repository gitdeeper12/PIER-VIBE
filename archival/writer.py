"""Append-only JSON/CSV safety record writer."""

import json
import csv
import os
from datetime import datetime


class SafetyRecordWriter:
    """Write safety records to append-only storage."""
    
    def __init__(self, archive_dir: str = "./archive"):
        self.archive_dir = archive_dir
        os.makedirs(archive_dir, exist_ok=True)
    
    def write_json(self, record: dict) -> str:
        """Write record as JSON."""
        record["timestamp"] = datetime.now().isoformat()
        filename = f"bridge_record_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.archive_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(record, f, indent=2)
        return filepath
    
    def write_csv(self, records: list) -> str:
        """Write records as CSV."""
        if not records:
            return ""
        filename = f"bridge_data_{datetime.now().strftime('%Y%m%d')}.csv"
        filepath = os.path.join(self.archive_dir, filename)
        
        fieldnames = list(records[0].keys())
        file_exists = os.path.exists(filepath)
        
        with open(filepath, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(records)
        return filepath
