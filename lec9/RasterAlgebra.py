import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
env.workspace = r"E:\programin\semestr2\20_05lec9\Lesson4"
# Get parameters of min and max elevations
inMin = 3000
inMax = 3300
# Perform the map algebra and make a temporary raster
inDem = Raster("foxlake")
tempRaster = (inDem > int(inMin)) & (inDem < int(inMax))
# Set up remap table and call Reclassify, leaving all values not 1 as NODATA
remap = RemapValue([[1,1]])
remappedRaster = Reclassify(tempRaster, "Value", remap, "NODATA")
# Save the reclassified raster to disk
remappedRaster.save("foxlake_recl_1.tif")
arcpy.CheckInExtension("Spatial")
print "All done!"
