#!/usr/bin/env bash
# shellcheck disable=SC2155,SC2086

export DEFAULT_COLLECTIONS_PATH="$ANSIBLE_COLLECTIONS_PATH/ansible_collections"

# Check if the variable is already set (e.g., in CI)
if [ -z "$ANSIBLE_COLLECTIONS_PATH" ]; then
    # If not, use base collections path
    ANSIBLE_COLLECTIONS_PATH="$DEFAULT_COLLECTIONS_PATH"
fi

echo "ANSIBLE_COLLECTIONS_PATH: $ANSIBLE_COLLECTIONS_PATH"
BASE_DIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
export ANSIBLE_ROLES_PATH=${BASE_DIR}

# Authentication vars
export VMWARE_HOST=$(awk '/vcenter_hostname/ {print $2}' ../../integration_config.yml)
export VMWARE_USER=$(awk '/vcenter_username/ {print $2}' ../../integration_config.yml)
export VMWARE_PASSWORD=$(awk '/vcenter_password/ {print $2}' ../../integration_config.yml)
export VMWARE_VALIDATE_CERTS=$(awk '/vcenter_validate_certs/ {print $2}' ../../integration_config.yml)