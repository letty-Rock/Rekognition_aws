import boto3
import json

client=boto3.client('rekognition')
s3 = boto3.resource('s3')

def detecta_faces():
    faces_detectadas=client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': 'letimagens',
                'Name': '_analise.jpg',
           },
        },
    )

    return faces_detectadas

def cria_lista_faceId_detectadas(faces_detectadas):
    faceId_detectadas = []
    for imagens in range(len(faces_detectadas['FaceRecords'])):
        faceId_detectadas.append(faces_detectadas['FaceRecords'][imagens]['Face']['FaceId'])
    return faceId_detectadas

def compara_imagens(faceId_detectadas):
    resultado_comparacao = []
    for ids in faceId_detectadas:
        resultado_comparacao.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=ids,
                FaceMatchThreshold=80,
                MaxFaces=10,
            )
        )
    return resultado_comparacao

faces_detectadas = detecta_faces()
faceId_detectadas = cria_lista_faceId_detectadas(faces_detectadas)
resultado_comparacao = compara_imagens(faceId_detectadas)
print(json.dumps(resultado_comparacao, indent=4))
