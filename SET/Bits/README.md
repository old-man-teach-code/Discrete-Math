# Tổng Hợp Lý Thuyết Toán Rời Rạc (Phần tập hợp - Set Theory) - Part 2

## Using Bit Strings to Find Union and Intersection of Sets (Sử dụng chuỗi bit để tìm hợp và giao của các tập hợp)

### Bit Strings (Chuỗi bit)
- **Bit string:** Một chuỗi bit là một chuỗi gồm các bit 0 và 1.
- **Ví dụ:** Chuỗi bit 1011 có nghĩa là bit 1 ở vị trí 1, bit 0 ở vị trí 2, bit 1 ở vị trí 3 và bit 1 ở vị trí 4.
- **Ví dụ 2***: 
  - U = {1, 2, 3, 4, 5}, A = {1, 3, 5}, B = {2, 3, 4}, C = {1, 2, 3, 4, 5}
  - A = 10101
  - B = 01110
  - C = 11111

### Union and Intersection of Sets using Bit Strings (Hợp và Giao của các tập hợp sử dụng chuỗi bit)
- **Union of Sets:** Để tìm hợp của hai tập hợp \(A\) và \(B\) sử dụng chuỗi bit, chúng ta chỉ cần thực hiện phép toán OR bit-wise giữa hai chuỗi bit tương ứng với \(A\) và \(B\).
- **Intersection of Sets:** Để tìm giao của hai tập hợp \(A\) và \(B\) sử dụng chuỗi bit, chúng ta chỉ cần thực hiện phép toán AND bit-wise giữa hai chuỗi bit tương ứng với \(A\) và \(B\).
- **Ví dụ:** Nếu \(A = \{1, 2, 3\}\) và \(B = \{3, 4, 5\}\), thì:
  - \(A = 1110\) (vì phần tử 1, 2, 3 có mặt trong \(A\)).
  - \(B = 0111\) (vì phần tử 3, 4, 5 có mặt trong \(B\)).
  - \(A ∪ B = 1111\) (vì \(A\) hoặc \(B\) chứa các phần tử 1, 2, 3, 4, 5).
  - \(A ∩ B = 0110\) (vì \(A\) và \(B\) đều chứa phần tử 3).
- **Compliment of a Set:** Để tìm phần bù của một tập hợp \(A\) trong tập hợp \(U\) sử dụng chuỗi bit, chúng ta chỉ cần thực hiện phép toán NOT bit-wise trên chuỗi bit tương ứng với \(A\).
  - **Ví dụ:** Nếu \(U = \{1, 2, 3, 4, 5\}\) và \(A = \{1, 3, 5\}\), thì:
    - \(A = 10101\) (vì phần tử 1, 3, 5 có mặt trong \(A\)).
    - \(A^c = 01010\) (vì phần tử 2, 4 có mặt trong \(A^c\)).