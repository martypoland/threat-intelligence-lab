# Threat Intelligence Lab

Automated threat intelligence platform combining SSH honeypot deployment, real-time log analysis with Loki/Grafana, and automated malware detection via VirusTotal integration.

## Overview

This project demonstrates end-to-end threat detection and malware analysis capabilities through a production-grade honeypot deployment. The system captures real-world SSH attacks, analyzes attacker behavior patterns, and automatically identifies malware samples using threat intelligence feeds.

## Architecture

**Components:**
- **Cowrie SSH Honeypot** - Captures live SSH attack traffic on port 22
- **Loki + Grafana** - Real-time log aggregation and visualization
- **Promtail** - Log shipping and parsing
- **VirusTotal Integration** - Automated malware hash analysis via Python script
- **Ubuntu 24.04 LTS** - Hardened server deployment

**Security Configuration:**
- Real SSH service relocated to high port with IP-restricted firewall rules
- Cowrie exposed on port 22 to maximize attack surface for intelligence gathering
- UFW firewall configured for defense-in-depth
- Root login disabled, key-based authentication enforced

## Deployment

### Prerequisites
- Ubuntu 24.04 LTS server
- Docker and Docker Compose installed
- Minimum 4GB RAM recommended

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/martypoland/threat-intelligence-lab.git
cd threat-intelligence-lab
```

2. **Deploy Cowrie honeypot**
```bash
docker-compose up -d
```

3. **Deploy Loki/Grafana stack** (optional)
```bash
cd loki/
docker-compose up -d
```

4. **Configure VirusTotal monitoring** (optional)
```bash
cd virustotal/
# Add your VirusTotal API key to config
python3 vt_monitor.py
```

### Security Hardening

Before exposing the honeypot to the internet:
- Move SSH to a non-standard high port (e.g., 52847)
- Disable root login and password authentication
- Configure UFW firewall to restrict management access
- Only expose port 22 (honeypot) to public internet

See detailed setup guide in [SETUP.md](SETUP.md) (optional - for very detailed instructions)

### Cowrie Honeypot Setup

**Docker Compose Configuration:**

See [`docker-compose.yml`](docker-compose.yml) for the complete configuration.

**Key Configuration:**
- Honeypot exposed on port 22 (standard SSH port for maximum attack exposure)
- Persistent volumes for configuration and log data
- Automatic restart on failure for continuous operation

**Deployment:**
```bash
docker-compose up -d
```
```

**Attack Analysis**

This honeypot captured 18,974 attack events from 129 unique IP addresses over [X] days, with 11 malware samples downloaded.

**Key Findings:**
- 50% of attacks targeted root account
- Coordinated botnet activity using paired credentials
- SSH backdoor installation attempts observed

See detailed analysis in [Attack Report](findings/attack-report.md)

## Malware Samples

[Details about captured malware - we can document the SSH key backdoor and any other samples]

## Skills Demonstrated

- Honeypot deployment and configuration
- Log aggregation and analysis (Loki/Grafana)
- Security automation (Python scripting)
- Threat intelligence integration (VirusTotal API)
- Linux system hardening
- Docker containerization
- Firewall configuration and network security
- Malware analysis techniques

## Future Enhancements

- [ ] Geographic attack visualization
- [ ] Automated alerting for malware detection
- [ ] Integration with additional threat intel feeds
- [ ] Machine learning for attack pattern recognition

## License

MIT License
