# Exercise Vision-02: Document Scanner

## 1. EXERCISE BRIEF

**Context**: OCR Document Scanning phổ cập tại Fintech định danh (KYC) e-Banking. Trích xuất tài liệu dạng Rectangles, nắn thẳng (Warp Perspective) là xử lý Computer Vision tiền quyết.
**Task**: Sử dụng OpenCV: Xử lý Thresholding, bôi nhiễu, sử dụng Thuật toán tìm Contours để bắt khối tứ giác tờ giấy ID/CCCD sau đó Transform Map Scale Flat tạo file scan chuẩn thẳng sáng.
**Constraints**: Chỉ dùng Python-OpenCV lõi `cv2`. Focus cực trị xử lý ảnh màu Grey Threshold Adaptions.
## 2. STARTER CODE

```python
import cv2
import numpy as np

class DocumentScanner:
    def __init__(self):
        """
        TODO: [... logic ...] 
        """
        pass

    def order_points(self, pts):
        """
        TODO: [... logic ...] 
        pts [... logic ...] 
        """
        rect = np.zeros((4, 2), dtype="float32")
        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        return rect

    def four_point_transform(self, image, pts):
        """
        TODO: [... logic ...] 
        """
        pass

    def scan(self, image_path: str, output_path: str):
         """
         TODO: [... logic ...] 
         """
         pass

if __name__ == "__main__":
    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        print("Please [... logic ...] !")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def four_point_transform(self, image, pts):
        rect = self.order_points(pts)
        (tl, tr, br, bl) = rect

        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")

        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
        return warped
```

**HINT-3 (Near-solution)**:

```python
    def scan(self, image_path: str, output_path: str):
        image = cv2.imread(image_path)
        orig = image.copy()

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

        screenCnt = None
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4:
                screenCnt = approx
                break

        if screenCnt is None:
            print("Could [... logic ...] ")
            return

        warped = self.four_point_transform(orig, screenCnt.reshape(4, 2))

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        cv2.imwrite(output_path, T)
        print(f"Scanned [... logic ...] {output_path}")
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `OpenCV`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `opencv-python`, `numpy`.
