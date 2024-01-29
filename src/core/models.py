from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class WorkerModel(Base):
    __tablename__ = 'worker'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


worker_metadata = WorkerModel.metadata
