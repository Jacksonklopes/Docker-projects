# Day 34 – Docker Compose: Flask + PostgreSQL + Redis

**Step 0: Create an EC2 instance**

- OS: Ubuntu (22.04 or 24.04 LTS)
- Size: 1 vCPU and 2 GB RAM or more (suggested)
- Disk: 10 GB or more (suggested, Docker images use space)
- Security group: allow SSH (port 22) and TCP port 5000
- Connect with SSH, then run the commands below

```bash
# Install Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Find the Compose package name (look for "tool for running multi-container applications on Docker")
apt search docker compose

# Install the Compose plugin (package name found above)
sudo apt-get install -y docker-compose-v2

# Run Docker without sudo
sudo usermod -aG docker $USER
newgrp docker

# Download the project
git clone https://github.com/Jacksonklopes/Docker-projects.git

# Go to the folder where docker-compose.yml is
cd Docker-projects/day-34-compose

# Start the app (web + db + redis) in the background
docker compose up -d

# Check that all services are running
docker compose ps

# Test the app
curl http://localhost:5000

# Stop and remove the containers (data is kept)
docker compose down
```

To open the app in a browser, allow inbound TCP port 5000 in the EC2 security group, then visit `http://<EC2-public-IP>:5000`.
