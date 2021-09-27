import boto3

# LB Section
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


# EC2 Section

ec2 = boto3.client('ec2')
ec2Response = ec2.describe_instances()
test = ec2.describe_instance_status()
print(ec2Response)
print('=====')
print(test)

#print(instance.name)

#for bucket in s3.buckets.all():
#    print(bucket.name)

#for instance in ec2.instance.all():
#   print(instance.name)

#s3 = boto3.resource('s3')
