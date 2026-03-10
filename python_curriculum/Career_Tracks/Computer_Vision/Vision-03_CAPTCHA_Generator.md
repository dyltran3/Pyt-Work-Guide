# Exercise Vision-03: CAPTCHA Generator

## 1. EXERCISE BRIEF

**Context**: Hàng thủ Anti-Bot (Bot Protection) yêu cầu thuật toán Randomizer Text CAPTCHA sinh ra nhiễu và độ méo méo mờ hình ảnh (Noise Transformation).
**Task**: Gen ảnh CAPTCHA: Tạo String text bất quy tắc ngẫu nhiên, Render Font vẽ lên ảnh phối hợp Lines, Points Noise Distortion để bot AI ko tự crack.
**Constraints**: Thao tác trên Pillow (PIL). Cải biên méo font (Warping Curve).
## 2. STARTER CODE

```python
from PIL import Image, ImageDraw, ImageFont
import random
import string

class CaptchaGenerator:
    def __init__(self, bg_color=(255, 255, 255), fg_color=(0, 0, 0), length=6):
        """
        TODO: [... logic ...] 
        """
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.length = length

    def generate_random_string(self) -> str:
        """
        TODO: [... logic ...] 
        """
        pass

    def create_captcha(self, text: str, output_path: str):
        """
        TODO: [... logic ...] 
        Include noise [... logic ...] 
        """
        pass

if __name__ == "__main__":
    import os
    import tempfile

    generator = CaptchaGenerator()

    with tempfile.TemporaryDirectory() as tmp:
        captcha_path = os.path.join(tmp, "captcha.png")
        text = generator.generate_random_string()
        print(f"Generating CAPTCHA [... logic ...] {text} at {captcha_path}...")
        generator.create_captcha(text, captcha_path)
        print("Done [... logic ...] ")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def generate_random_string(self) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=self.length))
```

**HINT-3 (Near-solution)**:

```python
    def create_captcha(self, text: str, output_path: str):
        width, height = 200, 80
        image = Image.new('RGB', (width, height), self.bg_color)
        draw = ImageDraw.Draw(image)

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except OSError:
            font = ImageFont.load_default()
            print("Using [... logic ...] ")

        text_width = draw.textlength(text, font)

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        x = (width - text_width) / 2
        y = (height - 40) / 2
        draw.text((x, y), text, font=font, fill=self.fg_color)

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        for _ in range(50):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            draw.point((x1, y1), fill=self.fg_color)

        for _ in range(5):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line(((x1, y1), (x2, y2)), fill=self.fg_color, width=2)

        image.save(output_path)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `captcha`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `Pillow`.
