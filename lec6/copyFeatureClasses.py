import arcpy

try:
    arcpy.env.workspace = r"E:\programin\semestr2\25.03-14.04lec5\Lesson1"

    # List the feature classes in the Lesson 1 folder
    fcList = arcpy.ListFeatureClasses()

    # Loop through the list and copy the feature classes to the Lesson 2 PracticeData folder
    for featureClass in fcList:
        arcpy.CopyFeatures_management(featureClass, r"E:\\programin\\semestr2\\14.04\\practiceData\\" + featureClass)
    print "All done"
except:
    print "Script failed to complete"
    print arcpy.GetMessages(2)
