import arcpy

# Run the Copy Features tool, setting the output to the geometry object.
# geometries is returned as a list of geometry objects.

featureClass = r"E:\programin\semestr2\14_04_28_04lec6\Lesson2PracticeExercise\USA.gdb\Roads"
geometries = arcpy.CopyFeatures_management(featureClass, arcpy.Geometry())

# Walk through each geometry, totaling the length
length = 0
for geometry in geometries:
    length += geometry.length

print("Total length: {0}".format(length))
