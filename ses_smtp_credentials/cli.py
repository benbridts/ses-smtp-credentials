#!/usr/bin/env python3
import argparse
from getpass import getpass

from constants import SMTP_REGIONS
from lib import calculate_key


def run():
    parser = argparse.ArgumentParser(description="Convert a Secret Access Key for an IAM user to an SMTP password.")
    parser.add_argument("--secret", help="The Secret Access Key to convert.")
    parser.add_argument(
        "--region",
        help="The AWS Region where the SMTP password will be used.",
        choices=SMTP_REGIONS,
    )
    args = parser.parse_args()

    region = args.region if args.region else input("region: ").strip()
    secret = args.secret if args.secret else getpass("secret: ").strip()
    print(calculate_key(secret, region))


if __name__ == "__main__":
    run()
