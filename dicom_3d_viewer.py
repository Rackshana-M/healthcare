
import vtk

# Set the path to the DICOM folder
dicom_path = r"D:/hack/"  # Change this to the actual folder
# Change this to your DICOM folder

# Read DICOM images
reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dicom_path)
reader.Update()

# Create a volume mapper
volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
volumeMapper.SetInputConnection(reader.GetOutputPort())

# Create volume property (defines appearance)
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.ShadeOn()
volumeProperty.SetInterpolationTypeToLinear()

# Create a color transfer function (adjust colors)
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(-1000, 0.0, 0.0, 0.0)  # Black
colorFunc.AddRGBPoint(0, 1.0, 0.5, 0.3)      # Brownish
colorFunc.AddRGBPoint(1000, 1.0, 1.0, 1.0)   # White

# Create an opacity transfer function
opacityFunc = vtk.vtkPiecewiseFunction()
opacityFunc.AddPoint(-1000, 0.0)
opacityFunc.AddPoint(0, 0.1)
opacityFunc.AddPoint(1000, 1.0)

# Set color and opacity to volume property
volumeProperty.SetColor(colorFunc)
volumeProperty.SetScalarOpacity(opacityFunc)

# Create the volume and set properties
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# Renderer
renderer = vtk.vtkRenderer()
renderer.AddVolume(volume)
renderer.SetBackground(0, 0, 0)  # Black background

# Render window
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

# Interactor
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Start rendering
renderWindow.Render()
renderWindowInteractor.Start()
