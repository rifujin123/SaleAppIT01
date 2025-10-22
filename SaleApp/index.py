from pprint import pprint

from flask import Flask, render_template, request
import dao
# tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cho trang chủ
@app.route("/")
def index():
    name = "Flask"
    search = request.args.get('q')
    cate_id = request.args.get('cate_id')

    cates = dao.load_category()
    prod = dao.load_products(q=search, cate_id = cate_id)

    return render_template("index.html", name=name, categories=cates, prod =prod)
    # Gửi dữ liệu 'name' đến template index.html
    return render_template("index.html", name = name)

# Chạy ứng dụng Flask
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)