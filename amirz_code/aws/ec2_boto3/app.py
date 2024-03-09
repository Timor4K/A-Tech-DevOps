import boto3

region = 'us-west-1'

# Create an EC2 client object
ec2 = boto3.client('ec2', region_name=region)

# Stop the EC2 instance with the given instance id
instance_id = 'i-0369ab82c15bd38bc'
ec2.stop_instances(InstanceIds=[instance_id])

# Wait until the instance is stopped
waiter = ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])

# Create an AMI from the stopped instance
image_name = 'my-ami'
response = ec2.create_image(InstanceId=instance_id, Name=image_name)

# Get the ID of the created AMI
ami_id = response['ImageId']
print(f"Created AMI with ID: {ami_id}")