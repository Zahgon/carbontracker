import sys
import pandas as pd
from carbontracker.emissions.intensity.fetchers import electricitymaps
import geocoder
import traceback
from typing import List, Optional, Tuple, Type
from carbontracker import constants, exceptions, loggerutil
from carbontracker.emissions.intensity.fetcher import IntensityFetch, IntensityFetcher
from carbontracker.emissions.intensity.location import Location



class IntensityService():
    def __init__(self,
                 logger : loggerutil.Logger,
                 intensity_fetcher : Optional[IntensityFetcher] = None,
                 ) -> None:
        self.logger = logger 
        self.intensity_fetcher = intensity_fetcher
        self.geo_location = self._fetch_geo_location()
        self.address = self._get_address()
        self.country = self._get_country()
        self.using_global_average = False
        self.default_carbon_intensity = self._get_default_carbon_intensity()
        self._log_state()

                 
    def fetch_carbon_intensity(self, time_duration = None) -> IntensityFetch:
        pass
        
    def _get_default_carbon_intensity(self) -> IntensityFetch:
        pass
  
    def _fetch_geo_location(self) -> Optional[Location]: 
            pass
    
    def _get_address(self) -> str: 
        pass
     
    def _get_country(self) -> str: 
        pass

    def _log_state(self):
        pass

    def _log_fetch_failed(self):
        pass

