import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST='127.0.0.1'
PORT=65432
server_socket.bind((HOST,PORT))


server_socket.listen()
print(f"Server listening on {HOST}:{PORT}")

client_socket, client_address = server_socket.accept()
print(f"Connected by {client_address}")

try:
    while True:
        data = client_socket.recv(1024)
        print(f"Data recieved from client {data.decode('utf-8')}")
        client_socket.sendall(data)
        if data.decode('utf-8') == '':
            break
            
finally:
    server_socket.close()
    client_socket.close()


