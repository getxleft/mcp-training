from abc import ABC

from mcp_training.commons.service.service_status import ServiceStatus
from mcp_training.commons.service.shutdown_order import ShutdownOrder
from src.mcp_training.commons.service.initialization_order import InitializationOrder

class ManagedService(ABC):

    def __init__(self,
                    initialization_order: InitializationOrder = InitializationOrder.CORE,
                    shutdown_order: ShutdownOrder = ShutdownOrder.APPLICATION,
                    service_status: ServiceStatus = ServiceStatus.INITIALIZING,
                    shutdown_timeout: float = 30.0,
                    initialization_timeout: float = 60.0):

        self._initialization_order = initialization_order
        self._shutdown_order = shutdown_order
        self._service_status = service_status
        self._shutdown_timeout = shutdown_timeout
        self._initialization_timeout = initialization_timeout

    