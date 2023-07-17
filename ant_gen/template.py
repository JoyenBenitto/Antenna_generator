template_msp= f''' 
# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2022.2.0
# 16:50:04  Jul 16, 2023
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project2")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-0.3mm",
		"YPosition:="		, "-0.3mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "1.3mm",
		"YSize:="		, "1mm",
		"ZSize:="		, "0.3mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Substrate"
				],
				[
					"NAME:Material",
					"Value:="		, "\\"FR4_epoxy\\""
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Substrate:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "45mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "48mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "1.6mm"
				],
				[
					"NAME:Position",
					"X:="			, "-24mm",
					"Y:="			, "-25mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-10mm",
		"YStart:="		, "-5mm",
		"ZStart:="		, "0mm",
		"Width:="		, "25mm",
		"Height:="		, "20mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Patch"
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 64
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Patch:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "38mm"
				],
				[
					"NAME:YSize",
					"Value:="		, "29mm"
				],
				[
					"NAME:Position",
					"X:="			, "-19mm",
					"Y:="			, "-15mm",
					"Z:="			, "1.6mm"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "24mm",
		"YStart:="		, "-25mm",
		"ZStart:="		, "0mm",
		"Width:="		, "-48mm",
		"Height:="		, "45mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Ground"
				],
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 64,
					"B:="			, 64
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-1.5mm",
		"YStart:="		, "-25mm",
		"ZStart:="		, "0mm",
		"Width:="		, "3mm",
		"Height:="		, "18mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Feed"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Feed:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-1.5mm",
					"Y:="			, "-25mm",
					"Z:="			, "1.6mm"
				],
				[
					"NAME:YSize",
					"Value:="		, "17.5mm"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2.5mm",
		"YStart:="		, "-15mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "7.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oDesign.Undo()
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2.5mm",
		"YStart:="		, "-15mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "7.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oDesign.Undo()
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-3mm",
		"YStart:="		, "-15mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1.5mm",
		"Height:="		, "7.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
		"XStart:="		, "1.5mm",
		"YStart:="		, "-15mm",
		"ZStart:="		, "0mm",
		"Width:="		, "2mm",
		"Height:="		, "7.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oDesign.Undo()
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "1.5mm",
		"YStart:="		, "-15mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1.5mm",
		"Height:="		, "7.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-1.5mm",
					"Y:="			, "-15mm",
					"Z:="			, "1.6mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "-1.5mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle2:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "1.5mm",
					"Y:="			, "-15mm",
					"Z:="			, "1.6mm"
				]
			]
		]
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Patch",
		"Tool Parts:="		, "Rectangle1,Rectangle2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Patch,Feed"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-1.5mm",
		"YStart:="		, "-25mm",
		"ZStart:="		, "1.6mm",
		"Width:="		, "-1.6mm",
		"Height:="		, "3mm",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle3",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle3"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Port"
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 0,
					"B:="			, 0
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPerfectE(
	[
		"NAME:Ground",
		"Objects:="		, ["Ground"],
		"InfGroundPlane:="	, False
	])
oModule.AssignPerfectE(
	[
		"NAME:Patch",
		"Objects:="		, ["Patch"],
		"InfGroundPlane:="	, False
	])
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		159
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Ground"
	], "1", True)
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Port:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-1.5mm",
					"Y:="			, "-25mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oDesign.Undo()
oModule = oDesign.GetModule("ModelSetup")
oModule.CreateOpenRegion(
	[
		"NAME:Settings",
		"OpFreq:="		, "2.4GHz",
		"Boundary:="		, "Radiation",
		"ApplyInfiniteGP:="	, False
	])
oModule = oDesign.GetModule("RadField")
oModule.InsertInfiniteSphereSetup(
	[
		"NAME:Infinite Sphere1",
		"UseCustomRadiationSurface:=", False,
		"CSDefinition:="	, "Theta-Phi",
		"Polarization:="	, "Linear",
		"ThetaStart:="		, "-180deg",
		"ThetaStop:="		, "180deg",
		"ThetaStep:="		, "10deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "90deg",
		"PhiStep:="		, "90deg",
		"UseLocalCS:="		, False
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "2.4GHz",
		"MaxDeltaS:="		, 0.02,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 6,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"DrivenSolverType:="	, "Direct Solver",
		"EnhancedLowFreqAccuracy:=", False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced",
		"InfiniteSphereSetup:="	, ""
	])
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearStep",
		"RangeStart:="		, "1.2GHz",
		"RangeEnd:="		, "3.6GHz",
		"RangeStep:="		, "0.01GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False
	])
oProject.SaveAs("C:\\Users\\rinit\\OneDrive\\Desktop\\capstone\\Design\\mspa_insetfeed.aedt", True)
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Terminal S Parameter Plot 1", "Terminal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(St(Patch_T1,Patch_T1))"]
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditFrequencySweep("Setup1", "Sweep", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearStep",
		"RangeStart:="		, "1.2GHz",
		"RangeEnd:="		, "3.6GHz",
		"RangeStep:="		, "0.001GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False
	])
oModule = oDesign.GetModule("ReportSetup")
oModule.AddMarker("Terminal S Parameter Plot 1", "m1", "dB(St(Patch_T1 Patch_T1)) : Setup1 : Sweep : Cartesian", "2.367GHz")
oModule.CreateReport("Gain Plot 1", "Far Fields", "Rectangular Plot", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "Infinite Sphere1"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["2.4GHz"]
	], 
	[
		"X Component:="		, "Theta",
		"Y Component:="		, ["dB(GainTotal)"]
	])
oModule.CreateReport("Directivity Plot 1", "Far Fields", "Rectangular Plot", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "Infinite Sphere1"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["2.4GHz"]
	], 
	[
		"X Component:="		, "Theta",
		"Y Component:="		, ["dB(DirTotal)"]
	])
oModule.CreateReport("Gain Plot 2", "Far Fields", "Rectangular Plot", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "Infinite Sphere1"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["2.4GHz"]
	], 
	[
		"X Component:="		, "Theta",
		"Y Component:="		, ["dB(GainTotal)"]
	])
oProject.Save()

'''  