from config.file_config import INT32_MAX
from validation.exceptions import PositiveIntegerValidationFailed


def validate_positive_integer(val: int):
    if val > -1 and val <= INT32_MAX:
        return
    raise PositiveIntegerValidationFailed
