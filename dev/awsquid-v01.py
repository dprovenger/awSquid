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

def aws_tenants():
    return "C101"
    

def aws_ec2_arg():
    """AWS EC2 Inventory"""
    print("AWS EC2 Inventory ...")

def aws_elb_arg():
    """AWS ELB Inventory"""
    print("AWS ELB Inventory ...")

def aws_help_arg():
    """AWS Available Options"""
    print("\nAWS Additional Options: Inventory for EC2 instances or ELB loadbalancers")
    print("SAMPLE USAGE: python3 awsquid.py AWS EC2 TENANT")
    print("SAMPLE USAGE: python3 awsquid.py AWS ELB TENANT\n")

def aws_tenant_arg():
    """AWS EC2"""

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
    print("\nUsage example:  python3 awsquid.py [MSP] [TASK]")
    print("Syntax example:  python3 awsquid.py AWS HELP")
    print("MSP Options: AWS AZURE GCP OCI")
    print("TASK Options: HELP EC2 ELB\n")

def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments"""
    if len(sys.argv) != 4:
        print(usage())
        exit()
    elif sys.argv[1] == "AWS":
        if sys.argv[2] == "EC2":
            if sys.argv[3] in aws_tenants():
                print("TENNANTS")
            print(aws_ec2_arg())
            exit()
        elif sys.argv[2] == "ELB":
            print(aws_elb_arg())
            exit()
        print(aws_help_arg())
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