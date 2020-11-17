from typing import Optional, Dict, Any


class ReferenceEventData:
    """The data within all Firebase Real Time Database reference events."""
    data: Optional[Dict[str, Any]]
    delta: Optional[Dict[str, Any]]

    def __init__(self, data: Optional[Dict[str, Any]], delta: Optional[Dict[str, Any]]) -> None:
        self.data = data
        self.delta = delta
