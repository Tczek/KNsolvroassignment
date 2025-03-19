import data
import clustering
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


ingredient_df = clustering.preprocess_data(data)
scaled_data = clustering.standardize_data(ingredient_df)
reduced_data = clustering.reduce_dimensions(scaled_data)
optimal_clusters, inertia, silhouette_scores, cluster_range = clustering.find_optimal_clusters(reduced_data)
kmeans, clusters = clustering.perform_clustering(reduced_data, optimal_clusters)
cluster_means, ingredient_df = clustering.compute_cluster_means(ingredient_df, clusters)

# Plot for drink category popularity
def drink_category_plot():
    df = data.get_data()
    plt.figure(figsize=(12, 6))
    df['category'].value_counts().plot(
        kind='bar',
        color='skyblue'
    )
    plt.xlabel("Kategoria drinka")
    plt.ylabel("Liczba drinków")
    plt.title("Popularność kategorii drinków")
    plt.xticks(rotation=45)
    return plt.show()


# Plot for glass type popularity
def drink_glass_plot():
    df = data.get_data()
    plt.figure(figsize=(12, 6))
    df['glass'].value_counts().plot(
        kind='bar',
        color='lightcoral'
    )
    plt.xlabel("Rodzaj szkła")
    plt.ylabel("Liczba drinków")
    plt.title("Popularność typów szkła")
    plt.xticks(rotation=45)
    return plt.show()


# Plot for number of ingredients
def drink_ingredient_num_plot():
    df = data.process_data()
    plt.figure(figsize=(10, 6))
    sns.histplot(
        df['num_ingredients'],
        bins=15,
        kde=True
    )
    plt.xlabel("Liczba składników")
    plt.ylabel("Liczba drinków")
    plt.title("Rozkład liczby składników w drinkach")
    return plt.show()


# Plot for alcoholic content
def drink_alcoholic_plot():
    df = data.get_data()
    plt.figure(figsize=(8, 6))
    sns.countplot(x=df['alcoholic'])
    plt.xlabel("Alkoholowy")
    plt.ylabel("Liczba drinków")
    plt.title("Podział drinków na alkoholowe i bezalkoholowe")
    return plt.show()


# Plot for inertia and silhouette score
def inertia_silhouette_plot():
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].plot(cluster_range, inertia, marker='o')
    ax[0].set_xlabel('Liczba klastrów')
    ax[0].set_ylabel('Inercja')
    ax[0].set_title('Metoda łokcia')

    ax[1].plot(cluster_range, silhouette_scores, marker='o', color='r')
    ax[1].set_xlabel('Liczba klastrów')
    ax[1].set_ylabel('Silhouette Score')
    ax[1].set_title('Silhouette Score dla różnych klastrów')

    return plt.show()


# Visualization of clusters in 2D
def cluster_visualization_plot():
    plt.figure(figsize=(10, 7))
    sns.scatterplot(
        x=reduced_data[:, 0],
        y=reduced_data[:, 1],
        hue=clusters,
        palette='viridis',
        alpha=0.7
    )
    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        c='red',
        marker='x',
        s=200,
        label="Centroidy"
    )
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.title("Wizualizacja klastrów koktajli w 2D")
    plt.legend()
    return plt.show()


# Plot for features in clusters
def features_clusters_plot():
    df = ingredient_df
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    sns.boxplot(x=clusters, y=df['num_ingredients'], ax=axes[0])
    axes[0].set_title("Rozkład liczby składników na Klaster")
    axes[0].set_ylabel('Ilość składników')
    axes[0].set_xlabel('Klaster')

    df = data.get_data()
    sns.countplot(x=clusters, hue=df['category'], ax=axes[1])
    axes[1].set_title("Popularność kategorii drinków na Klaster")
    axes[1].set_ylabel('Ilość')
    axes[1].set_xlabel('Klaster')

    sns.countplot(x=clusters, hue=df['glass'], ax=axes[2])
    axes[2].set_title("Popularność typów szkła na Klaster")
    axes[2].set_ylabel('Ilość')
    axes[2].set_xlabel('Klaster')

    return plt.show()


# Interactive plot for cluster feature means
def interactive_plot():
    fig = px.bar(
        cluster_means,
        title="Rozmieszczenie klastrów z średnią wartością cech",
        labels={
            'value': 'Średnia wartość cechy',
            'cluster': 'Klaster'
        },
        color_discrete_sequence=px.colors.sequential.Viridis
    )

    fig.update_layout(
        xaxis_title="Klaster",
        yaxis_title="Średnia wartość cechy",
        xaxis_tickangle=45,
        legend_title="Klaster",
        legend=dict(x=1.05, y=1)
    )

    return fig.show()

