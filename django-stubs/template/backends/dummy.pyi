import string
from typing import Any, Dict, List, Optional, Tuple, Union

from django.http.request import HttpRequest

from .base import BaseEngine

class TemplateStrings(BaseEngine[Template]):
    template_dirs: Tuple[str]
    def __init__(
        self, params: Dict[str, Union[Dict[Any, Any], List[Any], bool, str]]
    ) -> None: ...

class Template(string.Template):
    def render(
        self,
        context: Optional[Dict[str, Any]] = ...,
        request: Optional[HttpRequest] = ...,
    ) -> str: ...
