#Simple search and replace script
import arcpy

# Retrieve input parameters: the feature class, the field affected by
# the search and replace, the search term, and the replace term.
fc = arcpy.GetParameterAsText(0)
affectedField = arcpy.GetParameterAsText(1)
oldValue = arcpy.GetParameterAsText(2)
newValue = arcpy.GetParameterAsText(3)

#fc = r"E:\programin\semestr2\14.04\Lesson2PracticeExercise\USA.gdb"
#affectedField = "CAPITAL_RANGE"
#oldValue = 0
#newValue = 10

# Create the SQL expression for the update cursor. Here this is
# done on a separate line for readability.
#queryString = '"' + affectedField + '" = ' + "'" + oldValue + "'"

# Create the update cursor and update each row returned by the SQL expression
with arcpy.da.UpdateCursor(fc, (affectedField,), '"'+affectedField+'"=' + oldValue) as cursor:
    for row in cursor:
        row[0] = newValue
        cursor.updateRow(row)
arcpy.AddMessage("ALL DONE")