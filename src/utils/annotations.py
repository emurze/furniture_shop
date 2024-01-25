from typing import Annotated

from pydantic import Field

Str = Annotated[str, Field(min_length=1)]
