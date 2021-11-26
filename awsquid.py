import sys
import csv
import boto3
from typing import Dict, List


def main() -> None:
    """Entrypoint of program run as module."""
    args: Dict[str, str] = read_args()
    print(args)

def aws_arg():
    """AWS options"""
    print("AWS features: EC2 and ELB inventories")

def azure_arg():
    """"Azure options"""
    print("Azure fetures: TBD")

def gcp_arg():
    """GCP options"""
    print("GCP features: TBD")

def oci_arg():
    """OCI options"""
    print("OCI features: TBD")

def usage():
    """Usage options"""
    print("Usage example:  python3 awsquid.py [MSP]")
    print("Usage example:  python3 awsquid.py AWS")
    print("MSP Options: AWS AZURE GCP OCI")

def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments"""
    if len(sys.argv) != 2:
        print(usage())
        exit()
    elif sys.argv[1] == "AWS":
        print(aws_arg())
        exit()
    elif sys.argv[1] == "AZURE":
        print(azure_arg())
        exit()
    elif sys.argv[1] == "GCP":
        print(gcp_arg())
        exit()
    elif sys.argv[1] == "OCI":
        print(oci_arg())
        exit()
    else:
        print(usage())
    return {
        "keyword": sys.argv[1],
    }

if __name__ == '__main__':
    main()