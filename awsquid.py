import boto3
import csv
import sys
from typing import Dict, List

tenants = ['TENANT1', 'TENANT2']

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
    if sys.argv[2] in tenants:
        if len(sys.argv) == 3:
            print("\n Task missing, pls reference usage:")
            print(usage_help_arg())
            exit()
        if sys.argv[3] == "EC2":
            print(aws_ec2())
            exit()
        if sys.argv[3] == "ELB":
            print(aws_elb())
            exit()
        elif ((sys.argv[3] != "EC2") and (sys.argv[3] != "ELB")):
            print("\n Invalid task, pls reference usage:")
            print(usage_help_arg())
            exit()

    elif sys.argv[2] not in tenants:
        print("\n Invalid Tenant ID, pls reference usage:")
        print(usage_help_arg())
        exit()

def aws_ec2():
    each_prof = sys.argv[2]
    print('')
    print('== Profile -',each_prof,'-- EC2 instances == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    ins_file=open('output/' + each_prof + '-ec2_invent.csv','w',newline='')
    ins_data=csv.writer(ins_file)
    ins_data.writerow(['Name','Instance','IP','MacAddress','Environment','Platform','OS','RunAfterHours','InstanceType'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.resource('ec2')
        print("Auditing region",each_reg)
        for each_in in resource.instances.all():
            mac = ""
            for iface in each_in.network_interfaces:
                mac = iface.mac_address
            ins_name = ""
            run_af_hrs = ""
            env = ""
            for tags in each_in.tags:
                if tags["Key"] == 'Name':
                    ins_name = tags["Value"]
                if tags["Key"] == 'RunAfterHours':
                    run_af_hrs = tags["Value"]
                if tags["Key"] == 'Environment':
                    env = tags["Value"]        
            ins_data.writerow([ins_name,each_in.id,each_in.public_ip_address or each_in.private_ip_address,mac,env or "NotDefined",each_in.platform or 'Linux',"NotDefined",run_af_hrs or 'Yes',each_in.instance_type])
            print(' --> Region ' + each_reg + '\'s AWS EC2 inventory file: output/' + each_prof + '-ec2_invent.csv')
    ins_file.close()
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
    print("\n Usage: python3 awsquid.py MSP TENANT TASK")
    print(" Example: python3 awsquid.py AWS CID# EC2")
    print(" Example: python3 awsquid.py AWS CID# ELB")
    print(" Example: python3 awsquid.py OCI CID# HELP")
    print(" Example: python3 awsquid.py GCP CID# HELP")
    print(" Example: python3 awsquid.py AZURE CID# HELP\n")

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