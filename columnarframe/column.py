import pyarrow as pa


class Column:

    def __init__(self, value, rows=None):
        if isinstance(value, Column):
            self.value = pa.array(value.to_list())
        elif isinstance(value, pa.Array):
            self.value = pa.array(value.to_pylist())
        elif isinstance(value, list):
            self.value = pa.array(value)
        elif rows is not None:
            self.value = pa.array([value] * rows)
        else:
            raise RuntimeError('unknown data.')

    def __repr__(self):
        return self.value.__repr__()

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.to_pylist().__iter__()

    def to_list(self):
        return self.value.to_pylist()

    def unique(self):
        return Column(self.value.unique())

    def apply(self, func):
        return Column([func(d.as_py()) for d in self.value])
