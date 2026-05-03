from collections.abc import Mapping


class RangeKeyDict:
    def __init__(self, ranges):
        if isinstance(ranges, Mapping):
            ranges = ranges.items()

        self._ranges = []
        for key, value in ranges:
            self._validate_key(key)
            self._ranges.append((key[0], key[1], value))

    def __getitem__(self, number):
        matches = self.get_all(number)
        if matches:
            return matches[0]
        return None

    def get_all(self, number):
        return tuple(
            value
            for start, end, value in self._ranges
            if start <= number < end
        )

    @staticmethod
    def _validate_key(key):
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError('Range keys must be two-item tuples')
        if not all(isinstance(value, int) for value in key):
            raise TypeError('Range bounds must be integers')
        if key[0] >= key[1]:
            raise ValueError('Range lower bound must be lower than upper bound')
