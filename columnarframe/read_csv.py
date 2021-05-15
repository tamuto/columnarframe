import io
import pyexcel as pe

from .frame import ColumnarFrame
from .utils import skip_footer

def read_csv(
        filename,
        encoding='utf-8',
        delimiter=',',
        skiprows=0,
        skipfooter=0,
        header=True,
        quotechar='"',
        doublequote=True,
        escapechar=None,
        ):
    
    with open(filename, 'r') as f:
        stream = io.StringIO(f.read())

        data = pe.get_dict(
            file_stream=stream,
            file_type='csv',
            encoding=encoding,
            delimiter=delimiter,
            start_row=skiprows,
            quotechar=quotechar,
            doublequote=doublequote,
            escapechar=escapechar,
            auto_detect_float=False,
            auto_detect_int=False,
            auto_detect_datetime=False)
    
        # TODO: header

        data = skip_footer(skipfooter)

    return ColumnarFrame(data)
