import arcpy

featureClass = r"C:/Users/Sheol/Desktop/2013-14/2015-2016/ProgramGIS/ArcPy/Lesson2/PracticeData/Pennsylvania.gdb/counties"
populationField = "POP1990"

average = 0
totalPopulation = 0
recordsCounted = 0

with arcpy.da.SearchCursor(featureClass, (populationField,)) as cursor:
    for row in cursor:
        totalPopulation += row[0]
        recordsCounted += 1

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)
