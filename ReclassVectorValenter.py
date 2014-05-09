#import the ArcPy package.
import arcpy
import os

###Make/define three lists which hold classification table parameters
##Lowbound list
Llist = []
##Highbound list
Ulist = []
##Values/Classifications list
Vlist = []

###Fill the lists using fields from the table
##Define the searchcursor
cursor = arcpy.da.SearchCursor(arcpy.GetParameterAsText(0), [arcpy.GetParameterAsText(1), arcpy.GetParameterAsText(2), arcpy.GetParameterAsText(3)])
for row in cursor:
    Llist.append(row[0]) #Add lowbounds to lowbound list
    Ulist.append(row[1]) #Add highbounds to highbound list
    Vlist.append(row[2]) #Add values/classifications to list
##End the cursor
del cursor

#Specify the existing table
in_table = arcpy.GetParameterAsText(4)
#Name the new field
field_name = arcpy.GetParameterAsText(7)
#New layer as an output
out_class = arcpy.GetParameterAsText(6)

##Create a new layer and populate it with the input layer
arcpy.CopyFeatures_management(in_table, out_class)

##Execute adding a new "Double" field with the defined variables to the output table
arcpy.AddField_management(out_class, field_name, "DOUBLE")

###Populate the new field in the new layer
##Define Cursor 2
cursor2 = arcpy.da.UpdateCursor(out_class, [arcpy.GetParameterAsText(5), arcpy.GetParameterAsText(7)])
for row2 in cursor2: 
        if row2[0] < Llist[0]:
            row2[1] = 9999
            cursor2.updateRow(row2)
        elif row2[0] >= Ulist[-1]:
            row2[1] = 9999
        else:
         for y in Llist: 
             if row2[0] >= y: 
                 z = Llist.index(y)
                 if row2[0] < Ulist[z]:
                     row2[1] = Vlist[z]
                     cursor2.updateRow(row2)
                 else:
                     row2[1] = 9999
                     cursor2.updateRow(row2)
del cursor2
