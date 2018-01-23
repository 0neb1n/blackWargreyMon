#!/usr/bin/env bash

set -e

docker run -d --name slack_command -p 1337:1337 slack_command
