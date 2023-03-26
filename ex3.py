import pydicom
from utils.presentation import compare

ds = pydicom.dcmread("./images/example.dcm")

ds_copy = ds.copy()

ds_copy.InstanceNumber += 1
ds_copy.SOPInstanceUID = pydicom.uid.generate_uid()

ds_copy.save_as("./images/example_image2.dcm")

compare(ds, ds_copy)

# Dataset1:
#   ds["PatientID"]:         (0010, 0020) Patient ID           LO: 'Case2'
#   ds["StudyInstanceUID"]:  (0020, 000d) Study Instance UID   UI: 1.3.6.1.4.1.5962[...]
#   ds["SeriesInstanceUID"]: (0020, 000e) Series Instance UID  UI: 1.3.6.1.4.1.5962[...]
#   ds["SeriesNumber"]:      (0020, 0011) Series Number        IS: '71300000'
#   ds["SOPInstanceUID"]:    (0008, 0018) SOP Instance UID     UI: 1.3.6.1.4.1.5962[...]
#   ds["InstanceNumber"]:    (0020, 0013) Instance Number      IS: '39'
# ======================================================================================
# Dataset2:
#   ds["PatientID"]:         (0010, 0020) Patient ID           LO: 'Case2'
#   ds["StudyInstanceUID"]:  (0020, 000d) Study Instance UID   UI: 1.3.6.1.4.1.5962[...]
#   ds["SeriesInstanceUID"]: (0020, 000e) Series Instance UID  UI: 1.3.6.1.4.1.5962[...]
#   ds["SeriesNumber"]:      (0020, 0011) Series Number        IS: '71300000'
#   ds["SOPInstanceUID"]:    (0008, 0018) SOP Instance UID     UI: 1.2.826.0.1.3680[...]
#   ds["InstanceNumber"]:    (0020, 0013) Instance Number      IS: '40'
# ======================================================================================
