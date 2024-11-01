"""Helper functions for the diabetes risk calculator."""

from pathlib import Path
from typing import Dict, Any
import json


def save_configuration(config: Dict[str, Any], filepath: Path) -> None:
    """Save configuration to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)


def load_configuration(filepath: Path) -> Dict[str, Any]:
    """Load configuration from a JSON file."""
    with open(filepath) as f:
        return json.load(f)
