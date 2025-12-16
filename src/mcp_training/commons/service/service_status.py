import enum


class ServiceStatus(enum.Enum):
    INITIALIZING = 0
    RUNNING = 1
    STOPPING = 2
    STOPPED = 3
    FAILED = 4