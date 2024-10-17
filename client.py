import socket


def send_command(command, server_address='SERVER_IP', server_port=8820):
    client_socket = socket.socket()
    client_socket.connect(
        (server_address, server_port))  # The address and port will be as they are everytime you call the fumction

    cmd_size = str(len(command)).zfill(2)
    full_command = cmd_size + command

    try:
        client_socket.send(full_command.encode())  # Sending the wanted command

        # Receive response
        response_length = int(client_socket.recv(10).decode())
        response = client_socket.recv(response_length).decode()

        print(response)  # Printing the response
    finally:
        client_socket.close()  # Closing the client socket after every use


def main():
    while True:
        command = input("Enter command: ")
        send_command(command)

        if command.lower() == "exit":
            break  # Terminating the program


if __name__ == "__main__":
    main()
