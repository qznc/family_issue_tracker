#!/bin/bash
set -euo pipefail
# This script is run in the VM once when you first run `vagrant-spk up`.  It is
# useful for installing system-global dependencies.  It is run exactly once
# over the lifetime of the VM.

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y python3 python3-pip python-virtualenv

exit 0
