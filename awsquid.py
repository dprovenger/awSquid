import sys
from typing import Dict, List

def main() -> None:
    """Entrypoint of program."""
    args: Dict[str, str] = read_args()

# AWS Section 
def aws_options():
    """AWS options of tasks (EC2 and ELB)"""
    if len(sys.argv) == 2:
        print("\n Tenant ID missing, pls reference usage:")
        print(usage_help_arg())
        exit()
    if sys.argv[2] in ["TENANT1","TENANT2"]:
        if len(sys.argv) == 3:
            print("\n Task missing, pls reference usage:")
            print(usage_help_arg())
            exit()
        if sys.argv[3] == "EC2":
            print(aws_ec2())
        if sys.argv[3] == "ELB":
            print(aws_elb())
        elif ((sys.argv[3] != "EC2") and (sys.argv[3] != "ELB")):
            print("\n Invalid task, pls reference usage:")
            print(usage_help_arg())
            exit()

    elif sys.argv[2] not in ["TENANT1","TENANT2"]:
        print("\n Invalid Tenant ID, pls reference usage:")
        print(usage_help_arg())
        exit()

def aws_ec2():
    print("Welcome to AWS EC2 Section")
    exit()

def aws_elb():
    print("Welcome to AWS ELB section")
    exit()

# AZURE Section:
def azure_options():
    print("\n Azure options currently not available\n")
    exit()

# GCP Section:
def gcp_options():
    print("\n GCP options currently not available\n")
    exit()

# OCI Section:
def oci_options ():
    print("\n OCI options currently not available\n")
    exit()

# Section of all MSPs
def usage_help_arg():
    """Usage examples and syntax"""
    print("\n Usage: python3 awsquid MSP TENANT TASK")
    print(" Example: python3 awsquid AWS CID# EC2")
    print(" Example: python3 awsquid AWS CID# ELB")
    print(" Example: python3 awsquid OCI CID# HELP")
    print(" Example: python3 awsquid GCP CID# HELP")
    print(" Example: python3 awsquid AZURE CID# HELP\n")

def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments"""
    if len(sys.argv) <= 1:
        print("\n Arguments missing, pls referene usage:")
        print(usage_help_arg())
        exit()
    elif len(sys.argv) >= 5:
        print("\n Too many arguments, pls reference usage:")
        print(usage_help_arg())
        exit()
    elif (sys.argv[1] == "AWS"):
        print(aws_options())
        exit()
    elif sys.argv[1] == "AZURE":
        print(azure_options())
        exit()
    elif sys.argv[1] == "GCP":
        print(gcp_options())
        exit()
    elif sys.argv[1] == "OCI":
        print(oci_options())
        exit()
    else:
        print("\n Invalid MSP, pls referene usage:")
        print(usage_help_arg())

if __name__ == '__main__':
    main()