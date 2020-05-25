import arcpy
from arcpy import env
env.workspace = r"E:\programin\semestr2\20_05lec9\Lesson4"
inDem = "foxlake"
featureClass = "Temp.shp"
# Enter for loop for each feature
with arcpy.da.SearchCursor(featureClass, ["SHAPE@XY",]) as cursor:
    for row in cursor:
        x, y = row[0]
        result = arcpy.GetCellValue_management(inDem,str(x) + " " + str(y))
        print "Pixel value: " + result.getOutput(0)
print "All done!"

