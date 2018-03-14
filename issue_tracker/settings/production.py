from .base import *


DEBUG = False


INSTALLED_APPS += [
    'storages',
]

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = 'issue-tracker-1'

AWS_S3_REGION_NAME = 'eu-west-2'

AWS_S3_HOST = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

AWS_S3_SIGNATURE_VERSION = 's3v4'

DEFAULT_FILE_STORAGE = 'issue_tracker.aws.MediaRootS3Boto3Storage'

STATICFILES_STORAGE = 'issue_tracker.aws.StaticRootS3Boto3Storage'

MEDIA_URL = f'https://{AWS_S3_HOST}/media/'

STATIC_URL = f'https://{AWS_S3_HOST}/static/'
