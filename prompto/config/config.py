from typing import Optional
import os

class PromptoConfig:
    _environment: Optional[str]
    _server_url: Optional[str]

    def __init__(self,
                    environment: Optional[str] = None,
                    server_url: Optional[str] = None):
            
            self._environment = environment
            self._server_url = server_url

    @property
    def server_url(self) -> Optional[str]:
        if (self._server_url is None):
            return os.environ.get("PROMPT_HUB_SERVER_URL"
        return self._server_url

    @server_url.setter
    def server_url(self, value: Optional[str]):
        self._server_url = value

    
prompto_config = PromptoConfig()