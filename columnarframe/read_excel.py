import io
import pyexcel as pe

from .frame import ColumnarFrame
from .utils import skip_footer


def read_excel(
    filename,
    file_type='xlsx',
    encoding='utf-8',
    header=0,
    skiprows=0,
    skipfooter=0,
):
    with open(filename, 'rb') as f:
        stream = io.BytesIO(f.read())

        if header is None:
            # TODO: header
            # header=None を指定した際に、0 から連番のカラムを振りたい。
            # pyexcel では必ず1行目（start_row を指定している場合はその行から）がヘッダとして扱われてしまう。
            # （つまりデータから始まるファイルの場合不都合）
            # get_dict を呼ぶ前にダミー行を追加する等の細工が必要
            pass

        data = pe.get_dict(
            file_stream=stream,
            file_type=file_type,
            encoding=encoding,
            start_row=skiprows)

        data = skip_footer(data, skipfooter)

        print(data)

    return ColumnarFrame(data)
