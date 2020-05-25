import arcpy

inFolder = r"E:\programin\semestr2\14.04\Lesson2\\"
resultsFolder = r"E:\programin\semestr2\14.04\Lesson2\\Result\\"
clipFeature = r"E:\programin\semestr2\25.03-14.04lec5\Lesson1\Nebraska.shp"

# List feature classes
arcpy.env.workspace = inFolder
featureClassList = arcpy.ListFeatureClasses()

# Loop through each feature class and clip
for featureClass in featureClassList:
    # Make the output path by concatenating strings
    outputPath = resultsFolder + featureClass
    # Clip the feature class
    arcpy.Clip_analysis(featureClass, clipFeature, outputPath)
    print("Feature " + featureClass)
print('All done')