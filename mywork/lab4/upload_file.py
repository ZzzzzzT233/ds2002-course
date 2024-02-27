import boto3
import requests


#create client
s3 = boto3.client("s3", region_name = "us-east-1")

bucket = "ds2002-mgv8dh"

gif_url = "https://ohiofi.com/assets/nyan.gif"
local_file = "nyan.gif"

response = requests.get(gif_url)

if response.status_code == 200:
        with open(local_file, "wb") as f:
                f.write(response.content)
else:
        print("Failed to download the file")
        exit()


with open(local_file, "rb") as file:
        file_content = file.read()


resp = s3.put_object(
        Body = file_content,
        Bucket = bucket,
        Key = local_file,
        ACL = "public-read"
)

bucket_name = "ds2002-mgv8dh"
object_name = "nyan.gif"
expires_in = 604800

response = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": object_name},
        ExpiresIn = expires_in
        )

print("Presigned URL:", response)
# presigned url 
# https://ds2002-mgv8dh.s3.amazonaws.com/nyan.gif?AWSAccessKeyId=ASIA4MTWH63YKOPYYXUO&Signature=aW9bCRiol%2Bj6a1Iiyn2Jf8nAxeo%3D&x-amz-security-token=FwoGZXIvYXdzEAEaDDWNQbdcL3WYByg78SLEAR0GNIM2r68hS9HPvFo%2Fkkf29iU1o2QuysG3N%2FbDk%2BEG%2F0f7sR7kEgdxS1%2BNnHrTZHmFFP2f4t9pFX8TMZn4ZLxwxh%2FfHf%2FVUgxdG71uHnpOhD9369vk7Y1WFKl5eZCOh9nO9aX0fyjhU2k4oaguTFC3aTd6UDeDSisNQ066PIsDB9LapwiHNx98OtEoqsCaQU8UeNCuPpfVKjPH2IE4n8fezxQyc9F34cTXg%2BDJ%2Frgaf8qv8XCXCHhYqHSiD%2FOLYmD0t6IogY34rgYyLW%2BVtJbhnx5lHz5ZwvwWTWv58e9WbOhJqyDQo1V9ctMDSUg9HO%2FbDXCrPd2Wcw%3D%3D&Expires=1709659976
