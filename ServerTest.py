import socket

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
RECEIVED_FILE_PATH = 'received_audio.wav'
SEND_FILE_PATH = 'send_audio.wav'  # Path to the file you want to send back

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive a file from the client
    receive_file(conn, RECEIVED_FILE_PATH)

    # Wait for the client to indicate it's ready to receive the output file
    ready_message = "Ready to receive output file. Send 'GET_FILE' to request."
    conn.sendall(ready_message.encode())

    # Wait for the client to request the file
    request = conn.recv(1024).decode()
    if request == "GET_FILE":
        # Send a file back to the client
        send_file(conn, SEND_FILE_PATH)

    conn.close()
