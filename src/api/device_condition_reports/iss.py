from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
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
#     "lsid":48308,                                  // logical sensor ID **(no unit)**
#     "data_structure_type":1,                       // data structure type **(no unit)**
#     "txid":1,                                      // transmitter ID **(no unit)**
#     "temp":62.7,                                   // most recent valid temperature **(°F)**
#     "hum":1.1,                                     // most recent valid humidity **(%RH)**
#     "dew_point":-0.3,                              // **(°F)**
#     "wet_bulb":null,                               // **(°F)**
#     "heat_index":5.5,                              // **(°F)**
#     "wind_chill":6.0,                              // **(°F)**
#     "thw_index":5.5,                               // **(°F)**
#     "thsw_index":5.5,                              // **(°F)**
#     "wind_speed_last":2,                           // most recent valid wind speed **(mph)**
#     "wind_dir_last":null,                          // most recent valid wind direction **(°degree)**
#     "wind_speed_avg_last_1_min":4,                 // average wind speed over last 1 min **(mph)**
#     "wind_dir_scalar_avg_last_1_min":15,           // scalar average wind direction over last 1 min **(°degree)**
#     "wind_speed_avg_last_2_min":42606,             // average wind speed over last 2 min **(mph)**
#     "wind_dir_scalar_avg_last_2_min":170.7,        // scalar average wind direction over last 2 min **(°degree)**
#     "wind_speed_hi_last_2_min":8,                  // maximum wind speed over last 2 min **(mph)**
#     "wind_dir_at_hi_speed_last_2_min":0.0,         // gust wind direction over last 2 min **(°degree)**
#     "wind_speed_avg_last_10_min":42606,            // average wind speed over last 10 min **(mph)**
#     "wind_dir_scalar_avg_last_10_min":4822.5,      // scalar average wind direction over last 10 min **(°degree)**
#     "wind_speed_hi_last_10_min":8,                 // maximum wind speed over last 10 min **(mph)**
#     "wind_dir_at_hi_speed_last_10_min":0.0,        // gust wind direction over last 10 min **(°degree)**
#     "rain_size":2,                                 // rain collector type/size **(0: Reserved, 1: 0.01", 2: 0.2 mm, 3:  0.1 mm, 4: 0.001")**
#     "rain_rate_last":0,                            // most recent valid rain rate **(counts/hour)**
#     "rain_rate_hi":null,                           // highest rain rate over last 1 min **(counts/hour)**
#     "rainfall_last_15_min":null,                   // total rain count over last 15 min **(counts)**
#     "rain_rate_hi_last_15_min":0,                  // highest rain rate over last 15 min **(counts/hour)**
#     "rainfall_last_60_min":null,                   // total rain count for last 60 min **(counts)**
#     "rainfall_last_24_hr":null,                    // total rain count for last 24 hours **(counts)**
#     "rain_storm":null,                             // total rain count since last 24 hour long break in rain **(counts)**
#     "rain_storm_start_at":null,                    // UNIX timestamp of current rain storm start **(seconds)**
#     "solar_rad":747,                               // most recent solar radiation **(W/m²)**
#     "uv_index":5.5,                                // most recent UV index **(Index)**
#     "rx_state":2,                                  // configured radio receiver state **(no unit)**
#     "trans_battery_flag":0,                        // transmitter battery status flag **(no unit)**
#     "rainfall_daily":63,                           // total rain count since local midnight **(counts)**
#     "rainfall_monthly":63,                         // total rain count since first of month at local midnight **(counts)**
#     "rainfall_year":63,                            // total rain count since first of user-chosen month at local midnight **(counts)**
#     "rain_storm_last":null,                        // total rain count since last 24 hour long break in rain **(counts)**
#     "rain_storm_last_start_at":null,               // UNIX timestamp of last rain storm start **(sec)**
#     "rain_storm_last_end_at":null                  // UNIX timestamp of last rain storm end **(sec)**
# }

@dataclass
class Wind:
    Speed: float
    Direction: int


