{
	"General": {
		"Companyname": {
			"name": "Companyname",
			"label": "Company Name",
			"page": "General",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": "TEC"
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
			"val": 5
		},
		"Selectedweek": {
			"name": "Selectedweek",
			"label": "Selected Week",
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
			"normMax": 6.0,
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
			"val": 31
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
			"val": 0
		},
		"Week1": {
			"name": "Week1",
			"label": "Week 1",
			"page": "Calendar",
			"style": "Str",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": true,
			"enableExpr": null,
			"val": "''26'  '27'  '28'  '29'  '30'  '01'  '02''"
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
			"val": "''03'  '04'  '05'  '06'  '07'  '08'  '09''"
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
			"val": "''10'  '11'  '12'  '13'  '14'  '15'  '16''"
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
			"val": "''17'  '18'  '19'  '20'  '21'  '22'  '23''"
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
			"val": "''24'  '25'  '26'  '27'  '28'  '29'  '30''"
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
			"val": "''31'  '01'  '02'  '03'  '04'  '05'  '06''"
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
			"val": "00:00:07.00"
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
			"val": "00:00:05.00"
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
			"val": "00:00:10.00"
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
			"val": 0.135
		},
		"Tabcolor": {
			"name": "Tabcolor",
			"label": "Tab Color",
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
		"Tablecolor": {
			"name": "Tablecolor",
			"label": "Table Color",
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
		"Textcolor": {
			"name": "Textcolor",
			"label": "Text Color",
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
			"val": 0.0
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
				3362.0,
				525.0
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
		}
	}
}