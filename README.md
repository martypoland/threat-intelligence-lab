# threat-intelligence-lab
Automated threat intelligence platform combining SSH honeypot deployment, real-time log analysis with Loki/Grafana, and automated malware detection via VirusTotal integration
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

### Infrastructure
- Platform: DigitalOcean VPS (4GB RAM, 2 vCPU)
- OS: Ubuntu 24.04 LTS
- Containerization: Docker & Docker Compose

### Cowrie Honeypot Setup

[Configuration details will go here]

## Attack Analysis

[Your findings from attack data - we'll fill this in once you have more data and Grafana screenshots]

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
