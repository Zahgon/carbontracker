import os
import sys
import time
import traceback
import psutil
import math
import json
from threading import Thread, Event
from typing import List, Optional, Union
import importlib.resources as pkg_resources

from carbontracker.emissions.intensity.fetcher import IntensityFetcher
from carbontracker.emissions.intensity.intensity import IntensityService, IntensityFetch
import numpy as np
from random import randint

from carbontracker import constants
from carbontracker import loggerutil
from carbontracker import predictor
from carbontracker import exceptions
from carbontracker.components import component
from carbontracker.components.component import Component
from carbontracker.emissions.conversion import co2eq
from carbontracker.emissions.intensity.fetchers import electricitymaps
from carbontracker.emissions.intensity.fetchers import energidataservice
from carbontracker.emissions.intensity.fetchers import carbonintensitygb 


class CarbonIntensityThread(Thread):

    def __init__(self, logger : loggerutil.Logger, stop_event, intensity_fetcher: Optional[IntensityFetcher] = None, update_interval: Union[float, int] = 900,):
        super(CarbonIntensityThread, self).__init__()
        self.name = "CarbonIntensityThread"
        self.logger = logger
        self.update_interval: Union[float, int] = update_interval
        self.daemon = True
        self.stop_event = stop_event
        self.carbon_intensities_fetches : List[IntensityFetch] = []
        self.carbon_intensity_service = IntensityService(
            logger=self.logger,
            intensity_fetcher=intensity_fetcher
        )
        self.start()

    def run(self):
        pass

    def _fetch_carbon_intensity(self):
        pass


    def predict_carbon_intensity(self, pred_time_dur) -> float:
        pass

    def average_carbon_intensity(self) -> float :
        pass


class CarbonTrackerThread(Thread):

    def __init__(
        self,
        components: List[Component],
        logger,
        ignore_errors,
        delete,
        update_interval: Union[int, float] = 1,
    ):
        super(CarbonTrackerThread, self).__init__()
        self.cur_epoch_time = time.time()
        self.name = "CarbonTrackerThread"
        self.delete = delete
        self.components = components
        self.update_interval = update_interval
        self.ignore_errors = ignore_errors
        self.logger = logger
        self.epoch_times = []
        self.running = True
        self.measuring_event = Event()
        self.epoch_counter = 0
        self.daemon = True

        self.start()

    def run(self):
        pass

    def begin(self):
        pass

    def stop(self):
        pass

    def epoch_start(self):
        pass

    def epoch_end(self):
        pass

    def _log_components_info(self):
        pass

    def _log_epoch_measurements(self):
        pass

    def _components_remove_unavailable(self):
        pass

    def _components_init(self):
        pass

    def _components_shutdown(self):
        pass

    def _collect_measurements(self):
        pass

    def total_energy_per_epoch(self):
        pass

    def _handle_error(self, error):
        pass


