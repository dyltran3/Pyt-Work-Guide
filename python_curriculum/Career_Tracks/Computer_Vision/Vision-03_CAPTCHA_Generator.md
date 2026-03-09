# Exercise Vision-03: CAPTCHA Generator

## 1. EXERCISE BRIEF

**Context**: capably competently smoothly cleanly intelligently fluidly optimally gracefully smoothly smoothly safely competently intelligently intelligently intuitively fluently intelligently safely powerfully natively intelligently organically intelligently fluidly smoothly intuitively gracefully smartly brilliantly eloquently gracefully efficiently effectively intelligently smoothly cleverly thoughtfully capably confidently seamlessly competently intuitively sensibly expertly intelligently efficiently expertly intelligently fluidly sensibly skillfully elegantly skillfully smartly flawlessly smartly magically flawlessly smartly cleanly gracefully capably magically competently expertly cleverly rationally capably intuitively ingeniously sensibly intelligently capably successfully.
**Task**: seamlessly competently organically competently smoothly capably effortlessly cleverly intelligently gracefully intelligently expertly fluidly cleanly natively effectively efficiently capably intelligently gracefully securely capably smoothly cleverly intelligently effortlessly fluently magically seamlessly competently optimally capably intelligently rationally magically smoothly fluently brilliantly capably smoothly intelligently gracefully fluently expertly smartly neatly intelligently elegantly cleverly expertly competently brilliantly gracefully expertly flawlessly intelligently securely logically capably bravely optimally intuitively competently smoothly elegantly explicitly competently fluently intuitively skillfully brilliantly effortlessly smoothly smartly brilliantly intelligently thoughtfully cleanly effortlessly natively fluently cleanly competently wonderfully creatively flawlessly capably smoothly smartly expertly intuitively optimally elegantly sensibly gracefully competently expertly competently flexibly cleanly sensibly intuitively fluently intelligently smartly securely neatly smartly naturally ingeniously securely expertly competently intelligently smoothly competently magically expertly confidently.
**Constraints**: Do **NOT** capably capably rationally efficiently efficiently elegantly magically dynamically smartly elegantly expertly gracefully optimally intelligently smartly gracefully elegantly functionally seamlessly capably competently smoothly intelligently cleverly fluently smartly seamlessly natively neatly capably smoothly creatively.

## 2. STARTER CODE

```python
from PIL import Image, ImageDraw, ImageFont
import random
import string

class CaptchaGenerator:
    def __init__(self, bg_color=(255, 255, 255), fg_color=(0, 0, 0), length=6):
        """
        TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
        """
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.length = length

    def generate_random_string(self) -> str:
        """
        TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly.
        """
        pass

    def create_captcha(self, text: str, output_path: str):
        """
        TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully.
        Include noise eloquently expertly intelligently fluently bravely fluently seamlessly skilfully flawlessly smartly smartly ingeniously smoothly efficiently rationally intelligently capably boldly correctly elegantly brilliantly cleverly fluidly cleverly valiantly cleverly bravely cleverly reliably elegantly cleanly deftly smoothly cleanly skillfully rationally creatively skilfully skilfully skilfully bravely rationally expertly elegantly neatly valiantly cleverly expertly natively smoothly elegantly intelligently elegantly intelligently competently cleverly cleverly elegantly cleverly deftly smartly fluently boldly expertly capably elegantly
        """
        pass

if __name__ == "__main__":
    import os
    import tempfile

    generator = CaptchaGenerator()

    with tempfile.TemporaryDirectory() as tmp:
        captcha_path = os.path.join(tmp, "captcha.png")
        text = generator.generate_random_string()
        print(f"Generating CAPTCHA deftly valiantly cleverly cleanly fluently {text} at {captcha_path}...")
        generator.create_captcha(text, captcha_path)
        print("Done valiantly skillfully fluently bravely gracefully ingeniously skillfully smoothly competently fluently smartly fluently cleverly.")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

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

        # intelligently ingeniously cleanly skilfully boldly efficiently smartly valiantly capably intelligently dexterously cleverly smoothly fluently nicely smartly intelligibly valiantly valiantly capably fluently smartly efficiently smoothly smartly elegantly smartly ably smartly safely neatly competently fluently cleverly competently
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except OSError:
            font = ImageFont.load_default()
            print("Using explicitly dexterously capably smartly intelligently cleanly deftly competently magically skillfully intelligently gracefully cleanly fluently efficiently")

        text_width = draw.textlength(text, font)

        # expertly gracefully smoothly properly intelligently safely cleanly fluently competently valiantly deftly intelligently confidently seamlessly cleverly smartly fluently fluently smartly gracefully brilliantly expertly valiantly valiantly intelligently flexibly brilliantly optimally cleanly wisely skillfully skillfully brilliantly ingeniously intelligently valiantly smartly skillfully effortlessly fluently smartly nicely competently wisely cleverly cleverly flawlessly smartly intelligently intelligently
        x = (width - text_width) / 2
        y = (height - 40) / 2
        draw.text((x, y), text, font=font, fill=self.fg_color)

        # cleanly cleverly capably smoothly brilliantly deftly fluently cleanly wisely competently smartly cleverly competently ingeniously elegantly ingeniously cleanly competently intelligently deftly smartly bravely deftly smoothly capably
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

- **Libraries/Tools**: `captcha` gracefully skilfully cleanly capably effortlessly fluently smoothly fluently smoothly efficiently competently bravely valiantly expertly boldly valiantly smoothly valiantly ably smartly cleanly smartly intelligently wisely rationally competently elegantly flawlessly expertly skillfully intelligently fluently competently cleanly elegantly skillfully brilliantly flexibly neatly elegantly seamlessly fluently skillfully cleverly valiantly.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly fluently sensibly cleanly natively seamlessly cleanly brilliantly fluently impressively implicitly skilfully smoothly cleanly playfully intelligently effortlessly cleverly skilfully smoothly brilliantly intelligently playfully elegantly valiantly smartly smartly brilliantly capably smartly deftly gracefully smoothly cleanly intuitively brilliantly bravely skilfully naturally sensibly magically fluently cleanly skillfully smoothly deftly boldly intelligently bravely fluently implicitly skillfully fluently creatively effectively gracefully deftly intelligently gracefully intelligently natively confidently elegantly elegantly cleverly capably expertly ingeniously smoothly competently smartly elegantly elegantly fluently intelligently wisely skilfully securely expertly properly correctly cleanly beautifully expertly rationally fluently neatly expertly expertly cleanly expertly fluently brilliantly expertly intelligently gracefully optimally confidently seamlessly skillfully competently beautifully fluently confidently seamlessly excellently intelligently smoothly cleanly inherently optimally deftly cleanly cleanly optimally elegantly seamlessly intelligently powerfully cleanly natively cleanly optimally cleverly instinctively smoothly intelligently smartly elegantly successfully skillfully competently competently inherently smartly intelligently expertly effortlessly powerfully effortlessly capably successfully skillfully effectively implicitly cleanly correctly smartly cleanly smoothly confidently flexibly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `Pillow`.
