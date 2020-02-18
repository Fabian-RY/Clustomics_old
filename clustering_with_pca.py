from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import pandas as pd
import plotly.express as px

#Clustering

def cluster(array, num_clusters, distance_type, linkage_type):
    algorithm = AgglomerativeClustering(
                                        linkage=linkage_type,
                                        n_clusters=num_clusters,
                                        affinity=distance_type)
    algorithm.fit(array)
    validation = silhouette_score(array, algorithm.labels_, metric=distance_type)
    return ([str(label) for label in algorithm.labels_], validation)

#pca
def twodimensions(data, group_labels):

    pca = PCA(n_components=2)
    X_r = pca.fit(data).transform(data)
    pc1_values = [sample[0] for sample in X_r]
    pc2_values = [sample[1] for sample in X_r]
    data = pd.DataFrame(data = {"pc1":pc1_values,"pc2":pc2_values, "Group":group_labels})
    return (data,pca.explained_variance_ratio_)
#plotting
def plotPCA(transformed_data):
    fig = px.scatter(transformed_data[0], x = "pc1", y = "pc2", color = "Group")

    fig.update_layout(
        title="PCA",
        xaxis_title="PC1 (%.3f)"%(transformed_data[1][0]),
        yaxis_title="PC2 (%.3f)"%(transformed_data[1][1]),
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    fig.show()

#example
if __name__ == "__main__":
    print("Executing PCA example with 'iris' data.")
    from sklearn import datasets
    iris = datasets.load_iris()
    Z = pd.DataFrame(iris.data)

    a = cluster(array = Z, num_clusters = 3, distance_type = "euclidean", linkage_type = "ward")
    b = twodimensions(Z,a[0])
    plotPCA(b)
