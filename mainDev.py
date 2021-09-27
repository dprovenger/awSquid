import boto3
import pprint

# Adding profile sessions:
"""
# Using specific profile and region
session=boto3.Session(profile_name="nameOfProfile",region_name="nameOfRegion")

# Using single default profile
session=boto3.Session()
"""
# Using specific region:
session=boto3.Session(region_name='us-east-2')

# Using client session:
client=session.client('ec2')

# Lists all regions' names and endpoints
all_regions=client.describe_regions()

# Listing as list of key Region:
#pprint.pprint(all_regions['Regions'])
all_regions=client.describe_regions()

list_of_regions=[]
for each_reg in all_regions['Regions']:
    list_of_regions.append(each_reg['RegionName'])

print(list_of_regions)
# Prints list of regionNames:
#    print(each_reg['RegionName']

# Customizing sessions:
"""
ec2_re=session.resource(service_name="ec2")
ec2_cli=session.client(service_name="ec2")
"""

#Listing each instance within session, via resources:
"""
for each_in in ec2_re.instances.all():
# Lists each instance id only
#     print(each_in)
# Lists each instance id and state
#    print(each_in.id, each_in.state)
# Lists each instance id and state's key value
    print(each_in.id, each_in.state['Name'])
"""

# Listing each instance within session, via client:
"""
print('===')
for each in ec2_cli.describe_instances()['Reservations']:
    for each_in in each['Instances']:
        print(each_in['InstanceId'], each_in['State']['Name'])
"""

# EC2 Section
"""
ec2 = boto3.client('ec2')
ec2Response = ec2.describe_instances()
test = ec2.describe_instance_status()
print(ec2Response)
print('=====')
print(test)
"""

# LB Section
"""
elb = boto3.client('elb')
elbv2 = boto3.client('elbv2')
elbResponse = elb.describe_load_balancers()
elbv2Response = elbv2.describe_load_balancers()

print('Classic LBs')
print(elbResponse)
print('=====')
print('App/Net LBs')
print(elbv2Response)
print('=====')
"""