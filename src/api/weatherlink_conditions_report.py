from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union
)

from .device_condition_reports import *
from .from_json import FromJson

DeviceConditionT = Union[
    IssCondition, 
    LeafSoilMoistureCondition, 
    LssBarometerCondition, 
    LssTempHumidityCondition
]


@dataclass
class WeatherLinkConditionsReport(FromJson):
    """
    Report from parent WeatherLink or AirLink device. The parent device can report on the conditions for multiple 
    child devices (such as weather stations, indoor conditions, leaf/soil moisture, etc.)
    """

    DeviceId: str
    """WeatherLink or Airlink Device Id"""

    Timestamp: datetime
    """Timestamp of conditions report"""

    DeviceConditions: List[DeviceConditionT]
    """Individual conditions reports from devices registered with parent device."""

    @classmethod
    def FromJson(cls: Type[WeatherLinkConditionsReport], obj: Dict[str, Any]) -> WeatherLinkConditionsReport:
        """
        Create object from source API JSON

        :param obj: Python dictionary with key-value pairs, often returned from json.load()
        """
        _deviceId = obj['did']
        _timestamp = datetime.fromtimestamp(obj['ts'], timezone.utc)

        _conditions: List[DeviceConditionT] = []

        for c in obj['conditions']:
            data_structure_type_mapping: Dict[int, Type[DeviceConditionT]] = {
                1: IssCondition,
                2: LeafSoilMoistureCondition,
                3: LssBarometerCondition,
                4: LssTempHumidityCondition
            }
            _conditions.append(data_structure_type_mapping[c['data_structure_type']].FromJson(c))

        return WeatherLinkConditionsReport(
            DeviceId=_deviceId,
            Timestamp=_timestamp,
            DeviceConditions=_conditions
        )
