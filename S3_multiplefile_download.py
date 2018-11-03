# Download multiple buckets and files in each bucket
import boto3
import os

s3 = boto3.resource('s3')
os.chdir('C:\\Users\\Chiranjeevi\\Desktop')  # change directory to
for bucket in s3.buckets.all():
    for object in bucket.objects.all():
        if not os.path.exists(bucket.name):
            os.mkdir(bucket.name)
            os.chdir(bucket.name)
            if os.path.isfile(object.key):
                print(bucket.name, '-->', object.key, "avaialble")
            else:
                s3.Bucket(bucket.name).download_file(object.key, object.key)
                print(object.key, '-->', bucket.name)
                os.chdir('C:\\Users\\Chiranjeevi\\Desktop')
        else:
            os.chdir(bucket.name)
            if os.path.isfile(object.key):
                print(bucket.name, '-->', object.key, "avaialble")
                os.chdir('C:\\Users\\Chiranjeevi\\Desktop')
            else:
                s3.Bucket(bucket.name).download_file(object.key, object.key)
                print(object.key, '-->', bucket.name)
                os.chdir('C:\\Users\\Chiranjeevi\\Desktop')

print("Finished")
