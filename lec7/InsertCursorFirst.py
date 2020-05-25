#add new field in feature class
import arcpy

fc = r"E:\programin\semestr2\14_04_28_04lec6\Lesson2PracticeExercise\USA.gdb\CitiesCopy1"
newField = ["NAME","CAPITAL"]

with arcpy.da.InsertCursor(fc, newField) as cursor:
        cursor.insertRow(["Kiev",3])
        del cursor
print "All done!"
