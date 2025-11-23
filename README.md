 eSim Automated Tool Manager

An automated tool for managing eSim dependencies and configurations.

Features Implemented

- ✅ Dependency Checker: Automatically checks if required tools are installed
- ✅ User Interface: Simple CLI menu for easy interaction
- ✅ Cross-platform support (Windows, Linux, Mac)
- ✅ Clear feedback on missing dependencies
- ✅ System information display

## Requirements Met

This project implements 2 of the 6 requirements:

1. **Requirement 4 - Dependency Checker**: Checks all necessary dependencies for eSim
2. **Requirement 5 - User Interface**: Provides a user-friendly CLI interface

## Installation

### Prerequisites
- Python 3.6 or higher

### Steps
1. Clone this repository
2. Navigate to the project directory
3. Run the tool:
```bash
   python tool_manager.py
```

## Usage

When you run the tool, you'll see a menu with options:

1. **Check Dependencies**: Scans your system for required eSim tools
2. **View System Information**: Displays your OS and Python details
3. **View Installed Tools**: Lists all tools managed by this manager
4. **Exit**: Closes the application

## Tools Checked

The tool manager checks for:
- Python
- Git
- Ngspice
- Make

## Technical Details

- **Language**: Python 3
- **Libraries Used**: 
  - `subprocess` (running system commands)
  - `platform` (detecting OS)
  - Built-in libraries only (no external dependencies)

## Architecture
```
┌─────────────────────┐
│   User Interface    │
│      (CLI Menu)     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   ToolManager Class │
│   (Core Logic)      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Dependency Checker  │
│     Module          │
└─────────────────────┘
```

## Error Handling

- Handles missing tools gracefully
- Timeout protection for hanging commands
- Clear error messages for users
- Exception handling for unexpected errors

## Future Enhancements

- Automatic tool installation
- Update checking functionality
- Configuration file support
- GUI interface
- Support for more eSim tools

## Author

Deepti Srivastava

## Submission

eSim Winter Internship 2025 - Task 3
```



