#!/bin/bash

function install_flat_plugin {
    echo "Installing Flat Plugin"
    setup_develop $DEST/flat_horizon_plugin
}

if is_service_enabled flat_plugin; then
    case $1 in
        install)
            install_flat_plugin
            ;;
    esac
fi
