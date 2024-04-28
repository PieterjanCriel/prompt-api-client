from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Meta:
    authors: List[str]

@dataclass
class Prompt:
    namespace: str
    team: str
    name: str
    prompt_text: str
    interpolation_values: Optional[List[str]]
    description: Optional[str]
    tags: Optional[List[str]]
    meta: Optional[Meta]
    version: str
