def make_card_id_safe(unsafe_id: str) -> str:
    return unsafe_id.replace(" ", "")


def make_general_id_safe(some_id: str) -> str:
    return some_id.replace(" ", "")


def is_card_id_valid(card_id: str) -> bool:
    return make_card_id_safe(card_id).isalnum()


def is_general_id_valid(some_id: str) -> bool:
    return some_id.replace(" ", "").isalnum()


def insert_spaces_every_n_chars(starting_string: str, chars_before_separation: int=2, num_of_spaces: int=2) -> str:
    returned_str = ""
    for index, char in enumerate(starting_string):
        if index != 0:
            if index % chars_before_separation == 0:
                returned_str += " " * num_of_spaces
        returned_str += char
    return returned_str
