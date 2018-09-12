# GlacierBulkRestore
Restore objects stored in S3 under the Glacier storage class based on 'directories' and 'subdirectories'

# Requirements:
Python - 
  Windows: https://www.python.org/downloads/windows/
  Mac:https://www.python.org/downloads/mac-osx/
  
Boto3 - 
  pip install boto3
  
AWSCLI - 
  pip install awscli

# Steps:

1. Edit GlacierRestore.py with your bucket name under BUCKET and directory path needed under PREFIX
2. Run GlacierRestore.py with “python GlacierRestore.py”
*This is using the "Standard" Glacier restore which will take 3-5 hours*
3. Navigate to the local folder that you will restore S3 Objects to
4. Execute $ aws s3 cp --recursive --force-glacier-transfer s3://BUCKETNAME/PATH/TO/FOLDER/ ./
*This will download all objects in the above path to your current directory. Folders and subfolder structure will remain intact.*
