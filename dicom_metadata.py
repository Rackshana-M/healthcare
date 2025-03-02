import pydicom

# Load DICOM file
dicom_file = "output.dcm"  # Change if needed
ds = pydicom.dcmread(dicom_file)

# Extract metadata
patient_name = ds.get("PatientName", "Not Available")
patient_id = ds.get("PatientID", "Not Available")
modality = ds.get("Modality", "Not Available")
study_date = ds.get("StudyDate", "Not Available")
manufacturer = ds.get("Manufacturer", "Not Available")

# Print metadata
print("\n📄 DICOM Metadata:")
print("-" * 50)
print(f"Patient Name: {patient_name}")
print(f"Patient ID: {patient_id}")
print(f"Modality: {modality}")
print(f"Study Date: {study_date}")
print(f"Manufacturer: {manufacturer}")

# Display all metadata
print("\n📜 Full DICOM Metadata:")
print("-" * 50)
for elem in ds:
    print(f"{elem.tag} - {elem.keyword}: {elem.value}")

# Check & Fix Missing Metadata
if study_date == "Not Available" or manufacturer == "Not Available":
    print("\n⚠️ Missing metadata detected! Adding default values...")

    if study_date == "Not Available":
        ds.StudyDate = "20240301"  # Example: March 1, 2024

    if manufacturer == "Not Available":
        ds.Manufacturer = "Siemens"

    # Save the updated DICOM file
    updated_file = "updated_output.dcm"
    ds.save_as(updated_file)
    print(f"✅ Updated DICOM file saved as: {updated_file}")
else:
    print("\n✅ All metadata is available, no changes needed.")
