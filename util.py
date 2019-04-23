# coding=utf-8

from io import BytesIO
import numpy as np
from PIL import Image


def bytes_to_image(bytes_object: BytesIO):
    """ convert BytesIO object to PIL Image """
    try:
        frame = np.frombuffer(bytes_object.getbuffer(), np.uint8).reshape([1080, 1920, 3])
        return Image.fromarray(np.uint8(frame))

    except (TypeError, AttributeError, ValueError):
        """
            ValueError -> No Frame
        """
        return None


def image_refine(img: Image):
    """
    :param img: PIL Image
    :return: bytes
        https://stackoverflow.com/questions/34697559/pil-image-to-qpixmap-conversion-issue
        修正 PIL Image 與 QImage 之間的轉換的 bug ?? 直接調用 ImageQt 會 crash 
    """
    if img.mode == "RGB":
        r, g, b = img.split()
        img = Image.merge("RGB", (b, g, r))
    elif img.mode == "RGBA":
        r, g, b, a = img.split()
        img = Image.merge("RGBA", (b, g, r, a))
    elif img.mode == "L":
        img = img.convert("RGBA")

    img2 = img.convert("RGBA")

    return img2.tobytes("raw", "RGBA")
