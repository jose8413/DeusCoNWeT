# -*- coding: utf8 -*-
import sys, urllib
import test_utils

# Script para hacer pruebas a la API de Componentes de PicBit (api/componentes)
# Uso: python api_componentes_tester {subida|obtención|modificación|borrado}

def main():
	if len(sys.argv) == 2:
		option = sys.argv[1]
		test_utils.openConnection()
		basepath = "/api/componentes"
		option_list = ['subida', 'obtención', 'modificación', 'borrado']
		if option in option_list:
			# PRE-TEST 1: Hacer login en el sistema mediante googleplus
			request_uri = "/api/oauth/googleplus/login"
			print "\nPRETEST 1: Haciendo petición POST a " + request_uri + " (login)\n Ignorar el status de este caso"
			token_id_login = "idgoogle"
			access_token_login = "googleTEST"
			params = urllib.urlencode({'token_id': token_id_login, 'access_token':access_token_login})
			session1 = test_utils.make_request("POST", request_uri, params, 200, None, True)

			if option == "subida":
				request_uri = basepath
				params = urllib.urlencode({})

				# TEST 1
				print "TEST 1: : Obtener la lista de componentes. Debe retornar una lista vacia de componentes"
				print "Status esperado: 204 "
				test_utils.make_request("GET", request_uri, params, 204, session1, True)	
				
				# TESTs relativos a la operación PUT lista de componentes (Subir un componente al sistema) 
				# TEST 2
				print "TEST 2: Subir un componente al sistema, proporcionando una URI incorrecta."
				print "Status esperado: 404 "
				params = urllib.urlencode({'url': 'https://github.com/JuanFryS/badURI',
			            'component_id': 'twitterTimeline',
			            'description': 'Web component for obtain the timeline of Twitter using Polymer',
			            'social_network': 'twitter',
			            'input_type': 'None',
			            'output_type': 'tweet'
				})
				test_utils.make_request("PUT", request_uri, params, 404, session1)

				# TEST 3
				print "TEST 3: Subir un componente al sistema, proporcionando un parametro erróneo (red social)."
				print "Status esperado: 400 "
				params = urllib.urlencode({'url': 'https://github.com/JuanFryS/twitter-timeline',
			            'component_id': 'twitterTimeline',
			            'description': 'Web component for obtain the timeline of Twitter using Polymer',
			            'social_network': 'RedError' ,
			            'input_type': 'None',
			            'output_type': 'tweet'
				})
				test_utils.make_request("PUT", request_uri, params, 400, None)

				# TEST 4
				print "TEST 4: Subir un componente al sistema, proporcionando menos parámetros de los necesarios."
				print "Status esperado: 400 "
				params = urllib.urlencode({'url': 'https://github.com/JuanFryS/twitter-timeline',
			            'component_id': 'twitterTimeline',
			            'description': 'Web component for obtain the timeline of Twitter using Polymer',
			            'social_network': 'twitter' ,
			            'input_type': 'None'
				})
				test_utils.make_request("PUT", request_uri, params, 400, None)

				# Subimos dos componentes al sistema
				# TEST 5
				print "TEST 5: Subir un componente al sistema (componente 1)."
				print "Status esperado: 201 "
				params = urllib.urlencode({'url': 'https://github.com/JuanFryS/twitter-timeline',
			            'component_id': 'twitterTimeline',
			            'description': 'Web component for obtain the timeline of Twitter using Polymer',
			            'social_network': 'twitter' ,
			            'input_type': 'None',
			            'output_type': 'tweet'
				})
				test_utils.make_request("PUT", request_uri, params, 201, None)
				
				# TEST 6: Subir un componente al sistema (componente 2).
				print "TEST 6: Subir un componente al sistema (componente 2)."
				print "Status esperado: 201 "
				# request_uri = basepath
				params = urllib.urlencode({'url': 'https://github.com/JuanFryS/instagram-timeline',
			            'component_id': 'instagram-timeline',
			            'description': 'Web component for obtain the timeline of the social network Instagram using Polymer',
			            'social_network': 'instagram',
			            'input_type': 'None',
			            'output_type': 'photo'
				})
				test_utils.make_request("PUT", request_uri, params, 201, None)

				# TEST 7
				print "TEST 7: Subida de un componente repetido al sistema (componente 2)."
				print "Status esperado: 200 "
				params = urllib.urlencode({'url': 'https://github.com/JuanFryS/instagram-timeline',
			            'component_id': 'instagram-timeline',
			            'description': 'New description for the web component (Description changed in TEST 7)',
			            'social_network': 'instagram',
			            'input_type': 'None',
			            'output_type': 'photo'
				})
				test_utils.make_request("PUT", request_uri, params, 200, None)

			elif option == "obtención":
				# TESTs relativos al método GET Lista de componentes 
				request_uri = basepath
				params = urllib.urlencode({})
				
				# TEST 7
				print "TEST 7: Obtener la lista de componentes, sin proporcionar una cookie de sesion"
				print "Status esperado: 401 "
				test_utils.make_request("GET", request_uri, params, 401, None)	

				# TEST 8
				print "TEST 8: Obtener la lista de componentes, proporcionando una cookie de sesion (Sin parámetros)"
				print "Status esperado: 200"
				test_utils.make_request("GET", request_uri, params, 200, session1)

				# # Casos de obtención de lista de componentes, aplicando criterios de filtrado
				# # TEST 9
				# print "TEST 9: Obtener la lista de componentes, proporcionando una cookie de sesion"
				# print "(parámetro de filtrado por red social)"
				# print "Status esperado: 200"
				# request_uri = basepath + "?social_network=twitter"
				# test_utils.make_request("GET", request_uri, params, 200, session1)

				# # TEST 10
				# print "TEST 10: Obtener la lista de componentes, proporcionando una cookie de sesion"
				# print "(parámetro de filtrado por usuario)"
				# print "Status esperado: 200"
				# request_uri = basepath + "?filter=user"
				# test_utils.make_request("GET", request_uri, params, 200, session1)

				# # TEST 11
				# print "TEST 11: Obtener la lista de componentes, proporcionando una cookie de sesion"
				# print "(formato de lista completo)"
				# print "Status esperado: 200"
				# request_uri = basepath + "?format=all"
				# test_utils.make_request("GET", request_uri, params, 200, session1)

				# # TEST 12
				# print "TEST 12: Obtener la lista de componentes, proporcionando una cookie de sesion"
				# print "(Combinamos el parámetro de filtrado por red social y el filtrado por usuario con el formato de lista completo)"
				# print "Status esperado: 200"
				# request_uri = basepath + "?social_network=twitter&filter=user&format=all"
				# test_utils.make_request("GET", request_uri, params, 200, session1)
				
				# TESTs relativos al metodo GET Componente (obtener info de un componente en particular)
				# TEST 9
				print "TEST 9: Obtener información sobre componente 1, sin proporcionar cookie de usuario"
				print "Status esperado: 401"
				request_uri = basepath + '/twitter-timeline'
				test_utils.make_request("GET", request_uri, params, 401, None)	
				
				# TEST 10
				print "TEST 10: Obtener información sobre un componente no existente en el sistema"
				print "Status esperado: 404"
				request_uri = basepath + '/componenteERROR'
				test_utils.make_request("GET", request_uri, params, 404, session1)	

				# TEST 11
				print "TEST 11: Obtener información sobre el componente 1"
				print "Status esperado: 200"
				request_uri = basepath + '/twitter-timeline'
				test_utils.make_request("GET", request_uri, params, 200, session1)	
				
				# TEST 12
				print "TEST 12: Obtener información sobre el componente 2"
				print "Status esperado: 200"
				request_uri = basepath + '/instagram-timeline'
				test_utils.make_request("GET", request_uri, params, 200, session1)	
				
				# TODO TEST GET Component con formato completo
				# TODO Cubrir casos de obtención de info completa sobre componentes que no son del usuario
			
			elif option == "modificación":
				# TESTs relativos al método POST Componente (modificar info de un componente)
				# TEST 13
				print "TEST 13: Modificar información sobre un componente, sin proporcionar una cookie de sesión"
				print "Status esperado: 401"
				request_uri = basepath + '/twitter-timeline'
				test_utils.make_request("POST", request_uri, params, 401, None)	

				# TEST 14
				print "TEST 14: Modificar información sobre el componente 1 (Valor incorrecto para parámetro X)"
				print "Status esperado: 400"
				request_uri = basepath + '/twitter-timeline'
				params = urllib.urlencode({'x_axis': 'string',
						'y_axis': 250})
				test_utils.make_request("POST", request_uri, params, 400, session1)

				# TEST 15
				print "TEST 15: Modificar información sobre el componente 2 (Valor incorrecto para parámetro Rating, mayor que 5)"
				print "Status esperado: 400"
				request_uri = basepath + '/instagram-timeline'
				params = urllib.urlencode({'rating': 6})
				test_utils.make_request("POST", request_uri, params, 400, session1)

				# TEST 16
				print "TEST 16: Modificar información sobre el componente 1, caso cambiar posición del componente (x:150, y:250)"
				print "Status esperado: 200"
				request_uri = basepath + '/twitter-timeline'
				params = urllib.urlencode({'x_axis': 150,
						'y_axis': 250})
				test_utils.make_request("POST", request_uri, params, 200, session1)

				# TEST 17
				print "TEST 17: Modificar información sobre el componente 2, caso cambiar valoración. (Rating: 4.5)"
				print "Status esperado: 200"	
				request_uri = basepath + '/instagram-timeline'
				params = urllib.urlencode({'rating': 4.5})
				test_utils.make_request("POST", request_uri, params, 200, session1)

				# TEST 18
				print "TEST 18: Obtención de la lista de componentes del sistema, para verificar "
				print "que se ha modificado la información solicitada en las anteriores pruebas"
				print "Status esperado: 200"
				request_uri = basepath
				params = urllib.urlencode({})
				test_utils.make_request("GET", request_uri, params, 200, session1)
				
			elif option == 'borrado':
				params = urllib.urlencode({})
				# TESTs relativos al método DELETE Componente 
				# TEST 19
				print "TEST 19: Borrar componente 1 del sistema"
				print "Status esperado: 204 "
				request_uri = basepath + '/twitter-timeline'
				test_utils.make_request("DELETE", request_uri, params, 204, None)
				
				# TEST 20
				print "TEST 20: Borrar componente 1 del sistema (el componente se había borrado previamente) "
				print "Status esperado: 404 "
				# request_uri = basepath + '/twitter-timeline'
				test_utils.make_request("DELETE", request_uri, params, 404, None)	

				# TEST 21
				print "TEST 21: Borrar componente 2 del sistema"
				print "Status esperado: 204 "
				request_uri = basepath + '/instagram-timeline'
				test_utils.make_request("DELETE", request_uri, params, 204, None)
			
			# Realizamos logout en el sistema, tras llevar a cabo las pruebas
			# POST-TEST 1: Hacer logout en el sistema mediante googleplus
			request_uri = "/api/oauth/googleplus/logout"
			print "POST-TEST 1: Haciendo petición POST a " + request_uri + " (logout)\n Ignorar el status de este caso"
			params = urllib.urlencode({})
			test_utils.make_request("POST", request_uri, params, 200, session1)
		
		else:
			print "Error: Parámetro incorrecto"
			print "Uso: python api_componentes_tester.py {subida|obtención|modificación|borrado}"

	else:
		print "Error: es obligatorio proporcionar un parámetro válido para indicar que funcionalidad u operación se pretende testear"
		print "Uso: python api_componentes_tester.py {subida|obtención|modificación|borrado}"


	test_utils.closeConnection()
if __name__ == "__main__":
	main()