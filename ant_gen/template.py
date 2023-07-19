template_sub_and_gnd = '''   
# ----------------------------------------------
# Author : Joyen Benitto
# Email : joyen.benitto12@gmail.com
# {time}  {month} {day}, {year}
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
		"XStart:="		, "{ground_plane_X_pos}{unit}",
		"YStart:="		, "{ground_plane_Y_pos}{unit}",
		"ZStart:="		, "{ground_plane_Z_pos}{unit}",
		"Width:="		, "{ground_plane_X_size}{unit}",
		"Height:="		, "{ground_plane_Y_size}{unit}",
		"WhichAxis:="		, "Z"
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