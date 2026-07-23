import datetime
from typing import TYPE_CHECKING

import numpy as np
import requests

from carbontracker import exceptions
from carbontracker.emissions.intensity.fetcher import IntensityFetch, IntensityFetcher

if TYPE_CHECKING:
    from carbontracker.loggerutil import Logger

API_URL = "https://api.carbonintensity.org.uk"


class CarbonIntensityGB(IntensityFetcher):
    id = "carbonintensitygb"

    def __init__(self, logger: "Logger"):
        super().__init__(logger=logger)

    def suitable(self, g_location):
        pass

    def fetch_carbon_intensity(self, g_location, time_dur=None) -> IntensityFetch:
        pass

    def _carbon_intensity_gb_regional(self, postcode, time_dur=None) -> float:
        pass

    def _carbon_intensity_gb_national(self, time_dur=None) -> float:
        pass

    def _time_from_to_str(self, time_dur):
        pass

    def _raise_for_bad_response(self, response):
        pass
