import socket

HOST, PORT = 'localhost', 52557
payLoadData = '{    "glossary": {        "title": "example glossary",		"GlossDiv": {            "title": "S",		"GlossList": {                "GlossEntry": {                   "ID": "SGML",					"SortAs": "SGML",				"GlossTerm": "Standard Generalized Markup Language",					"Acronym": "SGML",				"Abbrev": "ISO 8879:1986",					"GlossDef": {                        "para": "A meta-markup language, used tocreate markup languages such as DocBook.",					"GlossSeeAlso": ["GML", "XML"]                    },					"GlossSee": "markup"                }            }        }    }}'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print ('Starting web-server on port ' + str(PORT))
while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024)
    print (request)

    http_response = """\
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *

""" + payLoadData

    client_socket.sendall(http_response.encode())
    client_socket.close()
