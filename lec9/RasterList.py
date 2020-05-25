import arcpy
from arcpy import env
env.workspace = r"E:\programin\semestr2\20_05lec9\Lesson4"
rasterlist = arcpy.ListRasters( )
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    print desc
    print raster + " is <<<" + desc.dataType + ">>> raster type"
