import boto3
from tabulate import tabulate

# Create EC2 client
ec2 = boto3.client('ec2')

def list_instances():
    response = ec2.describe_instances()
    instances = []

    for reservation in response['Reservations']:
        for inst in reservation['Instances']:
            instance_id = inst['InstanceId']
            instance_type = inst['InstanceType']
            state = inst['State']['Name']
            private_ip = inst.get('PrivateIpAddress', 'N/A')
            public_ip = inst.get('PublicIpAddress', 'N/A')
            security_groups = [sg['GroupName'] for sg in inst.get('SecurityGroups', [])]

            # Get attached volumes
            volumes = ec2.describe_volumes(Filters=[{'Name':'attachment.instance-id','Values':[instance_id]}])
            total_storage = sum(v['Size'] for v in volumes['Volumes'])

            instances.append([
                instance_id,
                instance_type,
                state,
                private_ip,
                public_ip,
                ', '.join(security_groups),
                f"{total_storage} GB"
            ])
    
    headers = ["Instance ID", "Type", "State", "Private IP", "Public IP", "Security Groups", "EBS Size"]
    print(tabulate(instances, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    list_instances()
