from typing import Optional
import requests

from carbontracker import exceptions
from carbontracker.emissions.intensity.fetcher import IntensityFetch, IntensityFetcher

API_URL = "https://api-access.electricitymaps.com/free-tier/carbon-intensity/latest"


class ElectricityMap(IntensityFetcher):
    id = "electricitymaps"

    def __init__(self, logger, api_key: str):
        self.logger = logger
        self._api_key = api_key

    def suitable(self, g_location):
        pass
    def fetch_carbon_intensity(self, g_location, time_dur=None) -> IntensityFetch:
        pass
 

    def _carbon_intensity_by_location(self, lon=None, lat=None, zone=None,) -> float:
        pass