@dataclass
class IssCondition(FromJson):
    LsId: int
    """Logical sensor id"""

    TxId: int
    """Transmitter id"""

    Temperature: float | None
    """Most recent temperature in degrees Fahrenheit"""

    Humidity: float | None
    """Most recent relative humidity in percent"""

    DewPoint: float | None
    """Most recent dew point in degrees Fahrenheit"""

    WetBulb: float | None
    """Most recent wet bulb in degrees Fahrenheit"""

    HeatIndex: float | None
    """Most recent heat index in degrees Fahrenheit"""

    WindChill: float | None
    """Most recent wind chill in degrees Fahrenheit"""

    THWIndex: float | None
    """Most recent temperature humidity wind index in degrees Fahrenheit"""

    THSWIndex: float | None
    """Most recent temperature humidity sun wind index in degrees Fahrenheit"""

    WindLast: Wind | None
    """Most recent wind reading. Speed in miles per hour"""

    Wind1MinAverage: Wind | None
    """Last 1-minute wind average speed and direction, speed in miles per hour"""

    Wind2MinAverage: Wind | None
    """Last 2-minute wind average speed and direction, speed in miles per hour"""

    Wind2MinGust: Wind | None
    """Last 2-minute wind gust speed and direction, speed in miles per hour"""

    Wind10MinAverage: Wind | None
    """Last 10-minute wind average speed and direction, speed in miles per hour"""

    Wind10MinGust: Wind | None
    """Last 10-minute wind gust speed and direction, speed in miles per hour"""

    RainRate: float | None
    """Most recent rain rate in inches per hour"""

    Rain1MinMax: float | None
    """Last 1-minute maximum rain rate in inches per hour"""

    Rain15MinTotal: float | None
    """Last 15-minute total rain in inches per hour"""

    Rain15MinMax: float | None
    """Last 15-minute maximum rain rate in inches per hour"""

    Rain60MinTotal: float | None
    """Last 60-minute total rain in inches per hour"""

    Rain24HourTotal: float | None
    """Last 24-hour total rain in inches per hour"""

    RainStormTotal: float | None
    """Most recent rain storm total rain in inches per hour"""

    RainStormStarted: datetime | None
    """When most recent rain storm started"""

    RainStormLastTotal: float | None
    """Total rain since last 24-hour long break in rain in inches"""

    RainStormLastStarted: datetime | None
    """When last rain storm started"""

    RainStormLastEnded: datetime | None
    """When last rain storm ended"""

    RainDaily: float | None
    """Total rain since station local midmight in inches"""

    RainMonthly: float | None
    """Total rain since first of month at station local midnight in inches"""

    RainYearly: float | None
    """Total rain since first of year at station local midnight in inches"""

    SolarRadiation: float | None
    """Most recent solar radiation in watts per square meter"""

    UVIndex: float | None
    """Most recent UV index"""

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
    def FromJson(cls: Type[FromJson], obj: Dict[str, Any]) -> IssCondition:
        def _RainCountToInches(count: float | None) -> float | None:
            if count is None:
                return None

            if obj['rain_size'] == 1:
                return count * 0.01
            elif obj['rain_size'] == 2:
                return count * 0.2 * 0.0393701
            elif obj['rain_size'] == 3:
                return count * 0.1 * 0.0393701
            elif obj['rain_size'] == 4:
                return count * 0.001
            
            ValueError(f'Unknown rain cup size found: {obj["rain_size"]}')

        return IssCondition(
            LsId=obj['lsid'],
            TxId=obj['txid'],
            Temperature=obj['temp'],
            Humidity=obj['hum'],
            DewPoint=obj['dew_point'],
            WetBulb=obj['wet_bulb'],
            HeatIndex=obj['heat_index'],
            WindChill=obj['wind_chill'],
            THWIndex=obj['thw_index'],
            THSWIndex=obj['thsw_index'],
            WindLast=Wind(Speed=obj['wind_speed_last'], Direction=obj['wind_dir_last']),
            Wind1MinAverage=Wind(Speed=obj['wind_speed_avg_last_1_min'], Direction=obj['wind_dir_scalar_avg_last_1_min']),
            Wind2MinAverage=Wind(Speed=obj['wind_speed_avg_last_2_min'], Direction=obj['wind_dir_scalar_avg_last_2_min']),
            Wind2MinGust=Wind(Speed=obj['wind_speed_hi_last_2_min'], Direction=obj['wind_dir_at_hi_speed_last_2_min']),
            Wind10MinAverage=Wind(Speed=obj['wind_speed_avg_last_10_min'], Direction=obj['wind_dir_scalar_avg_last_10_min']),
            Wind10MinGust=Wind(Speed=obj['wind_speed_hi_last_10_min'], Direction=obj['wind_dir_at_hi_speed_last_10_min']),
            RainRate=_RainCountToInches(obj['rain_rate_last']),
            Rain1MinMax=_RainCountToInches(obj['rain_rate_hi']),
            Rain15MinTotal=_RainCountToInches(obj['rainfall_last_15_min']),
            Rain15MinMax=_RainCountToInches(obj['rain_rate_hi_last_15_min']),
            Rain60MinTotal=_RainCountToInches(obj['rainfall_last_60_min']),
            Rain24HourTotal=_RainCountToInches(obj['rainfall_last_24_hr']),
            RainStormTotal=_RainCountToInches(obj['rain_storm']),
            RainStormStarted=datetime.fromtimestamp(obj['rain_storm_start_at'], timezone.utc) if obj['rain_storm_start_at'] is not None else None,
            RainStormLastTotal=_RainCountToInches(obj['rain_storm_last']),
            RainStormLastStarted=datetime.fromtimestamp(obj['rain_storm_last_start_at'], timezone.utc) if obj['rain_storm_last_start_at'] is not None else None,
            RainStormLastEnded=datetime.fromtimestamp(obj['rain_storm_last_end_at'], timezone.utc) if obj['rain_storm_last_end_at'] is not None else None,
            RainDaily=_RainCountToInches(obj['rainfall_daily']),
            RainMonthly=_RainCountToInches(obj['rainfall_monthly']),
            RainYearly=_RainCountToInches(obj['rainfall_year']),
            SolarRadiation=obj['solar_rad'],
            UVIndex=obj['uv_index'],
            RxState=RxState(int(obj['rx_state'])),
            TxBatteryLow=True if obj['trans_battery_flag'] == 1 else False
        )
