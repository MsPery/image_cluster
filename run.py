from flask import Flask, render_template
from app.product_clusterer import cluster_product_images

app = Flask(__name__)

# Sample data 
images = [
    'images/beach.jpg',
    'images/birds.jpg',
    'images/brownie.jpg',
    'images/elephant.jpg',
    'images/fruits.jpg',
    'images/lipstick.jpg',
    'images/make-up.jpg',
    'images/perfume.jpg',
    'images/shoes.jpg',
    'images/snow.jpg'
]

text_descriptions = [
    'Nature',
    'Wildlife',
    'Food & Drinks',
    'Wildlife',
    'Food & Drinks',
    'Fashion & Beauty',
    'Fashion & Beauty',
    'Fashion & Beauty',
    'Sneakers',
    'Nature'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster/images')
def cluster_images():
    # Performing clustering on the provided image URLs and text descriptions
    _, clustered_images = cluster_product_images(images, text_descriptions)

    # Debug
    print("Type of clustered_images:", type(clustered_images))

    # Pass clustered data to the template
    return render_template('results.html', clustered_images=clustered_images)

if __name__ == '__main__':
    app.run(debug=True)
