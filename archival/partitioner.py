"""Per-bridge time-window CSV partitioner."""

import os
import pandas as pd


class TimeWindowPartitioner:
    """Partition records by time windows."""
    
    def __init__(self, archive_dir: str = "./archive"):
        self.archive_dir = archive_dir
        os.makedirs(archive_dir, exist_ok=True)
    
    def partition_by_bridge(self, records: list, bridge_id: str) -> str:
        """Partition records by bridge ID."""
        df = pd.DataFrame(records)
        bridge_dir = os.path.join(self.archive_dir, bridge_id)
        os.makedirs(bridge_dir, exist_ok=True)
        
        filename = f"{bridge_id}_{pd.Timestamp.now().strftime('%Y%m%d')}.csv"
        filepath = os.path.join(bridge_dir, filename)
        df.to_csv(filepath, index=False)
        return filepath
    
    def partition_by_time(self, records: list, window_days: int = 7) -> dict:
        """Partition records by time window."""
        df = pd.DataFrame(records)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        df['window'] = df['timestamp'].dt.floor(f'{window_days}D')
        
        filepaths = {}
        for window, group in df.groupby('window'):
            filename = f"window_{window.strftime('%Y%m%d')}.csv"
            filepath = os.path.join(self.archive_dir, filename)
            group.to_csv(filepath, index=False)
            filepaths[str(window)] = filepath
        
        return filepaths
