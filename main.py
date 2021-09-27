import boto3

# List of aws profiles
aws_prof=['default', 'default']

# List of Regions and EC2 instances with in each region
for each_prof in aws_prof:
    print('== ',each_prof,' Profile ==')
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

