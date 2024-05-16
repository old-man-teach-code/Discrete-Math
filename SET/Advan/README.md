# Tổng Hợp Lý Thuyết Toán Rời Rạc - Part 3

## Tính Chất Của Tập Hợp (Set Identities)

### Các Quy Tắc Cơ Bản (Basic Laws)
- **Identity laws (Quy tắc đồng nhất)**: \(A ∩ U = A\), \(A ∪ ∅ = A\)
- **Domination laws (Quy tắc chi phối)**: \(A ∪ U = U\), \(A ∩ ∅ = ∅\)
- **Idempotent laws (Quy tắc đồng nhất đa nhiệm)**: \(A ∪ A = A\), \(A ∩ A = A\)
- **Complementation law (Quy tắc bù trừ)**: \(A = A\)
- **Commutative laws (Quy tắc giao hoán)**: \(A ∪ B = B ∪ A\), \(A ∩ B = B ∩ A\)

### Các Quy Tắc Kết Hợp (Associative Laws)
- **Associative laws (Quy tắc kết hợp)**: \(A ∪ (B ∪ C) = (A ∪ B) ∪ C\), \(A ∩ (B ∩ C) = (A ∩ B) ∩ C\)

### Các Quy Tắc Phân Phối (Distributive Laws)
- **Distributive laws (Quy tắc phân phối)**: \(A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)\), \(A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)\)

### Định Lý De Morgan (De Morgan’s Laws)
- **De Morgan’s laws (Quy tắc De Morgan)**: \((A ∩ B)^c = A^c ∪ B^c\), \((A ∪ B)^c = A^c ∩ B^c\)

### Các Quy Tắc Hấp Thụ (Absorption Laws)
- **Absorption laws (Quy tắc hấp thụ)**: \(A ∪ (A ∩ B) = A\), \(A ∩ (A ∪ B) = A\)

### Các Quy Tắc Bổ Sung (Complement Laws)
- **Complement laws (Quy tắc bổ sung)**: \(A ∪ A^c = U\), \(A ∩ A^c = ∅\)

## Cách Chứng Minh Hai Tập Hợp Bằng Nhau (How to Prove Two Sets Are Equal)
- Để chứng minh hai tập hợp \(A\) và \(B\) bằng nhau, \(A = B\), ta cần chứng minh \(A ⊆ B\) và \(B ⊆ A\).
- **Chứng minh**: Để chứng minh \(A ⊆ B\), ta cần chứng minh rằng mọi phần tử của \(A\) đều thuộc \(B\). Tương tự, để chứng minh \(B ⊆ A\), ta cần chứng minh rằng mọi phần tử của \(B\) đều thuộc \(A\). Nếu cả hai điều này đều đúng, ta có thể kết luận \(A = B\).

- **Ví dụ**: Chứng minh \(A = B\) với \(A = \{1, 2, 3\}\) và \(B = \{x | x ∈ ℤ và 0 < x < 4\}\). 

## Bảng Thành Viên (Membership Tables)
- **Khái niệm**: Bảng thành viên cho thấy tất cả các kết hợp của các tập hợp mà một phần tử có thể thuộc về, sử dụng 1 để biểu thị phần tử thuộc tập hợp và 0 để biểu thị phần tử không thuộc tập hợp.
- **Ví dụ**:

| A | B | A ∪ B | A ∩ B | A − B |
|---|---|-------|-------|-------|
| 1 | 1 |   1   |   1   |   0   |
| 1 | 0 |   1   |   0   |   1   |
| 0 | 1 |   1   |   0   |   0   |
| 0 | 0 |   0   |   0   |   0   |

- **Ví dụ**: Lập bảng thành viên cho các tập hợp \(A\), \(B\), và \(C\) với các phần tử như sau:
  - \(A = \{1, 2\}\)
  - \(B = \{2, 3\}\)
  - \(C = \{3, 4\}\)

  Bước 1: Lập tập hợp U = {1, 2, 3, 4}.
  Bước 2: Xác định các phần tử của A, B, và C trong U (Bit)
  A = {1, 2} = 1100
  B = {2, 3} = 0110
  C = {3, 4} = 0001
