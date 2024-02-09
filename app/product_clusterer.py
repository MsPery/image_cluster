from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def cluster_product_images(image_urls, text_descriptions):
    # Performing clustering based on text similarity
    num_clusters = 5  

    # TF-IDF vectorization of text descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(text_descriptions)

    # KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)

    # Reducing dimensionality for visualization
    pca = PCA(n_components=2, svd_solver='arpack')
    text_embedding = pca.fit_transform(tfidf_matrix.toarray())

    # Combine text and image clusters
    clusters = list(zip(kmeans.labels_, image_urls, text_embedding))

    # Assign each image to its corresponding cluster
    clustered_images = {}
    for i, label in enumerate(kmeans.labels_):
        if label not in clustered_images:
            clustered_images[label] = []
        clustered_images[label].append(image_urls[i])

    return clusters, clustered_images
