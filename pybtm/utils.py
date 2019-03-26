import qrcode
import pybase64
from io import BytesIO

# create_qrcode_base64 create qrcode, then encode it to base64
# type(s) is str
def create_qrcode_base64(s):
    img = qrcode.make(s)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    base64_str = pybase64.b64encode(buffered.getvalue()).decode("utf-8")
    return {
        "base64": base64_str
    }