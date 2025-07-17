from flask import Flask, render_template, request, redirect, url_for, flash
from src.shop import Shop
from src.sweet import Sweet

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key
shop = Shop()

@app.route('/')
def index():
    sweets = shop.view_sweets()
    return render_template('index.html', sweets=sweets)

@app.route('/add_sweet', methods=['GET', 'POST'])
def add_sweet():
    if request.method == 'POST':
        try:
            id = int(request.form['id'])
            name = request.form['name']
            category = request.form['category']
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            sweet = Sweet(id, name, category, price, quantity)
            shop.add_sweet(sweet)
            flash('Sweet added successfully!', 'success')
            return redirect(url_for('index'))
        except (ValueError, TypeError) as e:
            flash(str(e), 'danger')
    return render_template('add_sweet.html')

@app.route('/search_sweets', methods=['GET', 'POST'])
def search_sweets():
    if request.method == 'POST':
        name = request.form.get('name', '')
        category = request.form.get('category', '')
        min_price = float(request.form['min_price']) if request.form.get('min_price') else None
        max_price = float(request.form['max_price']) if request.form.get('max_price') else None
        results = shop.search_sweets(name=name, category=category, min_price=min_price, max_price=max_price)
        return render_template('search_sweets.html', sweets=results)
    return render_template('search_sweets.html', sweets=[])

@app.route('/sort_sweets/<by>')
def sort_sweets(by):
    try:
        sweets = shop.sort_sweets(by=by)
        return render_template('index.html', sweets=sweets)
    except ValueError as e:
        flash(str(e), 'danger')
        return redirect(url_for('index'))

@app.route('/purchase_sweet/<int:id>', methods=['GET', 'POST'])
def purchase_sweet(id):
    if request.method == 'POST':
        try:
            quantity = int(request.form['quantity'])
            shop.purchase_sweet(id, quantity)
            flash('Purchase successful!', 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e), 'danger')
    return render_template('purchase_sweet.html', id=id)

@app.route('/restock_sweet/<int:id>', methods=['GET', 'POST'])
def restock_sweet(id):
    if request.method == 'POST':
        try:
            quantity = int(request.form['quantity'])
            shop.restock_sweet(id, quantity)
            flash('Sweet restocked successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e), 'danger')
    return render_template('restock_sweet.html', id=id)

@app.route('/delete_sweet/<int:id>')
def delete_sweet(id):
    try:
        shop.delete_sweet(id)
        flash('Sweet deleted successfully!', 'success')
    except ValueError as e:
        flash(str(e), 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)