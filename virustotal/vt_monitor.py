#!/usr/bin/env python3
"""
VirusTotal Malware Monitor for Cowrie Honeypot
Monitors downloaded files and checks them against VirusTotal API
"""

import os
import time
import hashlib
import requests
import json
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY"  # Replace with your actual key
COWRIE_DOWNLOADS = "/var/lib/docker/volumes/cowrie-honeypot_cowrie-var/_data/lib/cowrie/downloads"
CHECKED_FILES = "checked_files.json"
CHECK_INTERVAL = 300  # Check every 5 minutes

# Email configuration
ENABLE_EMAIL = True
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "your-email@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "your-gmail-app-password"  # Your 16-char app password
EMAIL_TO = "your-email@gmail.com"  # Where to send alerts

def calculate_sha256(filepath):
    """Calculate SHA256 hash of a file"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_virustotal(file_hash):
    """Check file hash against VirusTotal API"""
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": VT_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": "File not found in VirusTotal database"}
        else:
            return {"error": f"API returned status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def load_checked_files():
    """Load list of already checked files"""
    if os.path.exists(CHECKED_FILES):
        with open(CHECKED_FILES, 'r') as f:
            return json.load(f)
    return {}

def save_checked_files(checked):
    """Save list of checked files"""
    with open(CHECKED_FILES, 'w') as f:
        json.dump(checked, f, indent=2)

def send_email_alert(filename, detection_rate, vt_link):
    """Send email alert when malware is detected"""
    if not ENABLE_EMAIL:
        return
    
    try:
        subject = f"[MALWARE ALERT] New malware detected: {filename[:32]}..."
        
        body = f"""
Cowrie Honeypot Malware Alert

A new malware sample has been detected and analyzed:

File Hash: {filename}
Detection Rate: {detection_rate}
VirusTotal Link: {vt_link}

This is an automated alert from your threat intelligence lab.
"""
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"[*] Email alert sent to {EMAIL_TO}")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

def scan_downloads():
    """Scan Cowrie downloads directory for new files"""
    checked = load_checked_files()
    new_files = 0
    
    print(f"[*] Scanning {COWRIE_DOWNLOADS} for new malware samples...")
    
    for filename in os.listdir(COWRIE_DOWNLOADS):
        filepath = os.path.join(COWRIE_DOWNLOADS, filename)
        
        # Skip if already checked
        if filename in checked:
            continue
        
        # Skip if not a file
        if not os.path.isfile(filepath):
            continue
        
        print(f"\n[+] New file detected: {filename}")
        
        # Check against VirusTotal
        print(f"[*] Querying VirusTotal...")
        result = check_virustotal(filename)  # filename is already SHA256
        
        if "error" in result:
            print(f"[!] Error: {result['error']}")
            checked[filename] = {"error": result['error'], "timestamp": time.time()}
        else:
            data = result.get('data', {})
            attributes = data.get('attributes', {})
            stats = attributes.get('last_analysis_stats', {})
            
            malicious = stats.get('malicious', 0)
            total = sum(stats.values())
            
            print(f"[*] Detection: {malicious}/{total} engines flagged as malicious")
            
            checked[filename] = {
                "detection_rate": f"{malicious}/{total}",
                "timestamp": time.time(),
                "malicious": malicious > 0
            }
            
            if malicious > 0:
                print(f"[!] MALWARE DETECTED: {filename}")
                vt_link = f"https://www.virustotal.com/gui/file/{filename}"
                send_email_alert(filename, f"{malicious}/{total}", vt_link)
        
        new_files += 1
        save_checked_files(checked)
        
        # Rate limiting - VT free tier allows 4 requests/minute
        time.sleep(16)
    
    if new_files == 0:
        print("[*] No new files found")
    
    return new_files

def main():
    """Main monitoring loop"""
    print("="*60)
    print("VirusTotal Malware Monitor")
    print("="*60)
    
    if VT_API_KEY == "YOUR_API_KEY_HERE":
        print("[!] ERROR: Please set your VirusTotal API key in the script")
        return
    
    print(f"[*] Monitoring: {COWRIE_DOWNLOADS}")
    print(f"[*] Check interval: {CHECK_INTERVAL} seconds")
    print(f"[*] Starting monitoring loop...\n")
    
    try:
        while True:
            scan_downloads()
            print(f"\n[*] Sleeping for {CHECK_INTERVAL} seconds...")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped by user")

if __name__ == "__main__":
    main()
