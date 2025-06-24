#!/bin/bash

set -e

# 1. Install Puppet if not already installed
if ! command -v puppet >/dev/null 2>&1; then
    echo "Installing Puppet..."
    sudo apt update
    sudo apt install -y puppet
else
    echo "Puppet is already installed."
fi

# 2. Enable and start Puppet agent service
echo "Enabling and starting Puppet agent service..."
sudo systemctl enable puppet
sudo systemctl start puppet

# 3. Copy hello_cloud.service to systemd if it exists
if [ -f hello_cloud.service ]; then
    echo "Copying hello_cloud.service to /etc/systemd/system/"
    sudo cp hello_cloud.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable hello_cloud.service
    sudo systemctl start hello_cloud.service
else
    echo "hello_cloud.service not found in current directory."
fi

echo "Setup complete."