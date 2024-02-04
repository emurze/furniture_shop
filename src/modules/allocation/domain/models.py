import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from modules.allocation.domain.exceptions import \
    BatchGtSupportedOnlyForBatchError


class Model(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class OrderLine(Model, frozen=True):
    order_ref: str
    CKU: str
    quantity: int

    def __hash__(self) -> int:
        return hash((self.order_ref, self.CKU, self.quantity))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderLine):
            return False
        return all(
            [
                self.order_ref == other.order_ref,
                self.CKU == other.CKU,
                self.quantity == other.quantity,
            ]
        )


class Batch(Model):
    reference: str = Field(frozen=True)
    CKU: str
    purchased_quantity: int
    ETA: Optional[datetime.datetime] = None
    allocated_lines: set[OrderLine] = Field(default_factory=set)

    def __hash__(self) -> int:
        return hash(self.reference)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Batch):
            return False
        return self.reference == other.reference

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Batch):
            raise BatchGtSupportedOnlyForBatchError()

        if self.ETA is None:
            return False

        if other.ETA is None:
            return True

        return self.ETA >= other.ETA

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self.allocated_lines)

    @property
    def available_quantity(self) -> int:
        return self.purchased_quantity - self.allocated_quantity

    def is_allocated_line(self, line: OrderLine) -> bool:
        return line in self.allocated_lines

    def can_allocate(self, line: OrderLine) -> bool:
        return all(
            [
                self.available_quantity >= line.quantity,
                line.CKU == self.CKU,
            ]
        )

    def deallocate(self, line: OrderLine) -> None:
        if self.is_allocated_line(line):
            self.allocated_lines.remove(line)

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self.allocated_lines.add(line)
