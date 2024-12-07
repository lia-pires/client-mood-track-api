from flask import Flask
from flask import request

app = Flask(__name__)

@app.post("/comment-analysis")
def analyze_comment():
    return f''


@app.get("/comments")
def get_all_comments():
    return f''


@app.route("comments/{id}", methods=['GET', 'DELETE', 'PUT'])
def comments():
    if request.method == 'POST':
        pass
    if request.method == 'DELETE':
        pass
    if request.method == 'PUT':
        pass


# POST /comment-analysis - Classifies a single comment using ChatGPT 
# GET /comments Retrieves all classified comments.
# GET /comments/{id} Retrieves a single classified comment by its ID.
# DELETE /comments/{id}  Deletes a classified comment by its ID.
# PUT /comments/{id} Updates a previously classified comment by its ID.


