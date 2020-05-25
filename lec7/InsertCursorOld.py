#add new field in feature class
import arcpy

# Create insert cursor for table
fc = r"E:\programin\semestr2\14_04_28_04lec6\Lesson2PracticeExercise\USA.gdb\CitiesCopy1"
rows = arcpy.InsertCursor(fc)

# Create 25 new rows. Set the initial row ID and distance values
for x in xrange(1, 26):
    row = rows.newRow()
    row.setValue("UIDENT", x)
    row.setValue("POPCLASS", 1)
    rows.insertRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows

print "All done!"