from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    Type
)

from ..from_json import FromJson

# Example from https://weatherlink.github.io/weatherlink-live-local-api/
#
# {
#     "lsid":48307,
#     "data_structure_type":4,
#     "temp_in":78.0,                                // most recent valid inside temp **(°F)**
#     "hum_in":41.1,                                 // most recent valid inside humidity **(%RH)**
#     "dew_point_in":7.8,                            // **(°F)**
#     "heat_index_in":8.4                            // **(°F)**
# }

@dataclass
class LssTempHumidityCondition(FromJson):
    LsId: int
    """Logical Sensor Id"""

    Temperature: float | None
    """Most recent indoor temperature in degrees Fahrenheit"""

    Humidity: float | None
    """Most recent indoor humidity in percent relative humitity"""

    DewPoint: float | None
    """Most recent indoor dewpoint in degrees Fahrenheit"""

    HeatIndex: float | None
    """Most recent indoor heat index in degrees Fahrenheit"""

    @classmethod
    def FromJson(cls: Type[FromJson], obj: Dict[str, Any]) -> LssTempHumidityCondition:
        return LssTempHumidityCondition(
            LsId=obj['lsid'],
            Temperature=obj['temp_in'],
            Humidity=obj['hum_in'],
            DewPoint=obj['dew_point_in'],
            HeatIndex=obj['heat_index_in']
        )

# Example from https://weatherlink.github.io/weatherlink-live-local-api/
#     
# {
#     "lsid":48306,
#     "data_structure_type":3,
#     "bar_sea_level":30.008,                        // most recent bar sensor reading with elevation adjustment **(inches)**
#     "bar_trend":null,                              // current 3 hour bar trend **(inches)**
#     "bar_absolute":30.008                          // raw bar sensor reading **(inches)**
# }

@dataclass
class LssBarometerCondition(FromJson):
    LsId: int
    """Logical Sensor Id"""

    Pressure: float | None
    """Absolute barometric pressure reading in inches"""

    SeaLevelPressure: float | None
    """Barometric pressure reading corrected for local elevation in inches"""

    ThreeHourPressureTrend: float | None
    """3-hour barometric pressure trend in inches"""

    @classmethod
    def FromJson(cls: Type[FromJson], obj: Dict[str, Any]) -> LssBarometerCondition:
        return LssBarometerCondition(
            LsId=obj['lsid'],
            Pressure=obj['bar_absolute'],
            SeaLevelPressure=obj['bar_sea_level'],
            ThreeHourPressureTrend=obj['bar_trend']
        )
        