from django.utils.deconstruct import deconstructible
from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage


@deconstructible
class MinioStorage(S3Boto3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        params = parameters.copy() if parameters else {}

        local_endpoint = settings.MINIO_ENDPOINT.replace('minio', 'localhost')
        session = self._create_session()
        s3 = session.resource(
                's3',
                region_name=self.region_name,
                use_ssl=self.use_ssl,
                endpoint_url=local_endpoint,
                config=self.config,
                verify=self.verify,
            )
        bucket = s3.Bucket(self.bucket_name)
        key = self._normalize_name(self._clean_name(name))

        params['Bucket'] = self.bucket_name
        params['Key'] = key

        return bucket.meta.client.generate_presigned_url(
            ClientMethod='get_object',
            Params=params,
            ExpiresIn=expire,
            HttpMethod=http_method,
        )
