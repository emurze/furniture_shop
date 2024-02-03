from datetime import date, timedelta

import pytest

from modules.allocation.domain.exceptions import OutOfStock
from modules.allocation.domain.models import Batch, OrderLine
from modules.allocation.domain.services import allocate

tomorrow = date.today() + timedelta(days=1)


def test_allocate_can_allocate_earliest_batch() -> None:
    """
    line -> allocate() -> [batch1, batch2, batch3, batch4]
    deliver batch1 or part of batch1
    """

    in_stock_batch = Batch(
        reference=1,
        CKU="RETRO-CLOCK",
        purchased_quantity=100,
        ETA=None,
    )
    shipment_batch = Batch(
        reference=2,
        CKU="RETRO-CLOCK",
        purchased_quantity=100,
        ETA=tomorrow,
    )
    line = OrderLine(order_ref=1, CKU="RETRO-CLOCK", quantity=10)

    res_batch_ref = allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.reference == res_batch_ref
    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_allocate_cannot_allocate_batches() -> None:
    in_stock_batch = Batch(
        reference=1,
        CKU="RETRO-CLOCK",
        purchased_quantity=5,
        ETA=None,
    )
    shipment_batch = Batch(
        reference=2,
        CKU="RETRO-CLOCK",
        purchased_quantity=3,
        ETA=tomorrow,
    )
    line = OrderLine(order_ref=1, CKU="RETRO-CLOCK", quantity=10)

    with pytest.raises(OutOfStock, match="RETRO-CLOCK"):
        allocate(line, [in_stock_batch, shipment_batch])


