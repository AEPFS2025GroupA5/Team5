# Team5/model/__init__.py
from __future__ import annotations

from .hotel      import Hotel
from .room_type  import RoomType
from .room       import Room
from .facility   import Facility
from .adress     import Address      # falls es adress.py + Klasse Address gibt

__all__ = [
    "Hotel",
    "RoomType",
    "Room",
    "Facility",
    "Address",
]
