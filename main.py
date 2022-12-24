from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_response = requests.get("https://mocki.io/v1/18a3f0ec-be29-49bb-bdc1-a58eb97f25ea")
blogs=blog_response.json()
post_objects = []
for post in blogs:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():

    return render_template("index.html",posts=post_objects)

@app.route("/blogs/<int:index>")
def get_post(index):
    required_post=None
    for blog_post in post_objects:
        if blog_post.id==index:
            required_post=blog_post
    return render_template("post.html",posts=required_post)


if __name__ == "__main__":
    app.run(debug=True)

for posts in post_objects:
    print(posts.title)
print(post_objects)