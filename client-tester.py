import socket

def start_client():
    # Creează un socket de tip TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Adresa și portul la care ne conectăm
    server_address = ('localhost', 12345)

    # Conectează-te la server
    client_socket.connect(server_address)

    # Trimite date către server
    message = "Hello, server!"
    client_socket.sendall(message.encode())

    # Închide conexiunea cu serverul
    client_socket.close()

if __name__ == "__main__":
    start_client()
