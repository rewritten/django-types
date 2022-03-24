from typing import Any, Callable, Dict, List, Optional

from django.http.request import HttpRequest
from django.template.base import Template as TemplateObject
from django.template.exceptions import TemplateSyntaxError

from .base import BaseEngine


class Jinja2(BaseEngine[Template]):
    context_processors: List[str] = ...
    def __init__(self, params: Dict[str, Any]) -> None: ...
    @property
    def template_context_processors(self) -> List[Callable[..., Any]]: ...

class Template:
    template: TemplateObject
    backend: Jinja2
    origin: Origin

    def __init__(self, template: TemplateObject, backend: Jinja2): ...

    def render(self, context: Optional[Dict[str, Any]] = ..., request: Optional[HttpRequest] = ...) -> str: ...

class Origin:
    name: str = ...
    template_name: Optional[str] = ...
    def __init__(self, name: str, template_name: Optional[str]) -> None: ...

def get_exception_info(exception: TemplateSyntaxError) -> Dict[str, Any]: ...
