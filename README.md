# Subnet Analysis & Visualization Tool

A simple Python-based tool that reads IP subnet data from Excel, analyzes subnet parameters, and exports the results to CSV & JSON formats — with optional visualization using matplotlib.

---

## Features

- Read subnet data from `ip_data.xlsx` (Excel) file.
- Calculates:
  - CIDR notation
  - Network address
  - Broadcast address
  - Number of usable hosts

- Exports output to:
  - `ip_subnet_analyzer.csv`
  - `Subnet_Group_Summary.csv`

- Visualizes subnet distribution using `matplotlib`.
- Fully Dockerized for isolated and reproducible execution.

---

## How to Run

### Locally (Python Environment)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python subnet_analyzer.py


# Build the image
docker build -t subnet-analyzer .

# Run the container (replace path depending on your OS):

# PowerShell (Windows)
docker run -v "${PWD}:/app" subnet-analyzer

# CMD (Windows)
docker run -v "%cd%:/app" subnet-analyzer

# Linux/macOS
docker run -v $(pwd):/app subnet-analyzer


```
BARQ_DEVOPS_TASK/
├── Dockerfile
├── ip_analyzer_requirements.txt
├── ip_data.xlsx
├── subnet_analyzer.py
├── ip_subnet_analyzer.csv
├── Subnet_Group_Summary.csv
├── network_plot.png
├── subnet_chart.png
├── README.md
├── Report.md
```
