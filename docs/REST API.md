(from https://weatherlink.github.io/weatherlink-live-local-api/)

 http://<WeatherLink Live’s ip_addr:port>/v1/current_conditions

 Response string
The data_structure_type field can be used to determine what type of record a JSON object represents. Possible values include:

1 = ISS Current Conditions record

2 = Leaf/Soil Moisture Current Conditions record

3 = LSS BAR Current Conditions record

4 = LSS Temp/Hum Current Conditions record

{
    "data":
    {
        "did":"001D0A700002",
        "ts":1531754005,
        "conditions":[
            {
                "lsid":48308,                                  // logical sensor ID **(no unit)**
                "data_structure_type":1,                       // data structure type **(no unit)**
                "txid":1,                                      // transmitter ID **(no unit)**
                "temp":62.7,                                   // most recent valid temperature **(°F)**
                "hum":1.1,                                     // most recent valid humidity **(%RH)**
                "dew_point":-0.3,                              // **(°F)**
                "wet_bulb":null,                               // **(°F)**
                "heat_index":5.5,                              // **(°F)**
                "wind_chill":6.0,                              // **(°F)**
                "thw_index":5.5,                               // **(°F)**
                "thsw_index":5.5,                              // **(°F)**
                "wind_speed_last":2,                           // most recent valid wind speed **(mph)**
                "wind_dir_last":null,                          // most recent valid wind direction **(°degree)**
                "wind_speed_avg_last_1_min":4,                 // average wind speed over last 1 min **(mph)**
                "wind_dir_scalar_avg_last_1_min":15,           // scalar average wind direction over last 1 min **(°degree)**
                "wind_speed_avg_last_2_min":42606,             // average wind speed over last 2 min **(mph)**
                "wind_dir_scalar_avg_last_2_min":170.7,        // scalar average wind direction over last 2 min **(°degree)**
                "wind_speed_hi_last_2_min":8,                  // maximum wind speed over last 2 min **(mph)**
                "wind_dir_at_hi_speed_last_2_min":0.0,         // gust wind direction over last 2 min **(°degree)**
                "wind_speed_avg_last_10_min":42606,            // average wind speed over last 10 min **(mph)**
                "wind_dir_scalar_avg_last_10_min":4822.5,      // scalar average wind direction over last 10 min **(°degree)**
                "wind_speed_hi_last_10_min":8,                 // maximum wind speed over last 10 min **(mph)**
                "wind_dir_at_hi_speed_last_10_min":0.0,        // gust wind direction over last 10 min **(°degree)**
                "rain_size":2,                                 // rain collector type/size **(0: Reserved, 1: 0.01", 2: 0.2 mm, 3:  0.1 mm, 4: 0.001")**
                "rain_rate_last":0,                            // most recent valid rain rate **(counts/hour)**
                "rain_rate_hi":null,                           // highest rain rate over last 1 min **(counts/hour)**
                "rainfall_last_15_min":null,                   // total rain count over last 15 min **(counts)**
                "rain_rate_hi_last_15_min":0,                  // highest rain rate over last 15 min **(counts/hour)**
                "rainfall_last_60_min":null,                   // total rain count for last 60 min **(counts)**
                "rainfall_last_24_hr":null,                    // total rain count for last 24 hours **(counts)**
                "rain_storm":null,                             // total rain count since last 24 hour long break in rain **(counts)**
                "rain_storm_start_at":null,                    // UNIX timestamp of current rain storm start **(seconds)**
                "solar_rad":747,                               // most recent solar radiation **(W/m²)**
                "uv_index":5.5,                                // most recent UV index **(Index)**
                "rx_state":2,                                  // configured radio receiver state **(no unit)**
                "trans_battery_flag":0,                        // transmitter battery status flag **(no unit)**
                "rainfall_daily":63,                           // total rain count since local midnight **(counts)**
                "rainfall_monthly":63,                         // total rain count since first of month at local midnight **(counts)**
                "rainfall_year":63,                            // total rain count since first of user-chosen month at local midnight **(counts)**
                "rain_storm_last":null,                        // total rain count since last 24 hour long break in rain **(counts)**
                "rain_storm_last_start_at":null,               // UNIX timestamp of last rain storm start **(sec)**
                "rain_storm_last_end_at":null                  // UNIX timestamp of last rain storm end **(sec)**
            },
            {
                "lsid":3187671188,
                "data_structure_type":2,
                "txid":3,
                "temp_1":null,                                 // most recent valid soil temp slot 1 **(°F)**
                "temp_2":null,                                 // most recent valid soil temp slot 2 **(°F)**
                "temp_3":null,                                 // most recent valid soil temp slot 3 **(°F)**
                "temp_4":null,                                 // most recent valid soil temp slot 4 **(°F)**
                "moist_soil_1":null,                           // most recent valid soil moisture slot 1 **(|cb|)**
                "moist_soil_2":null,                           // most recent valid soil moisture slot 2 **(|cb|)**
                "moist_soil_3":null,                           // most recent valid soil moisture slot 3 **(|cb|)**
                "moist_soil_4":null,                           // most recent valid soil moisture slot 4 **(|cb|)**
                "wet_leaf_1":null,                             // most recent valid leaf wetness slot 1 **(no unit)**
                "wet_leaf_2":null,                             // most recent valid leaf wetness slot 2 **(no unit)**
                "rx_state":null,                               // configured radio receiver state **(no unit)**
                "trans_battery_flag":null                      // transmitter battery status flag **(no unit)**
            },
            {
                "lsid":48307,
                "data_structure_type":4,
                "temp_in":78.0,                                // most recent valid inside temp **(°F)**
                "hum_in":41.1,                                 // most recent valid inside humidity **(%RH)**
                "dew_point_in":7.8,                            // **(°F)**
                "heat_index_in":8.4                            // **(°F)**
            },
            {
                "lsid":48306,
                "data_structure_type":3,
                "bar_sea_level":30.008,                        // most recent bar sensor reading with elevation adjustment **(inches)**
                "bar_trend":null,                              // current 3 hour bar trend **(inches)**
                "bar_absolute":30.008                          // raw bar sensor reading **(inches)**
            }
        ]
    },
    "error":null
}
Receiver State
The rx_state field describes the radio reception state for the transmitter.

Value	Name	Meaning	VP2 Console Display Equivalent
0	Synched & Tracking	Transmitter has been acquired and is actively being received.	Blinking “X”
1	Synched	Transmitter has been acquired, but we have missed 1-14 packets in a row.	“X” not blinking when expected
2	Scanning	Transmitter has not been acquired yet, or we’ve lost it (more than 15 missed packets in a row).	“R” reacquisition mode
In the “Synched” state the radio expects to hear from the transmitter in the future. The radio can miss a packet due to external radio interference or if two transmitters happen to transmit at the same time and the radio can only receive one of the packets.

In the “Scanning” state the radio does not have any synchronization with the transmitter. The radio will actively look for unacquired transmitters in this state.

Transmitter Battery Status
The trans_battery_flag field describes the current status of the transmitter’s CR-123A battery. A value of 1 indicates the battery is low, while a value of 0 indicates that the battery is okay.

Note: the battery status measurement may cross over from low to okay and back again throughout the day depending on the state of the solar panel and super-capacitor. For best results, check the battery status when the solar panel is not producing power.