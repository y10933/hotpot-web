from flask import Flask, render_template, request
import os

app = Flask(__name__)

menu = {
    "沙茶鍋": 180,
    "牛奶鍋": 200,
    "麻辣鍋": 220
}

side = {
    "白飯": 0,
    "冬粉": 0,
    "王子麵": 0,
    "烏龍麵": 10,
    "雞蛋": 10
}

meat = {
    "豬肉片": 10,
    "培根牛": 40,
    "松阪豬": 188
}

@app.route("/", methods=["GET", "POST"])
def index():
    cart = []
    total = 0

    if request.method == "POST":

        # 主餐 + 數量
        main = request.form.get("main")
        main_qty = int(request.form.get("main_qty", 1))

        if main in menu:
            cart.append(f"{main} x{main_qty}")
            total += menu[main] * main_qty

        # 副餐 + 數量
        side_item = request.form.get("side")
        side_qty = int(request.form.get("side_qty", 1))

        if side_item in side:
            cart.append(f"{side_item} x{side_qty}")
            total += side[side_item] * side_qty

        # 加肉（多選 + 數量固定1）
        meats = request.form.getlist("meat")
        for m in meats:
            if m in meat:
                cart.append(m)
                total += meat[m]

        # 刪除（用名稱刪）
        delete_item = request.form.get("delete")
        if delete_item:
            if delete_item in cart:
                cart.remove(delete_item)

    return render_template("index.html",
                           menu=menu,
                           side=side,
                           meat=meat,
                           cart=cart,
                           total=total)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
