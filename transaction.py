from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    description: str
    price: int
    sender: str
    receiver: str
    sender_id: int
    receiver_id: int
    quantity: int
    amount: int
    created: str = ""
    status: str = "new"
    id: Optional[int] = None
