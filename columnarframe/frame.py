from .column import Column


class ColumnarFrame:
    def __init__(self, data=None):
        self.rows = -1
        self.data = {}
        if data is not None:
            for k, v in data.items():
                if self.rows == -1:
                    self.rows = len(v)
                else:
                    self._check_length(v)
                self.data[k] = Column(v)

    def _check_length(self, v):
        if self.rows != len(v):
            raise RuntimeError('different row count.')

    @property
    def columns(self):
        return list(self.data.keys())

    def __getitem__(self, name):
        if isinstance(name, list):
            return ColumnarFrame({k: Column(self.data[k]) for k in name})
        return self.data[name]

    def __setitem__(self, name, value):
        self._check_length(value)
        self.data[name] = Column(value)

    def __repr__(self):
        return self.data.__repr__()

    def __len__(self):
        return self.rows

    def rename(self, columns):
        # TODO
        pass

    def to_csv(self, name, **kwargs):
        # TODO
        pass
