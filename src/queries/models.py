import datetime
from typing import Literal, Annotated

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, str256

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
    )
]
updated_at = Annotated[
    datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        default=datetime.datetime.utcnow,
    )
]


class WorkerModel(Base):
    __tablename__ = 'worker'

    id: Mapped[intpk]
    name: Mapped[str256]


class ResumeModel(Base):
    __tablename__ = 'resume'

    id: Mapped[intpk]
    title: Mapped[str256]
    compensation: Mapped[int | None]
    workload: Mapped[Literal["parttime", 'fulltime']]
    worker_id: Mapped[int] = mapped_column(
        ForeignKey("worker.id", ondelete="CASCADE")
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


worker_metadata = WorkerModel.metadata
resume_metadata = ResumeModel.metadata
