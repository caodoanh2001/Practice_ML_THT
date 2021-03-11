# Practice_ML_THT

Source code thực hành ML
Tình trạng hiện tại:

- [x] Đọc dữ liệu từ file excel
- [x] Đọc dữ liệu từ Microsoft SQL
- [x] Nhập input từ SQL (1 dòng)
- [x] Xuất output ra SQL (1 dòng)
- [x] Một số thuật toán học máy
- [ ] Neural network
- [x] Huấn luyện/ sử dụng mô hình
- [ ] Lưu mô hình ra file .pkl (để tái sử dụng)

## 1. Cách nhập/xuất dữ liệu từ SQL

### Chỉnh config
Cần chỉnh config ở folder `configs`

```
Driver={SQL Server}
Server=<tên server>
Database=<tên database>
Trusted_Connection=yes
DATA_Table_name=<tên bảng dữ liệu>
Input_Table_name=<tên bảng input>
Output_Tabe_name=<tên bảng output>
```

### Nhập dữ liệu từ SQL
Sau khi chỉnh xong config, để nhập dữ liệu có sẵn từ SQL thực hiện:
```python
from utils import *

# Đọc dữ liệu từ SQL
X_data, y_data = read_data_from_SQL()
# Trong đó X_data, Y_data là 2 bộ mảng numpy, mỗi mảng trong X_data có 3 phần tử, còn trong Y_data mỗi mảng có 2 phần tử, dùng để huấn luyện
```

### Xuất dữ liệu từ SQL
Sau khi đưa input qua mô hình, từ mô hình dự đoán ra kết quả (sẽ là một mảng numpy 2 phần tử) ta lưu như sau:
```python
from utils import *

# Lưu dữ liệu vào SQL
output = np.array([1,2.0,3.0]) # đây là output Y = [2.0, 3.0], 1 là số thứ tự primary key trong SQL
save_output_to_SQL(output)
# 
```

## 2. Huấn luyện/ thử nghiệm các mô hình

Đang cập nhật

## 3. Lưu mô hình ra file .pkl

Đang cập nhật

## 4. Load mô hình và sử dụng

Đang cập nhật