class CarbonTracker:

    def __init__(
        self,
        epochs,
        epochs_before_pred=1,
        monitor_epochs=-1,
        update_interval=1,
        interpretable=True,
        stop_and_confirm=False,
        ignore_errors=False,
        components="all",
        devices_by_pid=False,
        log_dir=None,
        log_file_prefix="",
        verbose=1,
        decimal_precision=12,
        api_keys=None,
        sim_cpu=None,
        sim_cpu_tdp=None,
        sim_cpu_util=None,
        sim_gpu=None,
        sim_gpu_watts=None,
        sim_gpu_util=None
    ):
        """Initialize CarbonTracker.

        Args:
            epochs (int): Total epochs of your training loop.
            epochs_before_pred (int, optional): Number of epochs to monitor before making predictions. Defaults to 1.
            monitor_epochs (int, optional): Number of epochs to monitor. Defaults to -1.
            update_interval (int, optional): Interval in seconds between measurements. Defaults to 1.
            interpretable (bool, optional): Whether to make predictions interpretable. Defaults to True.
            stop_and_confirm (bool, optional): Whether to stop and confirm before making predictions. Defaults to False.
            ignore_errors (bool, optional): Whether to ignore errors. Defaults to False.
            components (str, optional): Components to monitor. Defaults to "all".
            devices_by_pid (bool, optional): Whether to monitor devices by PID. Defaults to False.
            log_dir (str, optional): Directory to store logs. Defaults to None.
            log_file_prefix (str, optional): Prefix for log files. Defaults to "".
            verbose (int, optional): Verbosity level. Defaults to 1.
            decimal_precision (int, optional): Decimal precision for measurements. Defaults to 12.
            api_keys (dict, optional): API keys for external services. Defaults to None.
            sim_cpu (str, optional): Simulated CPU name. Defaults to None.
            sim_cpu_tdp (float, optional): Simulated CPU TDP in Watts. Defaults to None.
            sim_cpu_util (float, optional): Simulated CPU utilization. Defaults to None.
            sim_gpu (str, optional): Simulated GPU name. Defaults to None.
            sim_gpu_watts (float, optional): Simulated GPU power consumption in Watts. Defaults to None.
            sim_gpu_util (float, optional): Simulated GPU utilization. Defaults to None.
        """

        if monitor_epochs != -1:
            if monitor_epochs < epochs_before_pred:
                raise ValueError("monitor_epochs cannot be less than epochs_before_pred")
            if monitor_epochs == 0:
                raise ValueError("monitor_epochs cannot be zero")
        else:
            monitor_epochs = epochs
        if sim_cpu is not None and sim_cpu_tdp is None:
            raise ValueError("When using simulated CPU (sim_cpu), you must also specify the CPU TDP (sim_cpu_tdp)")
        if sim_gpu is not None and sim_gpu_watts is None:
            raise ValueError("When using simulated GPU (sim_gpu), you must also specify the GPU power consumption (sim_gpu_watts)")

        self.epochs = epochs
        self.epochs_before_pred = epochs_before_pred
        self.monitor_epochs = monitor_epochs
        self.update_interval = update_interval
        self.interpretable = interpretable
        self.stop_and_confirm = stop_and_confirm
        self.ignore_errors = ignore_errors
        self.components = components
        self.devices_by_pid = devices_by_pid
        self.log_dir = log_dir
        self.log_file_prefix = log_file_prefix
        self.verbose = verbose
        self.decimal_precision = decimal_precision
        self.api_keys = api_keys
        self.sim_cpu = sim_cpu
        self.sim_cpu_tdp = sim_cpu_tdp
        self.sim_cpu_util = sim_cpu_util
        self.sim_gpu = sim_gpu
        self.sim_gpu_watts = sim_gpu_watts
        self.sim_gpu_util = sim_gpu_util
        self.deleted = False
        self.epoch_counter = 0
        self.intensity_fetcher = None

        try:
            pids = self._get_pids()
            self.logger = loggerutil.Logger(
                log_dir=log_dir,
                verbose=verbose,
                log_prefix=log_file_prefix,
                logger_id=str(randint(1, 999999)),
            )
            self.tracker = CarbonTrackerThread(
                delete=self._delete,
                components=component.create_components(
                    components=components, pids=pids, devices_by_pid=devices_by_pid, logger=self.logger, sim_cpu=self.sim_cpu, sim_cpu_tdp=self.sim_cpu_tdp, sim_cpu_util=self.sim_cpu_util, sim_gpu=self.sim_gpu, sim_gpu_watts=self.sim_gpu_watts, sim_gpu_util=self.sim_gpu_util
                ),
                logger=self.logger,
                ignore_errors=ignore_errors,
                update_interval=update_interval,
            )
            self.intensity_stopper = Event()
            self.intensity_updater = CarbonIntensityThread(
                logger=self.logger, 
                stop_event=self.intensity_stopper,
                intensity_fetcher=self._get_fetcher()
            )
        except Exception as e:
            self._handle_error(e)

    def epoch_start(self):
        pass

    def epoch_end(self):
        pass

    def stop(self):
        pass

    def set_api_keys(self, api_keys):
        pass

    def _handle_error(self, error):
        pass

    def _output_energy(self, description, time, energy, co2eq, conversions):
        pass

    def _output_actual(self):
        pass

    def _output_pred(self):
        pass

    def _co2eq(self, energy_usage, pred_time_dur=None) -> float:
        pass

    def _user_query(self):
        pass

    def _check_input(self, user_input: str):
        pass

    def _delete(self):
        pass

    def _get_pids(self) -> List[int]:
        pass

    def _get_fetcher(self) -> Optional[IntensityFetcher]:
        pass
