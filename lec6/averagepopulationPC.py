# Finds the average population in a counties dataset
import arcpy

featureClass = r"E:\programin\semestr2\14.04\counties.shp"

rows = arcpy.SearchCursor(featureClass)
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

# Loop through each row and keep running total of population
# and records counted.
while row:
    totalPopulation += row.POP1990 ###totalPopulation += row.getValue(populationField)
    recordsCounted += 1
    row = rows.next()
average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)
