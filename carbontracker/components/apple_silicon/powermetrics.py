import platform
import subprocess
import re
import time
from carbontracker.components.handler import Handler
from typing import Union, List, Pattern


class PowerMetricsUnified:
    _output: Union[None, str] = None
    _last_updated: Union[None, float] = None

    @staticmethod
    def get_output():
        pass


class AppleSiliconCPU(Handler):
    def init(self, pids=None, devices_by_pid=False):
        pass

    def shutdown(self):
        pass

    def devices(self) -> List[str]:
        pass

    def available(self) -> bool:
        pass

    def power_usage(self) -> List[float]:
        pass

    def parse_power(self, output: str, pattern: Pattern[str]) -> float:
        pass


class AppleSiliconGPU(Handler):
    def init(self, pids=None, devices_by_pid=False):
        pass

    def devices(self) -> List[str]:
        pass

    def available(self) -> bool:
        pass

    def power_usage(self):
        pass

    def parse_power(self, output: str, pattern: Pattern[str]) -> float:
        pass
        
    def shutdown(self):
        pass
