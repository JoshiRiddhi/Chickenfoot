
# Implement suggested methods if needed.  Add or remove helper methods or attributes you need; 
# just make sure you keep the constructor parameters the same for the tests.
class Domino:
    def __init__(self, value_1: int, value_2: int) -> None:
        self.value = (value_1, value_2)
    
    # Returns true if value is one of the sides of the domino
    def contains_val(self, value):
        if self.value[0] == value or self.value[1] == value:
            return True
        return False

    # returns true is the domino is a double
    def is_double(self):
        if self.value[0] == self.value[1]:
            return True
        return False
    
    # sets which pip values are open to be played on and closed if played on a tile
    # set attributes self.open_value and self.closed_value to the appropriate values to get
    # __str__ to work
    def set_open_value(self, matched_value:int):
        if self.value[0] == matched_value:
            self.open_value = self.value[1]
            self.closed_value = self.value[0]
        else:
            self.open_value = self.value[0]
            self.closed_value = self.value[1]

    # returns a string representing the domino; used for casting as string and string formats
    def __str__(self) -> str:
        return f"{self.open_value}-{self.closed_value}" if hasattr(self, "open_value") \
            else f"{self.value[0]}-{self.value[1]}"

    # DO NOT CHANGE __eq__ or __hash__ BELOW.  These allow you to use == on dominos
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Domino):
            return obj.value == self.value
        return False

    def __hash__(self) -> int:
        return hash(self.value)