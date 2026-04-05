# Exercise Cyber-07: Compliance Scanner for Decree 13/2023

## 1. EXERCISE BRIEF
**Context**: Nghị định 13/2023/NĐ-CP của Chính phủ về Bảo vệ Dữ liệu Cá nhân yêu cầu các tổ chức tại Việt Nam phải phân loại, theo dõi và bảo vệ thông tin cá nhân (PII). Việc rà soát thủ công hàng nghìn file code là bất khả thi. Thay vào đó, kỹ sư bảo mật cần xây dựng các công cụ "Static Analysis" (SAST) chuyên nghiệp để tự động phát hiện các đoạn code xử lý dữ liệu nhạy cảm mà không có cơ chế bảo vệ.

**Task**: Xây dựng một trình quét tuân thủ (Compliance Scanner) sử dụng Abstract Syntax Tree (AST) của Python. Phát hiện các mẫu xử lý dữ liệu cá nhân không an toàn: Ghi log (print/logger) tên/số điện thoại/email trực tiếp; lưu trữ nhạy cảm không mã hóa; thiếu các hàm kiểm tra sự đồng ý (consent check); hoặc dùng các credential cứng (hardcoded credentials).

**Constraints**: Bắt buộc sử dụng module `ast` để phân tích cấu trúc code. Định nghĩa các quy tắc (Patterns) tìm kiếm dưới dạng file YAML cấu hình. Xuất báo cáo tuân thủ có phân loại mức độ nghiêm trọng (Severity).

## 2. STARTER CODE
```python
import ast
import yaml

class ComplianceScanner(ast.NodeVisitor):
    def __init__(self, rules_path):
        with open(rules_path, 'r') as f:
            self.rules = yaml.safe_load(f)
        self.findings = []

    def visit_Call(self, node):
        # TODO: Phát hiện logging hay print các biến có tên 'email', 'phone', 'fullname'
        # node.func.id == 'print'
        self.generic_visit(node)

    def visit_Assign(self, node):
        # TODO: Phát hiện gán password/secret cứng vào biến
        self.generic_visit(node)

    def generate_report(self):
        # TODO: Trả về JSON report với severity
        pass

# Example usage
# scanner = ComplianceScanner("decree_13_rules.yaml")
# scanner.visit(ast.parse(open("my_webapp.py").read()))
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Module `ast` cho phép bạn "nhìn" thấy cấu trúc code mà không cần chạy nó. Hãy dùng `ast.walk()` hoặc kế thừa `ast.NodeVisitor` để duyệt qua toàn bộ các hàm gọi (`Call`) và gán biến (`Assign`).
**HINT-2 (Partial)**: Kiểm tra logging: Nếu `node.func.id` (hoặc `node.func.attr`) là `info`, `debug`, `print`, hãy kiểm tra các `args` bên dưới. Nếu có biến (Name) hoặc chuỗi (Constant) trùng với list PII trong YAML, hãy cảnh báo.
**HINT-3 (Near-solution)**: Quy tắc YAML mẫu: `pii_fields: [email, sdt, cmnd, hoten]`, `sensitive_assign: [password, secret, token]`. Sử dụng Regex để so khớp mờ (fuzzy matching) tên biến.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Bandit (Python Security), SonarQube, Semgrep.
- **Why do it manually**: Tùy chỉnh bộ quy tắc (Ruleset) chính xác theo ngôn ngữ và thực tế luật pháp Việt Nam (Nghị định 13) mà các công cụ quốc tế thường bỏ qua.

## 5. VALIDATION CRITERIA
- [ ] Phát hiện được ít nhất 3 vị trí rò rỉ dữ liệu (PII Leakage) trong một file code mẫu.
- [ ] Báo cáo đúng dòng (lineno) và cột (col_offset) xảy ra lỗi.
- [ ] Không bị "False Positive" với các biến trùng tên nhưng nằm trong context an toàn (như docstring).

## 6. EXTENSION CHALLENGES
1. **Auto-fixer**: Tự động thay thế `print(email)` thành `print(mask_email(email))` sử dụng `ast.unparse`.
2. **Dependency Audit**: Kiểm tra file `requirements.txt` xem có các thư viện bị dính lỗ hổng bảo mật (CVE) đã biết không.
3. **Control Flow Analysis**: Kiểm tra xem trước khi gọi hàm xử lý dữ liệu, có hàm `check_consent()` nào được gọi trước đó không.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: `pip install pyyaml`
