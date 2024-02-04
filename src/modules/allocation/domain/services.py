from collections.abc import Sequence

from modules.allocation.domain.exceptions import OutOfStock
from modules.allocation.domain.models import Batch, OrderLine


def allocate(line: OrderLine, batches: Sequence[Batch]) -> int:
    try:
        batch = next(
            earliest_batch
            for earliest_batch in sorted(batches)
            if earliest_batch.can_allocate(line)
        )
    except StopIteration:
        raise OutOfStock(line.CKU)

    batch.allocate(line)
    return batch.reference
