from typing import TypeVar, Optional, Generic

T = TypeVar("T")
class Link(Generic[T]):
    """Store a single element in a link "chain"."""

    def __init__(self, element: Optional[T] = None):
        self.element: Optional[T] = element
        self.next: Optional[Link[T]] = None


class LinkChain:
    def __init__(self, head):
        self.head = head

    #     tmp = remove_all(1, tmp)
    def remove_all(self, value: T, head: Optional[Link[T]]) -> Optional[Link[T]]:
        if head is None:
            return None
        while head.element == value:
            head = head.next
        current: Link[T] = head
        while current is not None:
            if current.next.element == value:
                current.next = current.next.next