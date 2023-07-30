from flask import Flask

app = Flask(__name__)


@app.route('/cart', methods=['GET', 'PUT'])
def cart():
    return


@app.route('/cart/order', methods=['POST'])
def cart_order():
    return


@app.route('/cart/add', methods=['POST'])
def cart_add():
    return


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def user():
    return


@app.route('/user/register', methods=['POST'])
def user_register():
    return


@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():
    return


@app.route('/user/logout', methods=['POST', 'GET'])
def user_logout():
    return


@app.route('/user/restore', methods=['POST'])
def user_restore():
    return


@app.route('/user/orders', methods=['GET'])
def user_orders_history():
    return


@app.route('/user/order/<order_id>', methods=['GET'])
def user_order(order_id: int):
    return


@app.route('/user/address', methods=['GET', 'POST'])
def user_address_list():
    return


@app.route('/user/address/<address_id>', methods=['GET', 'POST', 'DELETE'])
def user_address(address_id: int):
    return


@app.route('/menu', methods=['GET'])
def menu():
    return


@app.route('/menu/<category_menu>', methods=['GET'])
def category(category_menu: str):
    return


@app.route('/menu/<category_menu>/<dish>', methods=['GET'])
def get_dish(dish: str):
    return


@app.route('/menu/<category_menu>/<dish>/review', methods=['POST'])
def review_dish(dish: str):
    return


@app.route('/menu/search/<name>', methods=['GET', 'POST'])
def search_by_menu(name: str):
    return


if __name__ == "__main__":
    app.run()
