# SocketServer

A powerful Python-based remote administration tool using socket connections for system control and file management.

## 🚀 Features

- **Remote File Management**: List, delete, and copy files remotely
- **Program Execution**: Execute programs and system commands
- **Screenshot Capture**: Take and transfer screenshots
- **Socket Communication**: Robust client-server architecture
- **Cross-Platform Support**: Works on Windows, Linux, and macOS
- **System Administration**: Remote system control and management

## 🛠️ Technologies

- **Language**: Python 3
- **Networking**: Socket programming
- **Libraries**: pyautogui, subprocess, shutil, glob
- **Architecture**: Client-Server model

## 📋 Requirements

- Python 3.6 or later
- `pyautogui` library for screenshot functionality
- Network connectivity between client and server

## 🚀 Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AdamTroyan/SocketServer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd SocketServer
   ```

3. Install required dependencies:
   ```bash
   pip install pyautogui
   ```

### Usage

#### Starting the Server
```bash
python server.py
```

#### Available Commands

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
- **Execute program:** 
  ```
  execute <file_path>
  ```
- **Take screenshot:** 
  ```
  take_screenshot
  ```
- **Exit connection:** 
  ```
  exit
  ```

## 📁 Project Structure

```
SocketServer/
├── server.py                  # Main server application
├── client.py                  # Client connection script
├── LICENSE                    # License information
└── README.md                  # Project documentation
```

## 🎯 Example Usage

- **List directory contents:**
  ```bash
  dir C:\Users\Username\Documents
  ```

- **Delete a file:**
  ```bash
  delete C:\Users\Username\Documents\example.txt
  ```

- **Copy files:**
  ```bash
  copy C:\source.txt C:\destination.txt
  ```

- **Execute programs:**
  ```bash
  execute C:\Path\To\Program.exe
  ```

- **Capture screenshot:**
  ```bash
  take_screenshot
  ```

## ⚠️ Security Considerations

- **Legal Use Only**: This tool is for legitimate system administration
- **Network Security**: Use only on networks you own and control
- **Authentication**: Consider implementing authentication for production use
- **Firewall**: Configure appropriate firewall rules

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Adam Troyan** - [GitHub Profile](https://github.com/AdamTroyan)

## ⚖️ Legal Notice

This software is intended for legitimate system administration purposes only. Users are responsible for complying with all applicable laws and regulations.

---

*Built with ❤️ for system administration and remote management*

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
