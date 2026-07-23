from carbontracker.components.handler import Handler
from typing import List

class SimulatedCPUHandler(Handler):
    def __init__(self, name: str, tdp: float, utilization: float = 0.5):
        super().__init__(pids=[], devices_by_pid=False)
        if not isinstance(name, str) or not name.strip():
            raise ValueError("CPU name must be a non-empty string.")
        if tdp is None or not isinstance(tdp, (int, float)) or tdp < 0:
            raise ValueError("CPU TDP must be a non-negative number.")
        if not isinstance(utilization, (int, float)) or not (0.0 <= utilization <= 1.0):
            raise ValueError("CPU utilization must be between 0.0 and 1.0.")
        self.cpu_brand = name
        self.utilization = utilization
        self.tdp = tdp * utilization

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