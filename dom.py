import pydicom
import numpy as np
import imageio.v2 as imageio  # Use v2 to avoid deprecation warnings
from pydicom.dataset import FileDataset
import pydicom.uid

# Load an image (example: "medical_image.png")
image_path = "D:\hack\download.png"
img_array = imageio.imread(image_path, mode='L')  # Use mode='L' for grayscale

# Create a DICOM dataset
ds = FileDataset("output.dcm", {}, file_meta=pydicom.dataset.FileMetaDataset(), preamble=b"\0" * 128)

# Set metadata
ds.PatientName = "John Doe"
ds.PatientID = "123456"
ds.Modality = "CT"
ds.StudyInstanceUID = "1.2.3.4.5"
ds.SeriesInstanceUID = "1.2.3.4.5.6"
ds.SOPInstanceUID = "1.2.3.4.5.6.7"
ds.PhotometricInterpretation = "MONOCHROME2"

# **Fix: Add required DICOM metadata**
ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
ds.Rows, ds.Columns = img_array.shape
ds.PixelData = img_array.tobytes()
ds.BitsAllocated = 8
ds.BitsStored = 8
ds.HighBit = 7
ds.SamplesPerPixel = 1
ds.PixelRepresentation = 0  # 0 for unsigned integers (common for medical images)

# Save the DICOM file
ds.save_as("output.dcm")
print("✅ DICOM file created successfully: output.dcm")
