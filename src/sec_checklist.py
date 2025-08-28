
#!/usr/bin/env python3
"""
sec_checklist.py — quick baseline host check (cross-platform).
Prints basic system info, firewall status, and listening TCP ports.
"""
import json, platform, shutil, subprocess, sys

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT).strip()
    except Exception as e:
        return f"ERR: {e}"
        
def firewall_status():
    # macOS Application Firewall
    if sys.platform == "darwin":
        # returns "Firewall is enabled. (State = 1)" or "Firewall is disabled. (State = 0)"
        return run("/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate")
    # Windows
    if sys.platform.startswith("win"):
        return run("netsh advfirewall show allprofiles")
    # Linux (common tools)
    elif shutil.which("ufw"):
        return run("ufw status")
    elif shutil.which("firewall-cmd"):
        return run("firewall-cmd --state")
    else:
        return "Unknown/No common firewall tool detected"

def listening_tcp():
    if shutil.which("ss"):
        return run("ss -lnt")
    elif shutil.which("netstat"):
        return run("netstat -an | grep LISTEN || netstat -an | findstr LISTEN")
    else:
        return "ss/netstat not found"

def main():
    report = {
        "os": platform.platform(),
        "python": sys.version.split()[0],
        "hostname": run("hostname"),
        "firewall_status": firewall_status(),
        "listening_tcp": listening_tcp(),
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()

