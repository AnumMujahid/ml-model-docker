1. The models are on hugging face so currently we do not need to store them on s3, we will directly pull the models from hugging face. (see app.py)

2. Then we will create and test the docker image using dockerfile and host it on AWS ECR.

```
docker build -t mxbai-embed .
```

3. The image will contain the requirements, logic for downloading and loading models and making predictions. We can host this application using this image on AWS Lambda, AWS EC2 etc using this docker image.

4. To run app.py locally follow these steps:

- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- flask run

Note:

- Consider the constraints of AWS Lambda before hosting models there like storage.
- To host models on EC2 GPU instance you will need to do some GPU setup.
- You can reduce the size of docker image if possible.
- You can optimize the models if possible.
