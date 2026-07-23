import argparse
import subprocess
from carbontracker.tracker import CarbonTracker
from carbontracker import parser
from carbontracker.report import generate_report_from_log, REPORTLAB_AVAILABLE
import ast
import os


def parse_logs(log_dir):
    parser.print_aggregate(log_dir=log_dir)


def generate_report(log_file, output_pdf):
    pass


def main():
    pass


if __name__ == "__main__":
    main()