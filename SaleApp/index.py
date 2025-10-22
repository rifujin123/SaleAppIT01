from flask import Flask, render_template
import dao
# tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cho trang chủ
@app.route("/")
def index():
    name = "Khoi Le"
    cates = dao.load_category()
    return render_template("index.html", name=name, categories=cates)
    # Gửi dữ liệu 'name' đến template index.html
    return render_template("index.html", name = name)

# Chạy ứng dụng Flask
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)