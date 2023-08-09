from flask import Flask


import sqlite3

app = Flask(__name__)


@app.route('/cart', methods=['GET', 'PUT'])
def cart():
    return "This is the cart page."


@app.route('/cart/order', methods=['POST'])
def cart_order():
    return "This is the order page."


@app.route('/cart/add', methods=['POST'])
def cart_add():
    return "This is the add page."


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def user():
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM User")
    RESULT = res.fetchall()
    return str(RESULT)


@app.route('/user/register', methods=['POST'])
def user_register():
    return "This is the register page."


@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():
    return "This is the sign in page."


@app.route('/user/logout', methods=['POST', 'GET'])
def user_logout():
    return "This is the log out page."


@app.route('/user/restore', methods=['POST'])
def user_restore():
    return "This is the restore page."


@app.route('/user/orders', methods=['GET'])
def user_orders_history():
    return "This is the orders history page."


@app.route('/user/order/<order_id>', methods=['GET'])
def user_order(order_id: int):
    return "This is the something order page."


@app.route('/user/address', methods=['GET', 'POST'])
def user_address_list():
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM Address")
    RESULT = res.fetchall()
    return str(RESULT)


@app.route('/user/address/<address_id>', methods=['GET', 'POST', 'DELETE'])
def user_address(address_id: int):
    return "This is the something address page."


@app.route('/menu', methods=['GET'])
def menu():
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM Dishes")
    RESULT = res.fetchall()
    return str(RESULT)


@app.route('/menu/<category_menu>', methods=['GET'])
def category(category_menu: str):
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM Category")
    RESULT = res.fetchall()
    return str(RESULT)


@app.route('/menu/<category_menu>/<dish>', methods=['GET'])
def get_dish(category_menu, dish: str):
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM Dishes")
    RESULT = res.fetchall()
    return str(RESULT)


@app.route('/menu/<category_menu>/<dish>/review', methods=['POST'])
def review_dish(category_menu, dish: str):
    return "This is review the dish page in category."


@app.route('/menu/search/<name>', methods=['GET', 'POST'])
def search_by_menu(name: str):
    return "This is the search page."


@app.route('/admin/dishes', methods=['GET', 'POST'])
def admin_dishes():
    return "This is the list dishes page."


@app.route('/admin/dishes/<dish>', methods=['GET', 'POST', 'DELETE'])
def redaction_dishes(dish: str):
    return "This is the list dish page."


@app.route('/admin/orders', methods=['GET'])
def admin_orders():
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM Orders")
    RESULT = res.fetchall()
    return str(RESULT)


@app.route('/admin/orders/<order_id>', methods=['GET', 'POST'])
def admin_order(order_id: int):
    return "This is the order page."


@app.route('/admin/categories', methods=['GET', 'POST'])
def admin_categories():
    return "This is the categories page."


@app.route('/admin/categories/<category_id>', methods=['DELETE'])
def admin_category(category_id: str):
    return "This is the category page."


@app.route('/admin/search/<name>', methods=['DELETE'])
def admin_search(name: str):
    return "This is the dish or category page."


if __name__ == "__main__":
    app.run()
