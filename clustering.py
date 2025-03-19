import data
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def preprocess_data(data):
    """Przetwarza dane wejściowe."""
    return data.process_data()

def standardize_data(df):
    """Standaryzuje dane."""
    scaler = StandardScaler()
    return scaler.fit_transform(df)

def reduce_dimensions(data, n_components=2):
    """Redukuje wymiarowość danych za pomocą PCA."""
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)

def find_optimal_clusters(data, cluster_range=range(2, 15)):
    """Znajduje optymalną liczbę klastrów na podstawie metody łokcia i współczynnika sylwetki."""
    inertia = []
    silhouette_scores = []
    
    for k in cluster_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        inertia.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(data, kmeans.labels_))
    
    optimal_clusters = cluster_range[silhouette_scores.index(max(silhouette_scores))]
    return optimal_clusters, inertia, silhouette_scores, cluster_range

def perform_clustering(data, n_clusters):
    """Przeprowadza klasteryzację K-Means."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(data)
    return kmeans, clusters

def compute_cluster_means(ingredient_df, clusters):
    """Dodaje informacje o klastrach do danych i oblicza średnie wartości dla każdego klastra."""
    ingredient_df['cluster'] = clusters
    cluster_means = ingredient_df.groupby('cluster').mean()
    return cluster_means, ingredient_df

