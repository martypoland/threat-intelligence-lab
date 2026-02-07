# VirusTotal Malware Monitor

Automated malware detection system that monitors Cowrie honeypot downloads and checks them against VirusTotal's threat intelligence database.

## Features

- **Automated scanning** of new malware samples every 5 minutes
- **VirusTotal integration** for comprehensive threat analysis
- **Email alerts** when malware is detected
- **Persistent tracking** of analyzed files to avoid duplicate API calls
- **Rate limiting** to comply with VirusTotal free tier (4 requests/minute)

## Setup

### Prerequisites

- Python 3.x
- VirusTotal API key (free at https://www.virustotal.com/gui/join-us)
- Gmail account with app password (for email alerts)

### Installation

1. **Install required Python packages:**
```bash
sudo apt install python3-requests
```

2. **Configure the script:**

Edit `vt_monitor.py` and set your credentials:
```python
VT_API_KEY = "your_virustotal_api_key"
EMAIL_FROM = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
EMAIL_TO = "your-email@gmail.com"
```

**Getting a Gmail App Password:**
- Enable 2-factor authentication on your Google account
- Go to https://myaccount.google.com/apppasswords
- Create an app password for "Cowrie VT Monitor"
- Use the 16-character password in the script

3. **Make the script executable:**
```bash
chmod +x vt_monitor.py
```

### Usage

**Run manually (for testing):**
```bash
sudo python3 vt_monitor.py
```

**Run in background (continuous monitoring):**
```bash
sudo nohup python3 vt_monitor.py > vt_monitor.log 2>&1 &
```

**View logs:**
```bash
tail -f vt_monitor.log
```

**Stop the monitor:**
```bash
sudo pkill -f vt_monitor.py
```

## How It Works

1. Scans the Cowrie downloads directory every 5 minutes
2. Identifies new files not yet analyzed
3. Queries VirusTotal API using file SHA256 hash
4. Records detection rates in `checked_files.json`
5. Sends email alerts for malicious files
6. Rate limits requests to comply with VirusTotal free tier

## Output

The script maintains a `checked_files.json` file tracking:
- File hash
- Detection rate (e.g., "44/76")
- Timestamp of analysis
- Malicious status

**Example email alert:**
```
[MALWARE ALERT] New malware detected

File Hash: 94f2e4d8d4436874785cd14e6e6d403507b8750852f7f2040352069a75da4c00
Detection Rate: 44/76
VirusTotal Link: https://www.virustotal.com/gui/file/94f2e4d8...
```
![Malware Email Alert](screenshots/malware-email-alert.png)

## API Rate Limits

VirusTotal free tier allows:
- 4 requests per minute
- 500 requests per day

The script automatically enforces 16-second delays between requests to stay within limits.
