
import sys

import pynvml
import os

from carbontracker import exceptions
from carbontracker.components.handler import Handler
from typing import List, Union


class NvidiaGPU(Handler):
    def __init__(self, pids: List[int], devices_by_pid: bool):
        super().__init__(pids, devices_by_pid)
        self._handles = []

    def devices(self) -> List[str]:
        pass

    def available(self) -> bool:
        pass

    def power_usage(self) -> List[float]:
        pass

    def init(self):
        pass

    def shutdown(self):
        pass

    def _get_handles(self) -> List:
        pass

    def _slurm_gpu_indices(self) -> Union[List[int], None]:
        pass

    def _get_handles_by_pid(self) -> List:
        pass
