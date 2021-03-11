from utils import *
import numpy as np

# Đọc dữ liệu từ xlsx
X, y = read_data_from_excel('Du lieu test-gui Doanh.xlsx')

# Chia dữ liệu train - test
X_train, X_test, y_train, y_test = train_test_split(X, y)

print('Số mẫu huấn luyện:', X_train.shape[0])
print('Số mẫu thử nghiệm:', X_test.shape[0])

# Dictionary chứa khai báo các mô hình.
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(n_estimators=10,
                                       max_features=3,     # Out of 20000
                                       random_state=0),
    "K-nn": KNeighborsRegressor(),                          # Accept default parameters
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
    "Lasso": Lasso(),
    "ElasticNet": ElasticNet(random_state=0),
    "RandomForestRegressor": RandomForestRegressor(max_depth=4, random_state=2),
    "Decision Tree Regressor":DecisionTreeRegressor(max_depth=5),
    "MultiO/P GBR" :MultiOutputRegressor(GradientBoostingRegressor(n_estimators=5)),
    "MultiO/P AdaB" :MultiOutputRegressor(AdaBoostRegressor(n_estimators=5))
}

# tạo 2 bộ dictionary chứa kết quả mô hình và độ đo
y_test_predict = dict()
y_mse = dict()

for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)                    # Hàm fit là hàm huấn luyện
    y_test_predict[name] = estimator.predict(X_test)   # Huấn luyện và lưu kết quả vào dictionary y_test_predict với key là tên của mô hình
    y_mse[name] = mean_squared_error(y_test, estimator.predict(X_test))

# Xuất kết quả độ đo của từng mô hình

for model in y_mse:
    print('RSME của', model, 'là', y_mse[model])

# Test thử 1 mẫu dữ liệu

test_sample = X_test[0]
test_label = y_test[0]
print('Mẫu thử:', test_sample)
print("Kết quả dự đoán:", ESTIMATORS["Linear regression"].predict([test_sample]))
print("Kết quả thực tế:", test_label)


# Đọc dữ liệu từ SQL
X_data, y_data = read_data_from_SQL()

# Đọc input (1 dòng, 3 cột) từ SQL (bảng Input)
X_input = load_input_from_SQL()

# Lưu input (1 dòng, 2 cột) từ SQL (bảng Prediction)
output = np.array([1,2.0,3.0])
save_output_to_SQL((1,2.0,3.0))