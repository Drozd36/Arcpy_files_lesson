#This script clips all feature classes in a file geodatabase
import arcpy

# Create path variables
sourceWorkspace = r"E:\programin\semestr2\14.04\Lesson2PracticeExercise\USA.gdb"
targetWorkspace = r"E:\programin\semestr2\14.04\Lesson2PracticeExercise\Iowa.gdb"
clipFeature = r"E:\programin\semestr2\14.04\Lesson2PracticeExercise\Iowa.gdb\Iowa"

# Get a list of all feature classes in the USA folder
arcpy.env.workspace = sourceWorkspace
featureClassList = arcpy.ListFeatureClasses()

try:
    # Loop through all USA feature classes
    for featureClass in featureClassList:
        # Construct the output path
        outClipFeatureClass = targetWorkspace + "\\Iowa" + featureClass
        # Perform the clip and report what happened
        arcpy.Clip_analysis(featureClass, clipFeature, outClipFeatureClass)
        arcpy.AddMessage("Wrote clipped file " + outClipFeatureClass + ". ")
        print "Wrote clipped file " + outClipFeatureClass + ". "
except:
    # Report if there was an error
    arcpy.AddError("Could not clip feature classes")
    print "Could not clip feature classes"
    print arcpy.GetMessages()
