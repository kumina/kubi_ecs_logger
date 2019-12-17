import json
import sys

from kubi_ecs_logger.models import Severity


def pprint(data: dict, output_destination=sys.stdout):
    """
    Prints the data in a formatted way with colors
    """
    severity = Severity.from_str(data["logline"]["level"])
    raw_data = ConsoleColors.get_color(severity) + json.dumps(data, indent=2, sort_keys=True) + ConsoleColors.ENDC
    print(raw_data, file=output_destination)


class ConsoleColors:
    GREY = '\033[37m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    DARK_RED = '\033[31m'
    ENDC = '\033[0m'

    @staticmethod
    def get_color(severity: Severity):
        if severity == Severity.DEBUG:
            return ConsoleColors.GREY
        if severity == Severity.INFO:
            return ConsoleColors.CYAN
        if severity == Severity.WARNING:
            return ConsoleColors.YELLOW
        if severity == Severity.ERROR:
            return ConsoleColors.RED
        if severity == Severity.CRITICAL:
            return ConsoleColors.DARK_RED
