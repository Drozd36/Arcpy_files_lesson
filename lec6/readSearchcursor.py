import arcpy

inTable = r"E:\programin\semestr2\14.04\Lesson2\CityBoundaries.shp"
inField = "NAME"

rows = arcpy.SearchCursor(inTable)

# This loop goes through each row in the table
#  and gets a requested field value

for row in rows:
    currentCity = row.getValue(inField)
    print currentCity
