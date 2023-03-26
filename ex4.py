import pydicom
from utils.presentation import show_pixel_info

ds = pydicom.dcmread("./images/example.dcm")

show_pixel_info(ds)

# ===========================================================================================
# ds["PhotometricInterpretation"]: (0028, 0004) Photometric Interpretation  CS: 'MONOCHROME2'
# ds["SamplesPerPixel"]:           (0028, 0002) Samples per Pixel           US: 1
# ds["BitsAllocated"]:             (0028, 0100) Bits Allocated              US: 16
# ds["BitsStored"]:                (0028, 0101) Bits Stored                 US: 12
# ds["HighBit"]:                   (0028, 0102) High Bit                    US: 11
# ds["PixelRepresentation"]:       (0028, 0103) Pixel Representation        US: 0
# ===========================================================================================
