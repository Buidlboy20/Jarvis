import socket
import threading
import jarvis

def handle_client(connection, addr):
    print(f"Connection from {addr}")
    RECEIVED_FILE_PATH = f'received_audio_{addr[1]}.wav'
    SEND_FILE_PATH = 'welcome.wav'  # Path to the file you want to send back
    
    # Receive a file from the client
    receive_file(connection, RECEIVED_FILE_PATH)

    # Wait for the client to indicate it's ready to receive the output file
    ready_message = "Ready to receive output file. Send 'GET_FILE' to request."
    connection.sendall(ready_message.encode())

    # Wait for the client to request the file
    request = connection.recv(1024).decode()
    if request == "GET_FILE":
        # Send a file back to the client
        send_file(connection, SEND_FILE_PATH)

    connection.close()

def receive_file(connection, file_path):
    with open(file_path, 'wb') as f:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            f.write(data)
    print(f"File received and saved as {file_path}")

def send_file(connection, file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            connection.sendall(data)
    print(f"File {file_path} sent successfully")

# Configuration
HOST = '0.0.0.0'
PORT = 5000

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Listen for up to 5 connections
print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
