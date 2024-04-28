import requests
from typing import Dict, Any
from .classes import Prompt

from prompto.config import prompto_config

class Prompto:
    def __init__(self):
        self.options = prompto_config

    def get(self, prompt_namespace: str, prompt_name: str, version: str = "LATEST") -> Dict[str, Any]:

        url = f"https://{self.options.server_url}/prompt/{prompt_namespace}/{prompt_name}"

        params = {
            "version": version
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if not response.ok:
            raise Exception(data.get("message", f"Erorr fetching prompt {prompt_name} in namespace {prompt_namespace}"))
        
        prompt = Prompt(
            namespace = data.get("namespace"),
            team = data.get("team"),
            name = data.get("name"),
            prompt_text = data.get("prompt_text"),
            interpolation_values = data.get("interpolation_values", list()),
            description = data.get("description", None),
            tags = data.get("tags", list()),
            meta = data.get("meta", None),
            version = data.get("version")
        )

        return prompt
    
prompto = Prompto()