import os
import uuid
from hashlib import md5

import boto3

from .const import S3_BUCKET, S3_BUCKET_REGION
from .logger import setup_logging

logger = setup_logging()


def upload_file_to_s3(filename):
    pass
