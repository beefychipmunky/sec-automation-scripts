# sec-automation-scripts
small, real world Python tools for entry level security work
## What is this?
Small, real-world Python tools for entry-level security work. First tool: `sec_checklist.py` prints basic host info, firewall status, and listening TCP ports.

## Quickstart (run locally)

**Requirements:** Python 3.8+  
*(Optional)* Git (recommended)

### macOS / Linux (Terminal)
```bash
git clone https://github.com/beefychipmunky/sec-automation-scripts.git
cd sec-automation-scripts
python3 src/sec_checklist.py
```

### Windows (PowerShell)
```powershell
git clone https://github.com/beefychipmunky/sec-automation-scripts.git
cd sec-automation-scripts
py src\sec_checklist.py
# or: python src\sec_checklist.py
```

### No Git? Download ZIP
- Click the green **Code** button → **Download ZIP**  
- Unzip, open Terminal/PowerShell in that folder, and run the command above for your OS.

### Sample output
```json
{
  "os": "macOS-11.7.10-x86_64-i386-64bit",
  "python": "3.8.x",
  "hostname": "YOUR-HOST",
  "firewall_status": "Firewall is enabled. (State = 1)",
  "listening_tcp": "tcp6      0      0  *.51529   *.*   LISTEN"
}
```

### Save output to a file
**macOS / Linux**
```bash
python3 src/sec_checklist.py > report.json
```
