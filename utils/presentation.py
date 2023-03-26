from pydicom import FileDataset
from icecream import ic


draw_line = lambda: print("=" * 150)


def show_dicom_hierarchy_info(ds: FileDataset):
    ic(ds["PatientID"])
    ic(ds["StudyInstanceUID"])
    ic(ds["SeriesInstanceUID"])
    ic(ds["SeriesNumber"])
    ic(ds["SOPInstanceUID"])
    ic(ds["InstanceNumber"])
    draw_line()


def compare(ds1: FileDataset, ds2: FileDataset):
    print("Dataset1:")
    show_dicom_hierarchy_info(ds1)

    print("Dataset2:")
    show_dicom_hierarchy_info(ds2)


def show_pixel_info(ds: FileDataset):
    draw_line()
    ic(ds["PhotometricInterpretation"])
    ic(ds["SamplesPerPixel"])
    ic(ds["BitsAllocated"])
    ic(ds["BitsStored"])
    ic(ds["HighBit"])
    ic(ds["PixelRepresentation"])
    draw_line()
