from setuptools import setup  
setup(     
	name="ConsoleTask",
	version="1.0",
	packages=["mi_paquete"],
	install_requires=[         
		"dependencia1",
		"dependencia2",
	],
	entry_points={         
		"console_scripts": [         
			"nombre_del_script=mi_paquete.script:main",      
		],
	}, 
)