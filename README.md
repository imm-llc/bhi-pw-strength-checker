# bhi-pw-strength-checker

## Overview

This is a webapp to check passwords against HIBP and common password best-practices.


## Usage

Clone the repo

Move `config.example.py` to `config.py`. Provide a value for `SECRET_KEY`.

Run the Flask app using the Docker container. Forward 5000 -> 5000

Run NGINX as a reverse proxy (check `service/` for config examples). Offload TLS there