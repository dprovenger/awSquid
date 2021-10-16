import boto3

# List of aws profiles
aws_prof=['jarrieta-awscli']

# Multiple profiles:
# aws_prof=['default', 'default', 'profileid']

# List of Regions and EC2 instances with in each region
for each_prof in aws_prof:
    print('')
    print('== Profile -',each_prof,'-- EC2 instances == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.resource('ec2')
        print("Region:",each_reg)
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
            #print("      -",each_reg,"-- Instance ID:",each_in.id,"-- Instance State:",each_in.state['Name'])
            print(ins_name,each_in.id,each_in.public_ip_address,mac,env or "NotDefined",each_in.platform or 'Linux',"NotDefined",run_af_hrs or 'Yes',each_in.instance_type)


# List of Regions and Classic ELBs with in each region
for each_prof in aws_prof:
    print('')
    print('== Profile -',each_prof,'-- Classic ELBs == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.client('elb')
        print("Region -",each_reg)
        for each in resource.describe_load_balancers()['LoadBalancerDescriptions']:
            #for each_in in each['LoadBalancerName']:
            #print(each)
            print("       -",each_reg,"-- Classic ELB Name:",each['LoadBalancerName'])
                #print('each_in.LoadBalancerName', 'each_in.DNSName')

# List of Regions and App/Net ELBs with in each region
for each_prof in aws_prof:
    print('')
    print('== Profile -',each_prof,'-- App/Net ELBs == ')
    session=boto3.Session(profile_name=each_prof,region_name='us-east-2')
    client=session.client('ec2')
    all_regions=client.describe_regions()
    list_of_regions=[]
    for each_reg in all_regions['Regions']:
        list_of_regions.append(each_reg['RegionName'])
    for each_reg in list_of_regions:
        session=boto3.Session(profile_name=each_prof,region_name=each_reg)
        resource=session.client('elbv2')
        print("Region -",each_reg)
        for each in resource.describe_load_balancers()['LoadBalancers']:
            print("       -",each_reg,"-- ELB Name:",each['LoadBalancerName'],"-- ELB Type:",each['Type'])

