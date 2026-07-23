import datetime
from typing import TYPE_CHECKING, List

import numpy as np
import requests

from carbontracker import exceptions
from carbontracker.emissions.intensity.fetcher import IntensityFetch, IntensityFetcher

if TYPE_CHECKING:
    from carbontracker.loggerutil import Logger

CURRENT_DATASET = "CO2emis"
PROGNOSIS_DATASET = "CO2Emis"
BASE_URL = "https://api.energidataservice.dk/dataset"


class EnergiDataService(IntensityFetcher):
    id = "energidataservice"

    def __init__(self, logger: "Logger"):
        super().__init__(logger=logger)

    def suitable(self, g_location):
        pass

    def fetch_carbon_intensity(self, g_location, time_dur=None) -> IntensityFetch:
        pass

    def _emission_current(self) -> float:
        pass

    def _emission_prognosis(self, time_dur: int) -> float:
        pass

    def _interval(self, time_dur: int):
        pass

    def _nearest_5_min(self, time):
        pass

    def _raise_for_bad_response(self, response):
        pass