Vậy ta có bảng thành viên như sau:

    | Phần Tử | \(A\) | \(B\) | \(C\) | \(B ∩ C\) | 
    |---------|-------|-------|-------|-----------|
    |    1    |   1   |   0   |   0   |     0     | 
    |    2    |   1   |   1   |   0   |     0     | 
    |    3    |   0   |   1   |   1   |     1     |
    |    4    |   0   |   0   |   1   |     0     | 



## Sử Dụng Bảng Thành Viên Để Chứng Minh Các Tính Chất
- **Ví dụ**: Chứng minh \(A ∩ B = B − (B − A)\) bằng bảng thành viên.

| A | B | A ∩ B | B − A | B − (B − A) |
|---|---|-------|-------|-------------|
| 1 | 1 |   1   |   0   |      1      |
| 1 | 0 |   0   |   0   |      0      |
| 0 | 1 |   0   |   1   |      0      |
| 0 | 0 |   0   |   0   |      0      |


## Định Nghĩa và Phép Toán Trên "Bags" (Multisets)
### Định Nghĩa
- **Bag**: Một "bag" (hay multiset) là một mở rộng của khái niệm tập hợp, cho phép nhiều phần tử giống nhau xuất hiện nhiều lần.
- **Độ nhiều (Multiplicity)**: Số lần xuất hiện của mỗi phần tử trong "bag".
- **Ký hiệu**: Bag được ký hiệu bằng \(\{|\ |\}\) để phân biệt với tập hợp \(\{\}\).

### Ví Dụ
- Bag \(\{|m, m, n, n, n|\}\): phần tử \(m\) có độ nhiều là 2, \(n\) có độ nhiều là 3.

### Phép Toán Trên "Bags"
- **Hợp (Union)**: Độ nhiều của một phần tử trong \(A ∪ B\) là giá trị lớn nhất của độ nhiều của phần tử đó trong \(A\) và \(B\).
- **Giao (Intersection)**: Độ nhiều của một phần tử trong \(A ∩ B\) là giá trị nhỏ nhất của độ nhiều của phần tử đó trong \(A\) và \(B\).
- **Hiệu (Difference)**: Độ nhiều của một phần tử trong \(A − B\) là độ nhiều của phần tử đó trong \(A\) trừ đi độ nhiều của phần tử đó trong \(B\) nếu kết quả là dương, và bằng 0 nếu kết quả là 0 hoặc âm.
- **Tổng (Sum)**: Độ nhiều của một phần tử trong \(A + B\) là tổng độ nhiều của phần tử đó trong \(A\) và \(B\).
- **Kích thước (Cardinality)**: Tổng số độ nhiều của tất cả các phần tử trong "bag".

### Ví Dụ về Phép Toán Trên "Bags"
- **Hợp**:
  - \(A = \{|a, m, m, m, n|\}\)
  - \(B = \{|a, a, m, m, n, n, n, n, r|\}\)
  - \(A ∪ B = \{|a, a, m, m, m, n, n, n, n, r|\}\)

- **Giao**:
  - \(A = \{|a, m, m, m, n|\}\)
  - \(B = \{|a, a, m, m, n, n, n, n, r|\}\)
  - \(A ∩ B = \{|a, m, m, n|\}\)

- **Hiệu**:
  - \(A = \{|a, m, m, m, n|\}\)
  - \(B = \{|a, a, m, m, n, n, n, n, r|\}\)
  - \(A - B = \{|m|\}\)
  - \(B - A = \{|a, n, n, n, r|\}\)

- **Tổng**:
  - \(A = \{|a, m, m, m, n|\}\)
  - \(B = \{|a, a, m, m, n, n, n, n, r|\}\)
  - \(A + B = \{|a, a, a, m, m, m, m, m, n, n, n, n, n, r|\}\)

- **Kích thước**:
  - \(A = \{|a, m, m, m, n|\}\)
  - \(B = \{|a, a, m, m, n, n, n, n, r|\}\)
  - \(|A| = 1 + 3 + 1 = 5\)
  - \(|B| = 2 + 2 + 4 + 1 = 9\)

## Ứng Dụng của "Bags"
- "Bags" lý tưởng cho việc xử lý các phân tích nguyên tố của số. Ví dụ, số 630 có thể được biểu diễn dưới dạng bag như sau:
  - \(630 = 2 × 3^2 × 5 × 7\) được biểu diễn là bag \(\{|2:1, 3:2, 5:1, 7:1|\}\).

