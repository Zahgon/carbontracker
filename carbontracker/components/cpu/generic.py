import cpuinfo
from carbontracker.components.handler import Handler
from typing import List, Optional
import csv
import os
from carbontracker.loggerutil import Logger
import statistics

logger = Logger()

class GenericCPU(Handler):
    def __init__(self, pids: List[int], devices_by_pid: bool):
        super().__init__(pids, devices_by_pid)
        self.cpu_brand = self.get_cpu_brand()
        self.tdp = None
        self.cpu_power_data = self.load_cpu_power_data()
        self.average_tdp = self.calculate_average_tdp()

    def get_cpu_brand(self) -> str:
        pass

    def load_cpu_power_data(self):
        pass

    def calculate_average_tdp(self) -> float:
        pass

    def init(self):
        pass

    def find_matching_tdp(self) -> Optional[float]:
        pass

    def devices(self) -> List[str]:
        pass

    def available(self) -> bool:
        pass

    def power_usage(self) -> List[float]:
        pass

    def shutdown(self):
        pass
