from datetime import datetime
from typing import TypeAlias

from modules.allocation.domain.models import Batch, OrderLine

BatchAndLine: TypeAlias = tuple[Batch, OrderLine]


def make_line_and_batch(batch_qty: int, line_qty: int) -> BatchAndLine:
    return (
        Batch(
            reference="1",
            CKU="RED CHAIR",
            purchased_quantity=batch_qty,
            eta=datetime.today(),
        ),
        OrderLine(order_ref="1", CKU="RED CHAIR", quantity=line_qty),
    )


def test_order_line_to_batch_allocation_reduces_available_quantity() -> None:
    batch, line = make_line_and_batch(batch_qty=10, line_qty=4)
    batch.allocate(line)
    assert batch.available_quantity == 6


def test_cannot_allocate_order_line_to_batch_different_sku() -> None:
    batch = Batch(reference="1", CKU="BLUE CHAIR", purchased_quantity=10)
    line = OrderLine(order_ref="5", CKU="RED CHAIR", quantity=4)
    batch.allocate(line)
    assert batch.available_quantity == 10


def test_cannot_allocate_the_same_order_line_to_batch_twice() -> None:
    batch, line = make_line_and_batch(batch_qty=10, line_qty=4)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 6


def test_cannot_allocate_if_line_quantity_more_than_batch_quantity() -> None:
    batch, line = make_line_and_batch(batch_qty=10, line_qty=11)
    batch.allocate(line)
    assert batch.available_quantity == 10


def test_can_allocate_if_line_quantity_equal_to_batch_quantity() -> None:
    batch, line = make_line_and_batch(batch_qty=10, line_qty=10)
    batch.allocate(line)
    assert batch.available_quantity == 0


def test_can_allocate_if_line_quantity_less_than_batch_quantity() -> None:
    batch, line = make_line_and_batch(batch_qty=10, line_qty=6)
    batch.allocate(line)
    assert batch.available_quantity == 4


def test_can_deallocate_line_from_batch() -> None:
    batch, line = make_line_and_batch(batch_qty=10, line_qty=6)
    batch.allocate(line)
    batch.deallocate(line)
    assert batch.available_quantity == 10


def test_batch_can_go_to_set() -> None:
    batch = Batch(reference="1", CKU="BLUE CHAIR", purchased_quantity=10)
    s = set()
    s.add(batch)


def test_order_line_can_go_to_set() -> None:
    line = OrderLine(order_ref="5", CKU="RED CHAIR", quantity=4)
    set(line)
