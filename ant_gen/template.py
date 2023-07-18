template_msp = '''   
# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2022.2.0
# {time}  {month} {day}, {year}
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("{project}")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
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

# oProject.Save()
'''

