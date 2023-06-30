from config import Config
from flights import Flights

wing_config = Config()
wing_config.set_config()

wing_flights = Flights(wing_config.flt_path)

wing_flights.write_load_cycles(wing_config.flts_per_block, wing_config.block, wing_config.logs, 0, "WING", "BMX", "ROOT")
