# Futures Calculator 
:warning: **Not an official product**  
This project is an imitation of the [Binance Futures Calculator](https://www.binance.com/en/futures/BTCUSDT_PERPETUAL/calculator), 
designed to compute trading metrics such as PnL (Profit and Loss), liquidation price, take profit / stop loss prices and target price. 
The application is built using the [PySide6](https://pypi.org/project/PySide6/) library and designed with Qt Creator, 
providing a user-friendly interface for simplified trading calculations.

## Prerequisites
- Installed [Qt Creator](https://www.qt.io/product/development-tools)

- `venv`
  > Before installing dependencies it is highly recommended to work in [virtual environment](https://docs.python.org/3/library/venv.html).
  > If you want to create virtual environment `.venv`, use following command:
  > ```bash
  >  python -m venv .venv
  >  ```
  > Make sure it is activated after installation

## Install dependencies 
```bash
pip install -r requirements.txt
```

## Executable 
To create an executable file without running the application within the Qt Creator
- **Windows**
  - Compile the application using `Release` build (instead of `Debug`)
  - Open `cmd` (Command Prompt) and position yourself in the `Release` directory
  - Use following command to generate everything needed:
    
    ```bash
    windeployqt your_app.exe
    ```
- **Linux**
  - Compile the application using `Release` build (instead of `Debug`)
  - Open `terminal` and position yourself in the `Release` directory
  - Use following command to generate everything needed:
    
    ```bash
    linuxdeployqt your_app.exe -appimage
    ```
  - Use following command to make `.AppImage` executable:
 
    ```bash
    chmod +x your_app.AppImage
    ```
- **macOS**
  - Compile the application using `Release` build (instead of `Debug`)
  - Open `terminal` and position yourself in the `Release` directory
  - Use following command to generate everything needed:
    
    ```bash
    macdeployqt your_app.app
    ```
