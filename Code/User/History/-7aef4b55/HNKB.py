from setuptools import setup  
setup(     
	name="nombre_de_la_app",
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