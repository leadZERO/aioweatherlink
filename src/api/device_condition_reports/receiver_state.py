from __future__ import annotations

from enum import Enum


class RxState(Enum):
    Synched = 0
    SynchedAndTracking = 1
    Scanning = 2

