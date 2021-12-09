import boto3
import csv
import sys
import datetime
from typing import Dict, List

# Global Variables To Configure:
tenants = ['TENANT1', 'TENANT2', 'jarrieta-awscli']
default_region = 'us-east-2'

# Default Global Variables:
time_now = datetime.datetime.now().strftime('_%Y_%m_%d')
# Global Variables End:


def main() -> None:
    """Entrypoint of program."""
    args: Dict[str, str] = read_args()

# AWS Section Begins:
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
        if sys.argv[3] == "RDS":
            print(aws_rds())
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
    print('\n' + each_prof + '\'s EC2 Instances Inventory: \n')
    session=boto3.Session(profile_name=each_prof,region_name=default_region)
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    ins_file=open('output/' + each_prof + '-ec2_invent' + time_now + '.csv','w',newline='')
    ins_data=csv.writer(ins_file)
    ins_data.writerow(['Name','Instance','IP','MacAddress','Environment','Platform','OS','RunAfterHours','InstanceType'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.resource('ec2')
        print("Auditing region",each_reg)
        ec2s_found = 0
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
            ec2s_found += 1
        if ec2s_found > 0:
            print(' --> Region ' + each_reg + '\'s AWS EC2 inventory file: output/' + each_prof + '-ec2_invent' + time_now + '.csv\n')
        else:
            print(' --> No EC2s found in ' + each_reg)
    ins_file.close()
    exit()

def aws_elb():
    each_prof = sys.argv[2]
    print('\n' + each_prof + '\'s Classic ELBs Inventory: \n')
    session=boto3.Session(profile_name=each_prof,region_name=default_region)
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
        ins_file=open('output/' + each_prof + '-classic_elb_inventory' + time_now + '.csv','w',newline='')
        ins_data=csv.writer(ins_file)
        ins_data.writerow(['ELB Name','ELB Type','ELB Created Date'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.client('elb')
        print("Auditing region",each_reg)
        celbs_found = 0
        for each in resource.describe_load_balancers()['LoadBalancerDescriptions']:
            ins_data.writerow([each['LoadBalancerName'],"classic",each['CreatedTime']])
            celbs_found += 1
        if celbs_found > 0:
            print(' --> Region ' + each_reg + '\'s AWS Classic ELB inventory file: output/' + each_prof + '-classic_elb_inventory' + time_now + '.csv\n')
        else:
            print(' --> No Classic ELBs found in ' + each_reg)
    ins_file.close()

    print('')
    print('\n' + each_prof + '\'s App/Net ELBs Inventory:\n')
    session=boto3.Session(profile_name=each_prof,region_name=default_region)
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
        ins_file=open('output/' + each_prof + '-app_net_elb_inventory' + time_now + '.csv','w',newline='')
        ins_data=csv.writer(ins_file)
        ins_data.writerow(['ELB Name','ELB Type','ELB State','ELB Created Date'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.client('elbv2')
        print("Auditing region -",each_reg)
        elbs_found = 0
        for each in resource.describe_load_balancers()['LoadBalancers']:
            ins_data.writerow([each['LoadBalancerName'],each['Type'],each['State']['Code'],each['CreatedTime']])
            elbs_found += 1
        if elbs_found > 0:
            print(' --> Region ' + each_reg + '\'s AWS Application|Network ELB inventory file: output/' + each_prof + '-app_net_elb_inventory' + time_now + '.csv\n')
        else:
            print(' --> No Application|Network ELBs found in ' + each_reg)
    ins_file.close()
    exit()

def aws_rds():
    each_prof = sys.argv[2]
    print('\n' + each_prof + '\'s RDS Inventory: \n')
    session=boto3.Session(profile_name=each_prof,region_name=default_region)
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
        ins_file=open('output/' + each_prof + '-rds_inventory' + time_now + '.csv','w',newline='')
        ins_data=csv.writer(ins_file)
        ins_data.writerow(['RDS Name','RDS Engine Type','RDS Engine Version','RDS Status','RDS Instance Type','RDS Created Date'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.client('rds')
        print("Auditing region",each_reg)
        rds_found = 0
        for each in resource.describe_db_instances()['DBInstances']:
            ins_data.writerow([each['DBInstanceIdentifier'],each['Engine'],each['EngineVersion'],each['DBInstanceStatus'],each['DBInstanceClass'],each['InstanceCreateTime']])
            rds_found += 1
        if rds_found > 0:
            print(' --> Region ' + each_reg + '\'s AWS RDS inventory file: output/' + each_prof + '-rds_inventory' + time_now + '.csv\n')
        else:
            print(' --> No RDS found in ' + each_reg)
    ins_file.close()
    exit()
# AWS Section Ends:

# AZURE Section Begins:
def azure_options():
    print("\n No Azure options available at this time!\n")
    exit()
# AZURE Section Ends:

# GCP Section Begins:
def gcp_options():
    print("\n No GCP options available at this time!\n")
    exit()
# GCP Section Ends:

# OCI Section Begins:
def oci_options ():
    print("\n No OCI options available at this time!\n")
    exit()
# OCI Section Ends:

# Section of all MSPs Begins:
def usage_help_arg():
    """Usage examples and syntax"""
    print("\n Usage is case sensitive: python3 awsquid.py MSP TENANT TASK")
    print(" Example: python3 awsquid.py AWS CID# EC2")
    print(" Example: python3 awsquid.py AWS CID# ELB")
    print(" Example: python3 awsquid.py AWS CID# RDS")
    print(" Example: python3 awsquid.py OCI CID# HELP")
    print(" Example: python3 awsquid.py GCP CID# HELP")
    print(" Example: python3 awsquid.py AZURE CID# HELP\n")
# Section for all MSPs Ends:

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