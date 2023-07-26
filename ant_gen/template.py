template_sub_and_gnd = '''   
# ----------------------------------------------
# Author : {author}
# Email : {email}
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("{project}")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{ground_plane_X_pos}{unit}",
		"YStart:="		, "{ground_plane_Y_pos}{unit}",
		"ZStart:="		, "{ground_plane_Z_pos}{unit}",
		"Width:="		, "{ground_plane_X_size}{unit}",
		"Height:="		, "{ground_plane_Y_size}{unit}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ground",
		"Flags:="		, "",
		"Color:="		, "(128 64 64)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "{ground_plane_X_pos}{unit}",
		"YPosition:="		, "{ground_plane_Y_pos}{unit}",
		"ZPosition:="		, "{ground_plane_Z_pos}{unit}",
		"XSize:="		, "{ground_plane_X_size}{unit}",
		"YSize:="		, "{ground_plane_Y_size}{unit}",
		"ZSize:="		, "{ground_plane_Z_size}{unit}"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ground_plane",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"{material}\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
'''

template_patch = '''
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{patch_plane_X_pos}{unit}",
		"YStart:="		, "{patch_plane_Y_pos}{unit}",
		"ZStart:="		, "{patch_plane_Z_pos}{unit}",
		"Width:="		, "{patch_plane_X_size}{unit}",
		"Height:="		, "{patch_plane_Y_size}{unit}",
		"WhichAxis:=" ,"Z"
    ],
	[
		"NAME:Attributes",
		"Name:="		, "{patch_name}",
		"Flags:="		, "",
		"Color:="		, "(128 64 64)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
'''

template_feed = '''
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{feed_X_pos}{unit}",
		"YStart:="		, "{feed_Y_pos}{unit}",
		"ZStart:="		, "{feed_Z_pos}{unit}",
		"Width:="		, "{feed_width}{unit}",
		"Height:="		, "{feed_size}{unit}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "feed",
		"Flags:="		, "",
		"Color:="		, "(128 64 64)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
    
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{feed_box_X_pos}{unit}",
		"YStart:="		, "{feed_box_Y_pos}{unit}",
		"ZStart:="		, "{feed_box_Z_pos}{unit}",
		"Width:="		, "{feed_box_width}{unit}",
		"Height:="		, "{feed_box_height}{unit}",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "feed_box",
		"Flags:="		, "",
		"Color:="		, "(128 64 64)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
    
'''

template_unite = '''
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "{unite1_name},{unite2_name}"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
'''

template_rectangle = '''
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "{rect_X_pos}{unit}",
		"YStart:="		, "{rect_Y_pos}{unit}",
		"ZStart:="		, "{rect_Z_pos}{unit}",
		"Width:="		, "{rect_width}{unit}",
		"Height:="		, "{rect_size}{unit}",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "{name}",
		"Flags:="		, "",
		"Color:="		, "(128 64 64)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\\"vacuum\\"",
		"SurfaceMaterialValue:=", "\\"\\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])    
'''

template_subtract ='''
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "{to_be_subtracted}",
		"Tool Parts:="		, "{rect1},{rect2}"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
'''
template_subtract_single_rect ='''
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "{to_be_subtracted}",
		"Tool Parts:="		, "{rect1}"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
'''
template_bound ='''
oModule = oDesign.GetModule("BoundarySetup")
'''