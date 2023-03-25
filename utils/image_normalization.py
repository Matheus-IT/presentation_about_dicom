import numpy as np
import cv2 as cv

__last_normalize_min_val = None
__last_normalize_max_val = None


def normalize(arr: np.ndarray, min_val: int = 0, max_val: int = 255):
    global __last_normalize_min_val, __last_normalize_max_val

    __last_normalize_min_val = min_val
    __last_normalize_max_val = max_val
    return cv.normalize(arr, None, min_val, max_val, cv.NORM_MINMAX)  # type: ignore


def denormalize(arr: np.ndarray, min_val: int, max_val: int):
    """Need min_val and max_val that was used before normalizing"""
    global __last_normalize_min_val, __last_normalize_max_val

    last_min_val = __last_normalize_min_val
    last_max_val = __last_normalize_max_val

    img = np.multiply(arr, (max_val - min_val) / last_max_val) + min_val  # type: ignore

    return img.astype(np.uint16)  # convert to original data type
