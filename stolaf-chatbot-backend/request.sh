curl -H 'Content-Type: application/json' \
      -d '{ "prompt": "How do I fix the disk quota issue?"}' \
      -X POST \
      http://localhost:8000/predict
