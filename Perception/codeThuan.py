import numpy as np


# Hàm sign trả về 1 nếu value dương, -1 nếu âm, 0 nếu value = 0
def pred(w, x):
    return np.sign((w.T).dot(x))


# Hàm kiểm tra sự hội tụ, đúng với tất cả các điểm dữ liệu
def has_converged(X, y, w):
    return np.array_equal(pred(w, X), y)


def perceptron(X, y, w_init):
    w = [w_init]
    d = X.shape[0]
    mis_points = []
    while True:
        # mix data
        mix_id = np.random.permutation(X.shape[1])

        for i in range(X.shape[1]):
            xi = X[:, mix_id[i]].reshape(d, 1)
            yi = y[0, mix_id[i]]
            # Nếu có điểm lỗi thì đi cập nhật
            if pred(w[-1], xi)[0] != yi:
                mis_points.append(mix_id[i])
                w_new = w[-1]+yi*xi
                w.append(w_new)

        if has_converged(X, y, w[-1]):
            break
    return w, mis_points


if __name__ == "__main__":
    X = np.array([[10.0, 5.0, 7.0, 4.0, 4.0, 5.0, 8.0, 8.0, 7.0, 6.0],
                  [1.0, 2.0, 1.0, 2.5, 1.0, 0.5, 0.5, 1.0, 0.3, 0.3]])
    # y = np.array([[1, 1, 1, 1, 0, 0, 0, 1, 0, 0]])
    y = np.array([[1, 1, 1, 1, -1, -1, -1, 1, -1, -1]])
    # extended data
    Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)

    w_init = np.random.randn(Xbar.shape[0], 1)
    w, m = perceptron(Xbar, y, w_init)
    print(w[-1].T)

    y_pred = pred(w[-1], [1, 4, 3])
    print(y_pred[0])
