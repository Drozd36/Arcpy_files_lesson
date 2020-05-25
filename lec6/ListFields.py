
# Reads the fields in a feature class

import arcpy

featureClass = r"E:\programin\semestr2\14.04\Lesson2PracticeExercise\USA.gdb\Cities"
fieldList = arcpy.ListFields(featureClass)
print(fieldList)
# Loop through each field in the list and print the name
for field in fieldList:
    print field.name

