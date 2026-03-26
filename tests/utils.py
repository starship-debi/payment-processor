import os
import json
from typing import Dict, Any, Optional, List
from datetime import datetime

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Read and parse a JSON file."""
    if not os.path.exists(file_path):
        return None
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (TypeError, IOError):
        return False

def generate_timestamp() -> str:
    """Generate a UTC timestamp string."""
    return datetime.utcnow().isoformat() + 'Z'

def validate_amount(amount: float) -> bool:
    """Validate that amount is a positive number with up to 2 decimal places."""
    return isinstance(amount, (int, float)) and amount >= 0 and round(amount, 2) == amount

def filter_dict_keys(data: Dict[str, Any], keys_to_keep: List[str]) -> Dict[str, Any]:
    """Filter a dictionary to only include specified keys."""
    return {k: v for k, v in data.items() if k in keys_to_keep}

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get an environment variable or return a default value."""
    return os.getenv(key, default)