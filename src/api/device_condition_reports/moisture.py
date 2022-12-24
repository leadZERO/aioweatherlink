from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    Type
)

from .receiver_state import RxState
from ..from_json import FromJson
 

# Example from https://weatherlink.github.io/weatherlink-live-local-api/
#
# {
#     "lsid":3187671188,
#     "data_structure_type":2,
#     "txid":3,
#     "temp_1":null,                                 // most recent valid soil temp slot 1 **(°F)**
#     "temp_2":null,                                 // most recent valid soil temp slot 2 **(°F)**
#     "temp_3":null,                                 // most recent valid soil temp slot 3 **(°F)**
#     "temp_4":null,                                 // most recent valid soil temp slot 4 **(°F)**
#     "moist_soil_1":null,                           // most recent valid soil moisture slot 1 **(|cb|)**
#     "moist_soil_2":null,                           // most recent valid soil moisture slot 2 **(|cb|)**
#     "moist_soil_3":null,                           // most recent valid soil moisture slot 3 **(|cb|)**
#     "moist_soil_4":null,                           // most recent valid soil moisture slot 4 **(|cb|)**
#     "wet_leaf_1":null,                             // most recent valid leaf wetness slot 1 **(no unit)**
#     "wet_leaf_2":null,                             // most recent valid leaf wetness slot 2 **(no unit)**
#     "rx_state":null,                               // configured radio receiver state **(no unit)**
#     "trans_battery_flag":null                      // transmitter battery status flag **(no unit)**
# }

@dataclass
class LeafSoilMoistureCondition(FromJson):
    LsId: int
    """Logical sensor id"""

    TxId: int
    """Transmitter id"""

    SoilTemperatures: Dict[int, float | None]
    """Most recent soil temperatures in degress Fahrenheit (max 4 slots)"""

    SoilMoisture: Dict[int, float | None]
    """Most recent soil moisture in |cb| (max 4 slots)"""

    LeafWetness: Dict[int, float | None]
    """Most recent leaf wetness (max 2 slots)"""

    RxState: RxState | None
    """Radio receiver state:
    Synched & Tracking: Transmitter has been acquired and is actively being received.
    Synched: Transmitter has been acquired, but we have missed 1-14 packets in a row.
    Scanning: Transmitter has not been acquired yet, or we’ve lost it (more than 15 missed packets in a row).
    """

    TxBatteryLow: bool | None
    """Internal CR-123A is low. Note: the battery status measurement may cross over from low to okay and back
    again throughout the day depending on the state of the solar panel and super-capacitor. For best results, 
    check the battery status when the solar panel is not producing power.
    """

    @classmethod
    def FromJson(cls: Type[FromJson], obj: Dict[str, Any]) -> LeafSoilMoistureCondition:
        return LeafSoilMoistureCondition(
            LsId=obj['lsid'],
            TxId=obj['txid'],
            SoilTemperatures= {
                1: obj['temp_1'],
                2: obj['temp_2'],
                3: obj['temp_3'],
                4: obj['temp_4']
            },
            SoilMoisture={
                1: obj['moist_soil_1'],
                2: obj['moist_soil_2'],
                3: obj['moist_soil_3'],
                4: obj['moist_soil_4']
            },
            LeafWetness= {
                1: obj['wet_leaf_1'],
                2: obj['wet_leaf_2']
            },
            RxState=RxState(obj['rx_state']),
            TxBatteryLow=True if obj['trans_battery_flag'] == 1 else False
        )
