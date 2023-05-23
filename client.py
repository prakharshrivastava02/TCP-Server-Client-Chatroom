import logging
from spyder.plugins.completion.providers.languageserver.transport.common.consumer import (
    IncomingMessageThread)

logger = logging.getLogger(__name__)


class TCPIncomingMessageThread(IncomingMessageThread):
    """TCP socket consumer."""

    def read_num_bytes(self, n):
        return self.fd.recv(n)
