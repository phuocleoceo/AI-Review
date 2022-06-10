from numpy.random import choice
import numpy as np


class Kmean_Clustering:
    def __init__(self, K, max_iters=10):
        """
        K : số tâm cụm
        max_iters : số vòng lặp tối đa của thuật toán
        """
        self.K = K
        self.max_iters = max_iters

    def initialize_K_centroids(self, X, K):
        """
        Hàm chọn ra K tâm ngẫu nhiên ban đầu
        Mỗi tâm có kích thước n (n đặc trưng)
        """
        m, n = X.shape
        k_rand = np.ones((K, n))
        k_rand = X[choice(range(m), K, replace=False), :]
        return k_rand

    def find_closest_centroids(self, X, centroids):
        """
        Hàm tìm ra tâm gần nhất của mỗi điểm
        """
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            # Khoảng cách từ 1 điểm đến các Tâm hiện tại
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            # Ghi lại tâm gần nhất
            c[i] = np.argmin(distances)
        return c

    def compute_means(self, X, idx, K):
        """
        Hàm cập nhật tâm cụm
        """
        _, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            # Láy ra những điểm thuộc tâm tương ứng
            points_belong_k = X[np.where(idx == k)]
            # Cập nhật lại tâm cụm bằng trung bình của các điểm đós
            centroids[k] = np.mean(points_belong_k, axis=0,)
        return centroids

    def fit(self, X):
        """
        Hàm tìm K-mean của X
        """
        # Khởi tạo K tâm ngẫu nhiên
        centroids = self.initialize_K_centroids(X, self.K)
        for _ in range(self.max_iters):
            # Tìm các điểm thuộc K tâm hiện tại
            idx = self.find_closest_centroids(X, centroids)
            # Cập nhật lại K tâm cụm
            centroids = self.compute_means(X, idx, self.K)

        # Trả về các tâm cụm và chỉ số tâm của mỗi điểm
        return centroids, idx
