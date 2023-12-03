import socket
import json

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        server_socket.bind(server_address)
        server_socket.listen(1)

        print(f"Serverul ascultă la {server_address}")

        while True:
            print("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()
            print(f"Conexiune de la {client_address}")

            try:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    if data.strip() and data.decode().startswith('{') and data.decode().endswith('}'):
                        decoded_data = json.loads(data.decode())
                        print(f"Date primite de la client: {decoded_data}")

            except json.JSONDecodeError as json_error:
                print(f"Eroare la decodificarea JSON: {str(json_error)}")

            except Exception as e:
                print(f"Eroare la primirea datelor: {str(e)}")

            finally:
                client_socket.close()

    except OSError as os_error:
        print(f"Eroare la legarea socket-ului: {str(os_error)}")

    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
