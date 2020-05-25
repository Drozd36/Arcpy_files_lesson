import arcpy

try:
    arcpy.env.workspace = r"E:\programin\semestr2\14.04\Lesson2\practiceData"

    template = "Precip2008Readings.shp"

    for year in range(2009, 2013):
        newfile = "Precip" + str(year) + "Readings.shp"
        arcpy.CreateFeatureclass_management(arcpy.env.workspace, newfile, "POINT", template,
                                            "DISABLED", "DISABLED", template)
    print('All done')
except:
    print arcpy.GetMessages()
