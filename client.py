import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='127.0.0.1'
PORT=65432

try: 
    client_socket.connect((HOST,PORT))
except ConnectionRefusedError :
    print("Server is not ready, pls try again later")
    raise SystemExit

# message = "HELLO SERVER"
# client_socket.sendall(message.encode('utf-8'))


try:
    while True:
        message = input()
        if message == '/quit':
            break
            
        client_socket.sendall(message.encode('utf-8'))

        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

        
finally:
    client_socket.close()
