import enum


class InitializationOrder(enum.IntEnum):
    """
        - 1-10: Application services (API handlers, workers)
        - 11-20: Mid-tier services (caches, queues)
        - 21-30: Infrastructure services (databases, connections)
        - 31-40: Core services (logs, monitoring)
        """
    APPLICATION = 5
    MID_TIER = 15
    INFRASTRUCTURE = 25
    CORE = 35
