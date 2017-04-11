from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("landing.html")


@app.route("/", methods=["POST"])
def update_avatar():
    text = request.form["text"]
    if not text:
        return render_template("landing.html")

    import io as io
    import base64 as b
    import generator as gen

    buffer = io.BytesIO()
    image = gen.get_image(text)
    image.save(buffer, format="PNG")
    image_data = buffer.getvalue()
    image_data = b.b64encode(image_data)
    image_data = image_data.decode()

    return render_template("main.html", name=text, image=image_data)

if __name__ == "__main__":
    app.run()
