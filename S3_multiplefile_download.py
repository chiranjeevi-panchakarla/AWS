# Download multiple buckets and files in each bucket with same structure
import boto3
import os

s3 = boto3.resource('s3')

# When you run the code from terminal it will download the buckets in terminal current directory
# for that below code will change the directory path to specified path
os.chdir('C:\\Users\\Chiranjeevi\\Desktop')

# below code fetch all buckets from s3
for bucket in s3.buckets.all():
    for object in bucket.objects.all():
        # It will check whether the bucket is available or not if not available it will create the bucket with
        # same name in s3 and change directory to bucket directory
        if not os.path.exists(bucket.name):
            os.mkdir(bucket.name)
            os.chdir(bucket.name)
            # It will compare with s3 bucket files and check whether file is avaiable in local bucket
            # if not available it will download the file and change the directory to specified directory
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
