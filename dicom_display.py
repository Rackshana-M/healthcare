import pydicom
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from mpl_toolkits.mplot3d import Axes3D

# File name of the DICOM file
dicom_file = "output.dcm"  # Change this to your actual filename

# Load the DICOM file
ds = pydicom.dcmread(dicom_file)

# Extract image data
img = ds.pixel_array.astype(np.float32)

# Normalize image (0 to 1)
img = (img - np.min(img)) / (np.max(img) - np.min(img))

# Apply Gaussian smoothing to reduce noise
img = gaussian_filter(img, sigma=2)

# Extract metadata
patient_name = ds.PatientName if 'PatientName' in ds else "Unknown"
patient_id = ds.PatientID if 'PatientID' in ds else "Unknown"
modality = ds.Modality if 'Modality' in ds else "Unknown"
study_date = ds.StudyDate if 'StudyDate' in ds else "Unknown"
manufacturer = ds.Manufacturer if 'Manufacturer' in ds else "Unknown"

# Display metadata
print("📄 DICOM Metadata:")
print(f"Patient Name: {patient_name}")
print(f"Patient ID: {patient_id}")
print(f"Modality: {modality}")
print(f"Study Date: {study_date}")
print(f"Manufacturer: {manufacturer}")

# Create 3D Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid
x = np.linspace(0, img.shape[1], img.shape[1])
y = np.linspace(0, img.shape[0], img.shape[0])
X, Y = np.meshgrid(x, y)

# Plot 3D surface
ax.plot_surface(X, Y, img, cmap="gray", edgecolor="none")

ax.set_title("3D DICOM Visualization")
plt.show()
