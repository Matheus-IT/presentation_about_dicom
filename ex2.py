import pydicom
from icecream import ic


def main():
    ds = pydicom.dcmread("./images/example.dcm")
    ic(ds["SOPClassUID"])

    # >> ds["SOPClassUID"]: (0008, 0016) SOP Class UID
    #    UI: Digital Mammography X-Ray Image Storage - For Presentation

    ic(ds["SOPClassUID"].value)

    # >> ds["SOPClassUID"].value: '1.2.840.10008.5.1.4.1.1.1.2'


if __name__ == "__main__":
    main()
