from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import os

app = Flask(__name__)

MODEL_NAME = "mixedbread-ai/mxbai-embed-large-v1"
MODEL_DIR = "model"
DIMENSIONS = 512

# Load the model
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

model_path = os.path.join(MODEL_DIR, MODEL_NAME.split('/')[-1])

if not os.path.exists(model_path):
    model = SentenceTransformer(MODEL_NAME, truncate_dim=DIMENSIONS)
    model.save(model_path)
else:
    model = SentenceTransformer(model_path, truncate_dim=DIMENSIONS)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    docs = data.get("docs", [])

    if len(docs) > 0:
        embeddings = model.encode(docs)

        similarities = cos_sim(embeddings[0], embeddings[1:])
        similarities_list = similarities.tolist()

        return jsonify({"similarities": similarities_list})
    else:
        return jsonify({"error": "Query and documents must be provided"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)