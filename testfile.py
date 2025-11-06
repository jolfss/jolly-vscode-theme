"""
This is a multi-line docstring for a module.
It serves as a general description of the module's purpose.
"""
import asyncio
from functools import wraps
from dataclasses import dataclass
from typing import Optional, Literal, cast

# Look, comments!
# NOTE: Define a constant
SOME_CONSTANT = 5

type BigT = type

@wraps
def greet(name: str) -> str:
    """
    This is a docstring about a method that greets people by name.
    It returns a kind greeting.
    """
    if name is None or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string.")
    message = f"Hello, {name}!"
    print(message)  # A print statement
    return message

@dataclass
class DummyClass: ...

class MyClass[GenericT : Optional[BigT]](int, DummyClass):
    """A sample class to test class-related theme elements."""

    class_variable : Literal["I am a class variable"] = "I am a class variable"
    generic_var : GenericT

    @property
    def read_only_property(self) -> int:
        """A read-only property."""
        return self.instance_variable * 2
    
    @classmethod
    def some_classmethod(cls, arg1: str, arg2: list) -> None: ...

    def __init__(self, value: int):
        local_variable = 0
        self.generic_var = cast(GenericT, value)
        self.instance_variable : int = value  # An instance variable
        self._private_variable : str = "private" # A "private" variable
        self.__dunder__ : str = "mangled" # A name-mangled variable
        local_variable -= 1


    def sample_method(self, arg1: str, arg2: list) -> None:
        """A sample method with various syntax elements."""
        local_variable = 10  # A local variable
        for item in arg2:
            if item == arg1:
                print(f"Found {item} matching {arg1}")
                break
            else:
                print(f"Item {item} does not match {arg1}")

        # A dictionary and list
        data = {
            "key1": "value1",
            "key2": 123,
            "key3": [1, 2, 3]
        }
        my_list = ["apple", "banana", "cherry"]

        # Exception handling
        try:
            result = local_variable / 0
            print(result)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        finally:
            print("Execution finished.")

        # Lambda function
        square = lambda x: x * x
        print(f"Square of 5: {square(5)}")
        print(data, my_list, square)

# Function calls and variable assignments
user_name = "Alice"
greeting_message = greet(user_name) # type: ignore

# Class instantiation and method calls
my_object = MyClass(42)
print(my_object.read_only_property)
my_object.sample_method("banana", ["apple", "orange", "banana"])

# Comments
# This is a single-line comment.
# TODO: Add more complex data structures.
# FIXME: This logic needs refactoring.

# Type hints and annotations
def process_data(data: dict[str, list[int]]) -> None:
    pass

# Async/await
async def fetch_data(url: str):
    # Simulate an asynchronous operation
    await asyncio.sleep(1)
    return {"data": "some_data"}

if __name__ == "__main__":
    print("Running main execution block.")
    asyncio.run(fetch_data("http://example.com"))