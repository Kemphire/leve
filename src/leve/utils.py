from typing import List
from .main import edit_distance


def closest_str(input_str: str, list_of_choices: List[str]) -> str:
    """
    Outputs the element from from the list_of_choices which is closest to the input_str
    **This function doesn't the case when list_of_choices is empty**
    """
    all_dist = list(map(lambda x: edit_distance(input_str, x), list_of_choices))
    index_of_least_dist = all_dist.index(min(all_dist))
    return list_of_choices[index_of_least_dist]


def normalized_dist(str1: str, str2: str) -> float:
    """
    Returs the normalized lavenshtein distance
    i.e. 1 when the string are not identical at all
         0 when the strings are completely identical
    """
    return edit_distance(str1, str2) / max(len(str1), len(str2))


if __name__ == "__main__":
    print(normalized_dist("add", "daddy"))
