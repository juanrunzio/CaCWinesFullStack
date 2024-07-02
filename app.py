from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://juan:juanrunzio@localhost/cacwine_reviews_db'
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wine_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/reviews', methods=['GET'])
def reviews():
    reviews = Review.query.order_by(Review.id.desc()).limit(5).all()
    return render_template('reviews.html', reviews=reviews)

@app.route('/add_review', methods=['POST'])
def add_review():
    wine_name = request.form['wine_name']
    review_text = request.form['review_text']
    rating = int(request.form['rating'])
    
    new_review = Review(wine_name=wine_name, review_text=review_text, rating=rating)
    db.session.add(new_review)
    db.session.commit()
    
    return redirect(url_for('reviews'))

@app.route('/delete_review/<int:id>', methods=['POST'])
def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"success": True})

@app.route('/edit_review/<int:id>', methods=['GET', 'POST'])
def edit_review(id):
    review = Review.query.get_or_404(id)
    if request.method == 'POST':
        review.wine_name = request.form['wine_name']
        review.review_text = request.form['review_text']
        review.rating = int(request.form['rating'])
        db.session.commit()
        return redirect(url_for('reviews'))
    return render_template('edit_review.html', review=review)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)