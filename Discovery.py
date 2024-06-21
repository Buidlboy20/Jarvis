import socket

def start():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 9999))
    print("Server running...")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Received request from {client_address}: {message.decode()}")
        server_socket.sendto(b"Hello, client!", client_address)
    server_socket.close()
