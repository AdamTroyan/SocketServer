import glob
import os
import shutil
import socket
import subprocess
import pyautogui


def setup_server_socket(port=8820):
    server_socket = socket.socket()  # Creates the socket object

    server_socket.bind(("0.0.0.0", port))  # Allows to connect to this pc from every ip
    server_socket.listen()  # Listening to every interaction with the server

    print("Server is up and running")
    return server_socket  # Returns the "socket" object


def send_response(response, client_socket):
    res_length = str(len(response)).zfill(10)  # Adding the "message" length to the beginning of the message
    client_socket.send((res_length + response).encode())  # Sending response to the server


def handle_client_command(command, client_socket):
    try: # The commands
        if command.startswith("dir"):
            handle_dir_command(command, client_socket)
        elif command.startswith("delete"):
            handle_delete_command(command, client_socket)
        elif command.startswith("copy"):
            handle_copy_command(command, client_socket)
        elif command.startswith("execute"):
            handle_execute_command(command, client_socket)
        elif command == "take_screenshot":
            handle_screenshot_command(client_socket)
        elif command == "exit":
            client_socket.close()

            send_response("You have terminated the connection.", client_socket)  # Terminating the connection | Closing the client socket
            print("The client have terminated the connection.")
        else:
            send_response("Invalid command", client_socket)
    except Exception as e:
        send_response(f"Error: {e}", client_socket)


def handle_dir_command(command, client_socket):
    all_data = command.split()  # Split the data to args- "dir[0] path[1]"

    if len(all_data) > 1:
        files = glob.glob(all_data[1])  # Check if the file is exist by its path

        if files:  # If do...
            send_response(files, client_socket)
        else:
            send_response("No file found.", client_socket)
    else:
        send_response("Please specify file", client_socket)


def handle_delete_command(command, client_socket):
    all_data = command.split()

    if len(all_data) > 1:
        file = all_data[1]

        if os.path.exists(file):  # Check if the file is exists
            try:
                os.remove(file)

                send_response(f"The file {file} successfully deleted.", client_socket)
                print(f"The file {file} successfully deleted.")
            except Exception as e:
                send_response(f"Error deleting file: {e}", client_socket)
        else:
            send_response("This file does not exist", client_socket)
    else:
        send_response("Please specify file", client_socket)


def handle_copy_command(command, client_socket):
    all_data = command.split()

    if len(all_data) > 2:
        src, dst = all_data[1], all_data[2]  # Declaring the source of the original file and the destination wanted.

        if os.path.exists(src):  # Checks if the source exists
            try:
                shutil.copy(src, dst)  # Copying the file from the source to the destination

                send_response(f"The file {src} successfully copied to {dst}", client_socket)
                print(f"The file {src} successfully copied to {dst}")
            except Exception as e:
                send_response(f"Error copying file: {e}", client_socket)
        else:
            send_response("This file does not exist", client_socket)
    else:
        send_response("Please specify source and destination files", client_socket)


def handle_execute_command(command, client_socket):
    file = command.removeprefix("execute ").strip()

    try:
        result = subprocess.call(file, shell=True)  # Calling the process...

        if result == 0:  # Check if the process actually opened
            send_response(f"The program {file} successfully opened.", client_socket)
            print(f"The program {file} successfully opened.")
        else:
            send_response(f"The program {file} did not open successfully.", client_socket)
    except Exception as e:
        send_response(f"Error executing file: {e}", client_socket)


def handle_screenshot_command(client_socket):
    try:
        screenshot_path = r"C:\Users\pover\Desktop\screenshot.png"

        image = pyautogui.screenshot()  # Take a screenshot
        image.save(screenshot_path)  # Save the screenshot in specific destination

        send_response(f"Screenshot saved in {screenshot_path}", client_socket)
        print(f"Screenshot saved in {screenshot_path}")
    except Exception as e:
        send_response(f"Error taking screenshot: {e}", client_socket)


def main():
    server_socket = setup_server_socket()  # The declaration of the socket we saw in the beginning.

    while True:
        (c_socket, c_address) = server_socket.accept()
        print(f"Client {c_address[0]} Connected")

        try:
            cmd_size = c_socket.recv(2).decode()  # Command handler -> the first result from the client
            cmd_data = c_socket.recv(int(cmd_size)).decode()

            handle_client_command(cmd_data.lower(), c_socket)
        finally:
            c_socket.close()


if __name__ == "__main__":
    main()
