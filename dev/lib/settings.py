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
				996.0,
				1.0
			]
		}
	},
	"Load": {
		"Loadsettingsfile": {
			"name": "Loadsettingsfile",
			"label": "Load Settings File",
			"page": "Load",
			"style": "File",
			"default": "",
			"enable": true,
			"startSection": false,
			"readOnly": false,
			"enableExpr": null,
			"val": ""
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