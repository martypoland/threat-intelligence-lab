## Attack Analysis

### Summary Statistics (As of [DATE])

- **Total Attack Events:** 18,974
- **Unique Source IPs:** 129 different attackers
- **Malware Samples Captured:** 11 unique files
- **Attack Duration:** [X days] of continuous monitoring

### Attack Patterns

**Most Targeted Usernames:**
| Username | Attempts |
|----------|----------|
| root | 955 |
| 345gs5662d34 | 448 |
| admin | 104 |
| user | 54 |
| ubuntu | 51 |
| oracle | 44 |
| mysql | 38 |

The predominance of 'root' attempts (50% of all username attempts) demonstrates attackers prioritizing administrative access. The unusual username '345gs5662d34' suggests automated botnet scanning with specific target profiles.

**Most Common Passwords:**
| Password | Attempts |
|----------|----------|
| 3245gs5662d34 | 451 |
| 345gs5662d34 | 449 |
| 123456 | 89 |
| 1234 | 80 |
| 123 | 55 |
| admin123 | 37 |
| 1q2w3e4r | 33 |

Analysis reveals coordinated botnet activity using paired username/password combinations ('345gs5662d34'/'3245gs5662d34') accounting for nearly 900 attempts, alongside traditional weak credentials like '123456' and sequential number patterns.

### Key Findings

- **Botnet Activity:** Significant coordinated scanning from distributed sources using identical credential pairs
- **IoT Targeting:** Attempts against service accounts (mysql, oracle, ftpuser) indicate targeting of poorly secured IoT devices and embedded systems
- **Persistence Mechanisms:** Attackers attempted SSH key backdoor installation (captured public key: `mdrfckr`)
- **Geographic Distribution:** Attacks originated from 129 unique IP addresses across multiple countries

### Attack Techniques Observed

1. **Credential Stuffing:** Systematic brute-force using common username/password combinations
2. **Backdoor Installation:** SSH authorized_keys manipulation for persistent access
3. **Malware Deployment:** Automated scripts attempting binary downloads and execution
