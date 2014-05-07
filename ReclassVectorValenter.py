#import the ArcPy package.
import arcpy
import os

arcpy.env.workspace = "C://Data"


###Make three lists which hold classification table parameters

L = arcpy.GetParameterAsText(2)
Llist = L.split(";")

U = arcpy.GetParameterAsText(3)
Ulist = U.split(";")

V = arcpy.GetParamterAsText(4)
Vlist = V.split(";")

###Make a blank field
##Define variables in AddField_management
#Specify the existing table
in_table = arcpy.GetParameterAsText(5)
#Name the new field
field_name = arcpy.GetParameterAsText(1)

##Execute adding the "Double" field with the defined variables to the table
arcpy.AddField_management(in_table, field_name, "DOUBLE")


###Populate the field
##Define Cursor 2
##Messages cannot adequately describe the things I did next.  These loops are the result of countless trial and error hours.
cursor2 = arcpy.da.UpdateCursor([arcpy.GetParameterAsText(5)], [arcpy.GetParameterAsText(0), arcpy.GetParameterAsText(1)])
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