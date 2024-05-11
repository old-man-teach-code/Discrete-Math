# Tổng Hợp Lý Thuyết Toán Rời Rạc

## Định Nghĩa và Đặc Điểm

### Tập hợp (Set)
- **Định nghĩa:** Một tập hợp là một bộ sưu tập không có thứ tự của các đối tượng, gọi là phần tử (elements) của tập hợp đó.
- **Ký hiệu:** Sử dụng chữ cái in hoa để đặt tên cho tập hợp, ví dụ \(A\), \(B\), \(C\),...
- **Cách biểu diễn:** Phần tử của tập hợp được liệt kê trong ngoặc nhọn, ví dụ \(A = \{a, b, c\}\).
- **Phần tử:** \(a ∈ A\) có nghĩa là \(a\) là một phần tử của \(A\); \(a ∉ A\) có nghĩa là \(a\) không phải là phần tử của \(A\).

### Tập hợp rỗng (Empty Set)
- **Định nghĩa:** Tập hợp không chứa phần tử nào, ký hiệu là \(∅\).

### Tập hợp con và Tập hợp thực sự (Subset and Proper Subset)
- **Tập hợp con (Subset):** \(A ⊆ B\) nếu mọi phần tử của \(A\) cũng là phần tử của \(B\).
- **Tập hợp thực sự (Proper Subset):** \(A ⊂ B\) nếu \(A\) là tập hợp con của \(B\) và \(A\) không bằng \(B\).

### Tích Descartes (Cartesian Product)
- **Định nghĩa:** Tích Descartes của hai tập hợp \(A\) và \(B\) là tập hợp các cặp có thứ tự \((a, b)\), với \(a ∈ A\) và \(b ∈ B\).
- **Ký hiệu:** \(A × B = \{(a, b) | a ∈ A \text{ và } b ∈ B\}\).

### Quan hệ (Relation)
- **Định nghĩa:** Một quan hệ từ tập hợp \(A\) đến \(B\) là một tập hợp con của tích Descartes \(A × B\).

## Tính Chất Cơ Bản

### Đẳng thức tập hợp (Equal Sets)
- **Định nghĩa:** Hai tập hợp là bằng nhau nếu chúng có cùng các phần tử.
- **Ký hiệu:** \(A = B\) nếu mọi \(x\), \(x ∈ A\) khi và chỉ khi \(x ∈ B\).

### Axiom of Extension (Tiên đề mở rộng)
- **Định nghĩa:** Một tập hợp được xác định bởi các phần tử của nó. Thứ tự các phần tử không quan trọng và mỗi phần tử chỉ được liệt kê một lần.

### Đồ thị Venn (Venn Diagrams)
- **Sử dụng:** Đồ thị Venn được sử dụng để biểu diễn các mối quan hệ giữa các tập hợp.

## Công Thức và Tính Chất Nâng Cao

### Tập hợp các tập con (Power Set)
- **Định nghĩa:** Tập hợp các tập con của một tập hợp \(S\) bao gồm tất cả các tập con của \(S\).
- **Ký hiệu:** \(P(S)\), ví dụ nếu \(S = \{1, 2, 3\}\) thì \(P(S) = \{∅, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}\).

### Kích thước của tập hợp (Cardinality)
- **Định nghĩa:** Số lượng phần tử trong một tập hợp, ký hiệu là \(|S|\).

### Định lý De Morgan
- **Công thức:**
  - \((A ∪ B)^c = A^c ∩ B^c\)
  - \((A ∩ B)^c = A^c ∪ B^c\)
