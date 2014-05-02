#import the ArcPy package.
import arcpy
import os

#Set the current workspace.
import arcpy
arcpy.env.workspace = "C:\\Users\\valenzak\\Documents\\GitHub\\Lab2"


##Create a new "Double" field
#Import arcpy and set the current workspace
import arcpy
arcpy.env.workspace = "C:\\Users\\valenzak\\Documents\\GitHub\\class-space\\urban-rural\\Table6"

#Specify the existing table
in_table = "saep_bg10"
#Name the new field
field_name = "POP_DEN13"

#Execute adding the "Double" field to the table
arcpy.AddField_management(in_table, field_name, "DOUBLE")