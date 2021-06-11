{
	"General": {
		"Name": {
			"name": "Name",
			"label": "Name",
			"page": "General",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "TEC"
		},
		"Individualorcompany": {
			"name": "Individualorcompany",
			"label": "Individual or Company",
			"page": "General",
			"style": "Toggle",
			"default": false,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": true
		},
		"Defaultdescription": {
			"name": "Defaultdescription",
			"label": "Default Description",
			"page": "General",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"val": "What I'm focusing on."
		},
		"Defaulthourlyrate": {
			"name": "Defaulthourlyrate",
			"label": "Default Hourly Rate",
			"page": "General",
			"style": "Float",
			"size": 1,
			"default": 50.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 10.0,
			"normMax": 500.0,
			"clampMin": false,
			"clampMax": false,
			"val": 50.0
		},
		"Sync": {
			"name": "Sync",
			"label": "Sync",
			"page": "General",
			"style": "Header",
			"default": "",
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"val": ""
		},
		"Loadsettingsfile": {
			"name": "Loadsettingsfile",
			"label": "Load Settings File",
			"page": "General",
			"style": "File",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": ""
		},
		"Booksfile": {
			"name": "Booksfile",
			"label": "Books File",
			"page": "General",
			"style": "File",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "lib/books.py"
		},
		"Timesheetsfile": {
			"name": "Timesheetsfile",
			"label": "Timesheets File",
			"page": "General",
			"style": "File",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "lib/timesheets.py"
		},
		"Utilities": {
			"name": "Utilities",
			"label": "Utilities",
			"page": "General",
			"style": "Header",
			"default": "",
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"val": ""
		},
		"Cleanlibrary": {
			"name": "Cleanlibrary",
			"label": "Clean Library",
			"page": "General",
			"style": "Pulse",
			"default": false,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": 0
		},
		"Resetlibrary": {
			"name": "Resetlibrary",
			"label": "Reset Library",
			"page": "General",
			"style": "Pulse",
			"default": false,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": 0
		}
	},
	"Calendar": {
		"Selectedyear": {
			"name": "Selectedyear",
			"label": "Selected Year",
			"page": "Calendar",
			"style": "Int",
			"size": 1,
			"default": 2021,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 2000.0,
			"normMax": 2100.0,
			"clampMin": false,
			"clampMax": false,
			"val": 2021
		},
		"Selectedmonth": {
			"name": "Selectedmonth",
			"label": "Selected Month",
			"page": "Calendar",
			"style": "Int",
			"size": 1,
			"default": 1,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 1.0,
			"normMax": 12.0,
			"clampMin": false,
			"clampMax": false,
			"val": 6
		},
		"Selectedday": {
			"name": "Selectedday",
			"label": "Selected Day",
			"page": "Calendar",
			"style": "Int",
			"size": 1,
			"default": 0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 1.0,
			"normMax": 31.0,
			"clampMin": false,
			"clampMax": false,
			"val": 11
		},
		"Selectedweek": {
			"name": "Selectedweek",
			"label": "Selected Week",
			"page": "Calendar",
			"style": "Int",
			"size": 1,
			"default": 0,
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 1.0,
			"normMax": 6.0,
			"clampMin": false,
			"clampMax": false,
			"val": 2
		},
		"Numweeksinmonth": {
			"name": "Numweeksinmonth",
			"label": "Num Weeks in Month",
			"page": "Calendar",
			"style": "Int",
			"size": 1,
			"default": 0,
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 5
		},
		"Selecteddayindex": {
			"name": "Selecteddayindex",
			"label": "Selected Day Index",
			"page": "Calendar",
			"style": "Int",
			"size": 1,
			"default": 0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 6.0,
			"clampMin": false,
			"clampMax": false,
			"val": 4
		},
		"Week1": {
			"name": "Week1",
			"label": "Week 1",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": true,
			"readOnly": true,
			"enableExpr": null,
			"val": "''31'  '01'  '02'  '03'  '04'  '05'  '06''"
		},
		"Week2": {
			"name": "Week2",
			"label": "Week 2",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "''07'  '08'  '09'  '10'  '11'  '12'  '13''"
		},
		"Week3": {
			"name": "Week3",
			"label": "Week 3",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "''14'  '15'  '16'  '17'  '18'  '19'  '20''"
		},
		"Week4": {
			"name": "Week4",
			"label": "Week 4",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "''21'  '22'  '23'  '24'  '25'  '26'  '27''"
		},
		"Week5": {
			"name": "Week5",
			"label": "Week 5",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "''28'  '29'  '30'  '01'  '02'  '03'  '04''"
		},
		"Week6": {
			"name": "Week6",
			"label": "Week 6",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": ""
		},
		"Loading": {
			"name": "Loading",
			"label": "Loading",
			"page": "Calendar",
			"style": "Toggle",
			"default": false,
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": false
		}
	},
	"Time": {
		"Pomodorolength": {
			"name": "Pomodorolength",
			"label": "Pomodoro Length",
			"page": "Time",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "00:25:00.00"
		},
		"Shortrestlength": {
			"name": "Shortrestlength",
			"label": "Short Rest Length",
			"page": "Time",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "00:05:00.00"
		},
		"Pomodorosperset": {
			"name": "Pomodorosperset",
			"label": "Pomodoros Per Set",
			"page": "Time",
			"style": "Int",
			"size": 1,
			"default": 0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 4
		},
		"Longrestlength": {
			"name": "Longrestlength",
			"label": "Long Rest Length",
			"page": "Time",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "00:15:00.00"
		},
		"Totalhours": {
			"name": "Totalhours",
			"label": "Total Hours",
			"page": "Time",
			"style": "Float",
			"size": 1,
			"default": 0.0,
			"enable": true,
			"startSection": true,
			"readOnly": true,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 2.0
		},
		"Totalearnings": {
			"name": "Totalearnings",
			"label": "Total Earnings",
			"page": "Time",
			"style": "Float",
			"size": 1,
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 100.0
		}
	},
	"Appearance": {
		"Theme": {
			"name": "Theme",
			"label": "Theme",
			"page": "Appearance",
			"style": "Menu",
			"default": "Dark",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"menuNames": [
				"Dark",
				"Light"
			],
			"menuLabels": [
				"Dark",
				"Light"
			],
			"val": "Dark"
		},
		"Menubarbgcolor": {
			"name": "Menubarbgcolor",
			"label": "Menubar BG Color",
			"page": "Appearance",
			"style": "RGB",
			"default": 0.0,
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 0.08699999749660492
		},
		"Panelbgcolor": {
			"name": "Panelbgcolor",
			"label": "Panel BG Color",
			"page": "Appearance",
			"style": "RGB",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 0.20000000298023224
		},
		"Smalltabcolor": {
			"name": "Smalltabcolor",
			"label": "Small Tab Color",
			"page": "Appearance",
			"style": "RGBA",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": [
				0.2540000081062317,
				0.2540000081062317,
				0.2540000081062317,
				1.0
			]
		},
		"Tablebgcolor": {
			"name": "Tablebgcolor",
			"label": "Table BG Color",
			"page": "Appearance",
			"style": "RGB",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 0.3109999895095825
		},
		"Listbgcolor": {
			"name": "Listbgcolor",
			"label": "List BG Color",
			"page": "Appearance",
			"style": "RGB",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 0.25
		},
		"Selectedtextcolor": {
			"name": "Selectedtextcolor",
			"label": "Selected Text Color",
			"page": "Appearance",
			"style": "RGBA",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": 1.0
		},
		"Unselectedtextcolor": {
			"name": "Unselectedtextcolor",
			"label": "Unselected Text Color",
			"page": "Appearance",
			"style": "RGBA",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": [
				0.5,
				0.5,
				0.5,
				1.0
			]
		},
		"Selectioncolor": {
			"name": "Selectioncolor",
			"label": "Selection Color",
			"page": "Appearance",
			"style": "RGBA",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": [
				0.714,
				0.714,
				0.714,
				1.0
			]
		},
		"Restcolor": {
			"name": "Restcolor",
			"label": "Rest Color",
			"page": "Appearance",
			"style": "RGB",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": [
				0.0,
				0.8,
				1.0
			]
		},
		"Accentcolor": {
			"name": "Accentcolor",
			"label": "Accent Color",
			"page": "Appearance",
			"style": "RGB",
			"default": 0.0,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": [
				0.8,
				0.106667,
				0.0
			]
		},
		"Winoffset": {
			"name": "Winoffset",
			"label": "Window Offset",
			"page": "Appearance",
			"style": "XY",
			"default": 0.0,
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"min": 0.0,
			"max": 1.0,
			"normMin": 0.0,
			"normMax": 1.0,
			"clampMin": false,
			"clampMax": false,
			"val": [
				3381.0,
				235.0
			]
		},
		"Showpanel": {
			"name": "Showpanel",
			"label": "Show Panel",
			"page": "Appearance",
			"style": "Toggle",
			"default": false,
			"enable": true,
			"startSection": true,
			"readOnly": false,
			"enableExpr": null,
			"val": true
		},
		"Currentpanel": {
			"name": "Currentpanel",
			"label": "Current Panel",
			"page": "Appearance",
			"style": "Menu",
			"default": "Manage",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"menuSource": "op.UI.op('panel/folderTabs').par.Value0",
			"val": "Time"
		}
	},
	"About": {
		"Version": {
			"name": "Version",
			"label": "Version",
			"page": "About",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "0.1"
		},
		"Author": {
			"name": "Author",
			"label": "Author",
			"page": "About",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "Dylan Roscover"
		},
		"Contact": {
			"name": "Contact",
			"label": "Contact",
			"page": "About",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "rosco@tec.design"
		},
		"Website": {
			"name": "Website",
			"label": "Website",
			"page": "About",
			"style": "Pulse",
			"default": false,
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": 0
		}
	}
}