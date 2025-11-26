# Python Debugging in VSCode

## Setup Verified
- Virtual environment: ✅ Active (`(venv)` shown in terminal)
- Debugger: ✅ Working (debugpy extension)
- Output: ✅ Displaying correctly

## Debugging Commands
- **F5**: Start debugging
- **F9**: Toggle breakpoint
- **F10**: Step over
- **F11**: Step into
- **Shift+F11**: Step out
- **Ctrl+Shift+F5**: Restart debugging

## Output Configuration

### Debug Console (Recommended)
- Set `"console": "internalConsole"` in launch.json
- Output appears in Debug Console panel
- Cleaner debugging experience

### Terminal Output
- Set `"console": "integratedTerminal"` in launch.json
- Output appears in terminal
- Shows full command execution

## Configuration File
Created `.vscode/launch.json` with Debug Console setting