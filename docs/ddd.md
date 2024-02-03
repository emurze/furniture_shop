# Domain Features

* ```__hash__ and __eq__``` for using in set and dict keys

```python
# Entity

class Batch(Model):
    reference: int = Field(frozen=True)
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


# Value Object

class OrderLine(BaseModel, frozen=True):
    order_ref: int
    CKU: str
    quantity: int

    def __hash__(self) -> int:
        return hash((self.order_ref, self.CKU, self.quantity))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderLine):
            return False
        return all([
            self.order_ref == other.order_ref,
            self.CKU == other.CKU,
            self.quantity == other.quantity
        ])
```


* ```__gt__``` for using in sorted() without key

