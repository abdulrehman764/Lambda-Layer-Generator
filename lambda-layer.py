import subprocess
import shutil
import boto3
import json
import os
import re

def get_python_version():
    try:
        result = subprocess.check_output(['python', '--version'], stderr=subprocess.STDOUT)
        output = result.decode('utf-8')
        print("Output:", output)
        match = re.search(r'Python (\d+\.\d+)', output)
        if match:
            version = match.group(1)
            print("Version:", version)
            return version
        else:
            print("Version not found in the output.")
            return None
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

def install_package(package_name, version, target_dir):
    try:
        if version:
            subprocess.call(['pip3', 'install', f'{package_name}=={version}', '-t', target_dir, '--no-cache-dir'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.call(['pip3', 'install', f'{package_name}', '-t', target_dir, '--no-cache-dir'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as exception:
        print('Oops, Exception: ', exception)

def create_zip_archive(source_dir, archive_name):
    shutil.make_archive(archive_name, 'zip', source_dir)

def upload_to_s3(zip_file, s3_bucket, s3_key):
    S3 = boto3.resource('s3')
    try:
        S3.meta.client.upload_file(zip_file, s3_bucket, s3_key)
    except Exception as exception:
        print('Oops, Exception: ', exception)

def lambda_handler(event, context):
    pip_package = "openai"
    package_version = "" #optional
    s3_bucket = "abdullambdalayers"
    
    python_version = get_python_version()
    if not python_version:
        return {'statusCode': 500, 'body': 'Error'}

    tmp_dir = f"/tmp/python/python/lib/python{python_version}/site-packages/"
    os.makedirs(tmp_dir)

    install_package(pip_package, package_version, tmp_dir)
    create_zip_archive("/tmp/python", "/tmp/python")
    
    if package_version:
        s3_key = f'{pip_package}/{package_version}/python.zip'
    else:
        s3_key = f'{pip_package}/python.zip'
        
    upload_to_s3('/tmp/python.zip', s3_bucket, s3_key)

    return {'statusCode': 200, 'body': json.dumps('Success!')}
