#import the ArcPy package.
import arcpy
import os

arcpy.env.workspace = "C://Data"


###Make three lists which hold classification table parameters

Llist = []
Ulist = []
Vlist = []

cursor = arcpy.da.SearchCursor(arcpy.GetParameterAsText(0), [arcpy.GetParameterAsText(1), arcpy.GetParameterAsText(2), arcpy.GetParameterAsText(3)])
for row in cursor:
    Llist.append(row[0])
    Ulist.append(row[1])
    Vlist.append(row[2])
del cursor



###Make a blank field
##Define variables in AddField_management
#Specify the existing table
in_table = arcpy.GetParameterAsText(4)
#Name the new field
field_name = arcpy.GetParameterAsText(7)

out_class = arcpy.GetParameterAsText(6)

arcpy.CopyFeatures_management(in_table, out_class)

##Execute adding the "Double" field with the defined variables to the table
arcpy.AddField_management(out_class, field_name, "DOUBLE")


###Populate the field
##Define Cursor 2
##Messages cannot adequately describe the things I did next.  These loops are the result of countless trial and error hours.
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
