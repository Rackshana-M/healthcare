import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Load the updated DICOM file
ds = pydicom.dcmread("updated_output.dcm")

# Normalize & Display the image
img = ds.pixel_array.astype(np.float32)
img = (img - np.min(img)) / (np.max(img) - np.min(img))  # Scale to [0,1]
img = (img * 255).astype(np.uint8)  # Convert to 8-bit

plt.imshow(img, cmap="gray")
plt.title("Updated DICOM Image")
plt.colorbar()
plt.show()
