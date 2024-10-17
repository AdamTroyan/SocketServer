# Socket File Management Server

This Python application implements a socket server that allows remote control over file operations, such as listing, deleting, copying files, executing programs, and taking screenshots.

## Features

- List files in a directory
- Delete specified files
- Copy files from one location to another
- Execute programs
- Take screenshots

## Requirements

- **Python:** 3.x
- **Required libraries:**
  - `pyautogui`

## Installation

1. Clone the repository or download the source code.
2. Install the required libraries using pip:
   ```bash
   pip install pyautogui
   ```

## Usage

1. **Run the server:**
   ```bash
   python server.py
   ```

2. **Connect a client to the server and issue commands in the following format:**
   - **List files:** 
     ```
     dir <path>
     ```
   - **Delete file:** 
     ```
     delete <file_path>
     ```
   - **Copy file:** 
     ```
     copy <source_path> <destination_path>
     ```
   - **Execute program:** 
     ```
     execute <file_path>
     ```
   - **Take screenshot:** 
     ```
     take_screenshot
     ```
   - **Exit:** 
     ```
     exit
     ```

## Example Commands

- **To list files in a directory:**
  ```bash
  dir C:\Users\YourUsername\Documents
  ```

- **To delete a file:**
  ```bash
  delete C:\Users\YourUsername\Documents\example.txt
  ```

- **To copy a file:**
  ```bash
  copy C:\Users\YourUsername\Documents\example.txt C:\Users\YourUsername\Documents\copy_example.txt
  ```

- **To execute a program:**
  ```
  execute C:\Path\To\Your\Program.exe
  ```

- **To take a screenshot:**
  ```
  take_screenshot
  ```

- **To exit the connection:**
  ```
  exit
  ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
