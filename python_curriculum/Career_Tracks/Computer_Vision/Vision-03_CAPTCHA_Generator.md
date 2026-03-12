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
    def __init__(self, bg_color=(255, 255, 255), fg_color=(0, 0, 0), length=6, font_path="arial.ttf"):
        """
        Initializes the CAPTCHA generator with background color, foreground color,
        CAPTCHA text length, and font path.
        """
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.length = length
        self.font_path = font_path

    def generate_random_string(self) -> str:
        """
        Generates a random string of alphanumeric characters for the CAPTCHA.
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=self.length))

    def create_captcha(self, text: str, output_path: str):
        """
        Generates a CAPTCHA image with the given text, including noise and distortions,
        and saves it to the specified output path.
        """
        width, height = 200, 80
        image = Image.new('RGB', (width, height), self.bg_color)
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(self.font_path, 40)
        except OSError:
            font = ImageFont.load_default()
            print(f"Warning: Font '{self.font_path}' not found. Using default font.")

        text_width = draw.textlength(text, font)
        text_height = font.getbbox(text)[3] - font.getbbox(text)[1] # Get actual text height

        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, font=font, fill=self.fg_color)

        # Add noise points
        for _ in range(50):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            draw.point((x1, y1), fill=self.fg_color)

        # Add noise lines
        for _ in range(5):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line(((x1, y1), (x2, y2)), fill=self.fg_color, width=2)

        image.save(output_path)

if __name__ == "__main__":
    import os
    import tempfile

    generator = CaptchaGenerator()

    with tempfile.TemporaryDirectory() as tmp:
        captcha_path = os.path.join(tmp, "captcha.png")
        text = generator.generate_random_string()
        print(f"Generating CAPTCHA for text: {text} at {captcha_path}...")
        generator.create_captcha(text, captcha_path)
        print("Done!")
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
            print("Using default font.")

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
