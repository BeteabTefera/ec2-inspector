# EC2 Inspector

**EC2 Inspector** is a lightweight Python application that helps AWS users monitor and audit their EC2 instances. The tool provides a quick overview of your instances, including instance type, status, private and public IPs, attached EBS storage, and security groups.

---

## Features

- List all EC2 instances in your AWS account
- Display:
  - Instance ID
  - Instance Type
  - State (running, stopped, etc.)
  - Private and Public IP addresses
  - Associated Security Groups
  - Total EBS volume size attached
- Easy-to-read table output in terminal

---

## Requirements

- Python 3.7+
- `boto3` Python library
- `tabulate` Python library
- AWS CLI configured with credentials (`aws configure`)

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/ec2-inspector.git
cd ec2-inspector
