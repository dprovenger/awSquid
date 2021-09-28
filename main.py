import boto3

# List of aws profiles
aws_prof=['default', 'jarrieta-awscli']
# Multiple profiles:
# aws_prof=['default', 'default']


# List of Regions and EC2 instances with in each region
for each_prof in aws_prof:
    print('')
    print('== ',each_prof,' profile and EC2 instances == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    for each_reg in list_of_regions:
        session=boto3.Session(region_name=each_reg)
        resource=session.resource('ec2')
        print(each_reg," -- EC2s:")
        for each_in in resource.instances.all():
            print("-->  ",each_reg," -- ",each_in.id,each_in.state['Name'])

# List of Regions and Classic ELBs with in each region
for each_prof in aws_prof:
    print('')
    print('== ',each_prof,' profile and Classic Load Balancers == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    for each_reg in list_of_regions:
        session=boto3.Session(region_name=each_reg)
        resource=session.client('elb')
        print(each_reg," -- Classic ELBs:")
        for each in resource.describe_load_balancers()['LoadBalancerDescriptions']:
            #for each_in in each['LoadBalancerName']:
            #print(each)
            print("-->  ",each_reg," -- ",each['LoadBalancerName'])
                #print('each_in.LoadBalancerName', 'each_in.DNSName')

# List of Regions and App/Net ELBs with in each region
for each_prof in aws_prof:
    print('')
    print('== ',each_prof,' profile and App/Net Load Balancers == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    for each_reg in list_of_regions:
        session=boto3.Session(region_name=each_reg)
        resource=session.client('elbv2')
        print(each_reg," -- APP/NET ELBs:")
        for each in resource.describe_load_balancers()['LoadBalancers']:
            print("-->  ",each_reg," -- ",each['LoadBalancerName']," -- ",each['Type'])