import boto3

PREFIX = 'path/to/folder'
BUCKET = 'BucketName'

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
for obj_sum in bucket.objects.filter(Prefix=PREFIX):
    obj = s3.Object(obj_sum.bucket_name, obj_sum.key)
    restore_requestDict = {
        'Days': 30, # Number of days object is kept in S3 before it is removed
        'GlacierJobParameters': {
        'Tier': 'Standard' # can also be 'Expedited' or 'Standard' see Glacier restore options for explanation
        },}
    if obj.storage_class == 'GLACIER':
        # Try to restore the object if the storage class is glacier and
        # the object does not have a completed or ongoing restoration
        # request.
     
        if obj.restore is None:
            print('Submitting restoration request: %s' % obj.key)
            response = obj.restore_object(RestoreRequest=restore_requestDict)
        #Print out objects whose restoration is on-going
        elif 'ongoing-request="true"' in obj.restore:
            print('Restoration in-progress: %s' % obj.key)
        # Print out objects whose restoration is complete
        elif 'ongoing-request="false"' in obj.restore:
            print('Restoration complete: %s' % obj.key)