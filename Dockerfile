# Use the official slim Python 3.13 image as base
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /ip_subnet_package

COPY ip_analyzer_requirements.txt .
COPY subnet_analyzer.py .
COPY ip_data.xlsx .

# Install Python dependencies without using cache to keep the image small
RUN pip install --no-cache-dir -r ip_analyzer_requirements.txt

# Set the default command to run the Python script when the container starts
CMD [ "python" , "subnet_analyzer.py" ]
