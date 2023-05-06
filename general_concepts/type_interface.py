from typing import List, Tuple, Optional


def add(a: int, b: int) -> int:
    # Add two integers and return the result.
    return a + b


def find_even_numbers(numbers: List[int]) -> List[int]:
    # Return a list of even numbers from the input list of integers.
    return [number for number in numbers if number % 2 == 0]


def multiply(a: float, b: float) -> float:
    # Multiply two floating-point numbers and return the result.
    return a * b


def get_full_name(first_name: str, last_name: Optional[str] = None) -> str:
    # Return a person's full name, with an optional last name.
    if last_name:
        return f"{first_name} {last_name}"
    else:
        return first_name


def find_longest_word(words: List[str]) -> Tuple[str, int]:
    # Find the longest word in the input list and return the word and its length.
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)


if __name__ == "__main__":
    print(add(5, 3))
    print(find_even_numbers([1, 2, 3, 4, 5, 6]))
    print(multiply(3.5, 4.2))
    print(get_full_name("John", "Doe"))
    print(find_longest_word(["apple", "banana", "cherry"]))
