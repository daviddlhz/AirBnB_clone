import json

archivo = {}

archivo['clients'] = []

archivo['clients'].append({
	'Nombres':'Jesus',
	'Apellidos':'Gonzalez',
	'Edad':36,
	})


archivo['clients'].append({
	'Nombres':'Martha',
	'Apellidos':'Guardo',
	'Edad':87,
	})


archivo['clients'].append({
	'Nombres':'Dilia',
	'Apellidos':'Guardo',
	'Edad':32,
	})

with open('arch.json', 'w') as file:
		json.dump(archivo, file, indent=4)