from flask import Flask, render_template, request
import os

app = Flask(__name__)

menu = {
    "沙茶鍋": 180,
    "牛奶鍋": 200,
    "麻辣鍋": 220
}

@app.route("/", methods=["GET", "POST"])
def index():
    total = 0
    selected = ""

    if request.method == "POST":
        selected = request.form.get("food")
        if selected in menu:
            total = menu[selected]

    return render_template("index.html",
                           menu=menu,
                           total=total,
                           selected=selected)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
