# Download single bucket and files with same structure
import sys

directory_path = sys.argv[1]
bucket_name = sys.argv[2]


def s3_single(directory_path, bucket_name):
    import boto3
    import os
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    # When you run the code from terminal it will download the buckets in terminal current directory
    # for that below code will change the directory path to specified path
    os.chdir(directory_path)
    # below code fetch specified bucket objects
    for obje in bucket.objects.all():
        if os.path.exists(bucket.name):
            print(bucket.name)
            os.chdir(bucket.name)
            if os.path.isfile(obje.key):
                print(bucket.name, '-->', obje.key, "avaialble")
            else:
                s3.Bucket(bucket.name).download_file(obje.key, obje.key)
                print(obje.key, '-->', bucket.name)
                os.chdir(bucket.name)
        else:
            # It will check whether the bucket is available or not if not available it will create the bucket with
            # same name in s3 and change directory to bucket directory
            os.mkdir(bucket.name)
            os.chdir(bucket.name)
            if os.path.isfile(obje.key):
                print(bucket.name, '-->', obje.key, "avaialble")
            else:
                s3.Bucket(bucket.name).download_file(obje.key, obje.key)
                print(obje.key, '-->', bucket.name)

    return "Finished"


# It will call the function
s3_single(directory_path, bucket_name)
