import boto3

# First Credentials - Access Key & Secret Access Key

s3 = boto3.resource('s3')

print('Connection Successfully')
print("Existing Buckets:")
for bucket in s3['Buckets']:
    print(f"  {bucket['Name']}")