import boto3


client = boto3.client('rekognition')
s3 = boto3.resource('s3')

def detecta_faces():
        faces_detectadas = client.index_faces(
            CollectionId='faces',
            DetectionAttributes=['DEFAULT'],
            ExternalImageId='TEMPORARIA',
            Image={
                'S3Object': {
                    'Bucket': 'letimagens',
                    'Name': '_analise.png',
                },

            },
        )