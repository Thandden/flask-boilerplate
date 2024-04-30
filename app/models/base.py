from typing import Optional

from sqlmodel import (
    Field,  # type: ignore
    SQLModel,
)


class Foo(SQLModel, table=True):  # type: ignore
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
