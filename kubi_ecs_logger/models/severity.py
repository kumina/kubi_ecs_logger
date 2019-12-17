from enum import Enum


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Severity(OrderedEnum):
    CRITICAL = 5
    ERROR = 4
    WARNING = 3
    INFO = 2
    DEBUG = 1

    @staticmethod
    def from_str(severity_str: str) -> 'Severity':
        severity_str = severity_str.lower()
        if severity_str == "debug":
            return Severity.DEBUG
        elif severity_str == "info":
            return Severity.INFO
        elif severity_str == "warning":
            return Severity.WARNING
        elif severity_str == "error":
            return Severity.ERROR
        elif severity_str == "critical":
            return Severity.CRITICAL
        else:
            raise AssertionError(f"Invalid severity - {severity_str}")
