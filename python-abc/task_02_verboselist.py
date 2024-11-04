class VerboseList(list):
    """
    """

    def append(self, item):
        """
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
