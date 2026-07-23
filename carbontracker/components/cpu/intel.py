import os
import re
import time

from carbontracker import exceptions
from carbontracker.components.handler import Handler
from typing import List, Union


RAPL_DIR = "/sys/class/powercap/"
CPU = 0
DRAM = 2
MEASURE_DELAY = 1


class IntelCPU(Handler):
    def __init__(self, pids: List, devices_by_pid: bool):
        super().__init__(pids, devices_by_pid)
        self._handler = None

    def devices(self) -> List[str]:
        pass

    def available(self) -> bool:
        pass

    def power_usage(self) -> List[float]:
        pass

    def _compute_power(self, before: int, after: int) -> float:
        pass

    def _read_energy(self, path: str) -> int:
        pass

    def _get_measurements(self):
        pass

    def _convert_rapl_name(self, package, name, pattern) -> Union[None, str]:
        pass

    def init(self):
        pass

    def shutdown(self):
        pass
