import pydicom
from icecream import ic


def main():
    ds = pydicom.dcmread("./images/example.dcm")
    ic(ds.PatientName)
    ic(ds.PatientID)
    ic(ds.PatientSex)
    ic(ds.PatientBirthDate)
    # ic(ds.PatientWeight) NOT FOUND, IT'S OPTIONAL

    # >> ds.PatientName: 'Case2'
    #    ds.PatientID: 'Case2'
    #    ds.PatientSex: 'M'
    #    ds.PatientBirthDate: ''


if __name__ == "__main__":
    main()
