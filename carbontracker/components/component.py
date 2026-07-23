import numpy as np

from carbontracker import exceptions
from carbontracker.components.gpu import nvidia
from carbontracker.components.cpu import intel, generic
from carbontracker.components.apple_silicon.powermetrics import (
    AppleSiliconCPU,
    AppleSiliconGPU,
)
from carbontracker.components.handler import Handler
from typing import Iterable, List, Union, Type, Sized
from carbontracker.loggerutil import Logger
import os
from carbontracker.components.cpu.sim_cpu import SimulatedCPUHandler
from carbontracker.components.gpu.sim_gpu import SimulatedGPUHandler

COMPONENTS = [
    {
        "name": "gpu",
        "error": exceptions.GPUError("No GPU(s) available."),
        "handlers": [nvidia.NvidiaGPU, AppleSiliconGPU],
    },
    {
        "name": "cpu",
        "error": exceptions.CPUError("No CPU(s) available."),
        "handlers": [intel.IntelCPU, AppleSiliconCPU, generic.GenericCPU],
    },
]


def component_names() -> List[str]:
    return [comp["name"] for comp in COMPONENTS]


def error_by_name(name) -> Exception:
    for comp in COMPONENTS:
        if comp["name"] == name:
            return comp["error"]
    raise exceptions.ComponentNameError()


def handlers_by_name(
    name, 
    sim_cpu=None, 
    sim_cpu_tdp=None, 
    sim_cpu_util=None,
    sim_gpu=None, 
    sim_gpu_watts=None,
    sim_gpu_util=None
):
    pass


class Component:
    def __init__(
        self, 
        name: str, 
        pids: Iterable[int], 
        devices_by_pid: bool, 
        logger: Logger, 
        sim_cpu=None,
        sim_cpu_tdp=None,
        sim_cpu_util=None,
        sim_gpu=None,
        sim_gpu_watts=None,
        sim_gpu_util=None
    ):
        self.name = name
        if name not in component_names():
            raise exceptions.ComponentNameError(
                f"No component found with name '{self.name}'."
            )
        self._handler = self._determine_handler(
            pids=pids, 
            devices_by_pid=devices_by_pid, 
            sim_cpu=sim_cpu,
            sim_cpu_tdp=sim_cpu_tdp,
            sim_cpu_util=sim_cpu_util,
            sim_gpu=sim_gpu,
            sim_gpu_watts=sim_gpu_watts,
            sim_gpu_util=sim_gpu_util
        )
        self.power_usages: List[List[float]] = []
        self.cur_epoch: int = -1
        self.logger = logger

    @property
    def handler(self) -> Handler:
        pass

    def _determine_handler(
        self, 
        pids: Iterable[int], 
        devices_by_pid: bool, 
        sim_cpu=None,
        sim_cpu_tdp=None,
        sim_cpu_util=None,
        sim_gpu=None,
        sim_gpu_watts=None,
        sim_gpu_util=None
    ) -> Union[Handler, None]:
        pass

    def devices(self) -> List[str]:
        pass

    def available(self) -> bool:
        pass

    def collect_power_usage(self, epoch: int):
        pass

    def energy_usage(self, epoch_times: List[int]) -> List[int]:
        pass

    def init(self):
        pass

    def shutdown(self):
        pass


def create_components(
    components: str, 
    pids: Iterable[int], 
    devices_by_pid: bool, 
    logger: Logger, 
    sim_cpu=None,
    sim_cpu_tdp=None,
    sim_cpu_util=None,
    sim_gpu=None,
    sim_gpu_watts=None,
    sim_gpu_util=None
) -> List[Component]:
    components = components.strip().replace(" ", "").lower()
    if components == "all":
        return [
            Component(
                name=comp_name, 
                pids=pids, 
                devices_by_pid=devices_by_pid, 
                logger=logger, 
                sim_cpu=sim_cpu,
                sim_cpu_tdp=sim_cpu_tdp,
                sim_cpu_util=sim_cpu_util,
                sim_gpu=sim_gpu,
                sim_gpu_watts=sim_gpu_watts,
                sim_gpu_util=sim_gpu_util
            )
            for comp_name in component_names()
        ]
    else:
        return [
            Component(
                name=comp_name, 
                pids=pids, 
                devices_by_pid=devices_by_pid, 
                logger=logger, 
                sim_cpu=sim_cpu,
                sim_cpu_tdp=sim_cpu_tdp,
                sim_cpu_util=sim_cpu_util,
                sim_gpu=sim_gpu,
                sim_gpu_watts=sim_gpu_watts,
                sim_gpu_util=sim_gpu_util
            )
            for comp_name in components.split(",")
        ]
