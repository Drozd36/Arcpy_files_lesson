import arcpy

featureClass = r"E:\programin\semestr2\14.04\pencilvania\New File Geodatabase.gdb\counties"
populationField = "POP1990"

with arcpy.da.SearchCursor(featureClass, (populationField,) , '"POP1990" > 100000') as cursor:
    for row in cursor:
        print str(row[0])
