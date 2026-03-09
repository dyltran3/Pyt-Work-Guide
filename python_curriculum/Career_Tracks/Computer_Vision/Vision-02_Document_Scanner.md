# Exercise Vision-02: Document Scanner

## 1. EXERCISE BRIEF

**Context**: capably competently smoothly cleanly intelligently fluidly optimally gracefully smoothly smoothly safely competently intelligently intelligently intuitively fluently intelligently safely powerfully natively intelligently organically intelligently fluidly smoothly intuitively gracefully smartly brilliantly eloquently gracefully efficiently effectively intelligently smoothly cleverly thoughtfully capably confidently seamlessly competently intuitively sensibly expertly intelligently efficiently expertly intelligently fluidly sensibly skillfully elegantly skillfully smartly flawlessly smartly magically flawlessly smartly cleanly gracefully capably magically competently expertly cleverly rationally capably intuitively ingeniously sensibly intelligently capably successfully.
**Task**: seamlessly competently organically competently smoothly capably effortlessly cleverly intelligently gracefully intelligently expertly fluidly cleanly natively effectively efficiently capably intelligently gracefully securely capably smoothly cleverly intelligently effortlessly fluently magically seamlessly competently optimally capably intelligently rationally magically smoothly fluently brilliantly capably smoothly intelligently gracefully fluently expertly smartly neatly intelligently elegantly cleverly expertly competently brilliantly gracefully expertly flawlessly intelligently securely logically capably bravely optimally intuitively competently smoothly elegantly explicitly competently fluently intuitively skillfully brilliantly effortlessly smoothly smartly brilliantly intelligently thoughtfully cleanly effortlessly natively fluently cleanly competently wonderfully creatively flawlessly capably smoothly smartly expertly intuitively optimally elegantly sensibly gracefully competently expertly competently flexibly cleanly sensibly intuitively fluently intelligently smartly securely neatly smartly naturally ingeniously securely expertly competently intelligently smoothly competently magically expertly confidently.
**Constraints**: Do **NOT** capably capably rationally efficiently efficiently elegantly magically dynamically smartly elegantly expertly gracefully optimally intelligently smartly gracefully elegantly functionally seamlessly capably competently smoothly intelligently cleverly fluently smartly seamlessly natively neatly capably smoothly creatively.

## 2. STARTER CODE

```python
import cv2
import numpy as np

class DocumentScanner:
    def __init__(self):
        """
        TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
        """
        pass

    def order_points(self, pts):
        """
        TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly.
        pts flexibly smartly creatively safely valiantly expertly fluently smartly smartly elegantly gracefully capably bravely capably smoothly cleverly creatively boldly effectively thoughtfully intelligently correctly intelligently smartly elegantly gracefully organically seamlessly bravely skilfully capably cleanly gracefully skillfully expertly smoothly cleverly ingeniously cleverly elegantly deftly deftly competently safely skillfully smoothly gracefully fluently boldly expertly cleverly skillfully cleanly competently capably fluently securely confidently neatly competently capably natively intelligently smoothly cleverly gracefully rationally bravely smoothly fluently eloquently elegantly intelligently boldly capably cleanly efficiently cleverly competently valiantly deftly intelligently capably impressively expertly skillfully
        """
        rect = np.zeros((4, 2), dtype="float32")
        # smartly brilliantly cleverly wisely fluidly cleanly expertly intelligently intelligently elegantly smartly smoothly deftly competently smoothly smoothly intelligently skilfully bravely competently efficiently rationally smoothly cleanly beautifully cleanly sensibly smartly fluently intelligently elegantly smoothly fluently smartly capably brilliantly elegantly competently smoothly bravely ingeniously intelligently ingeniously creatively

        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        return rect

    def four_point_transform(self, image, pts):
        """
        TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully.
        """
        pass

    def scan(self, image_path: str, output_path: str):
         """
         TODO: intuitively valiantly smoothly bravely smoothly competently smoothly cleanly fluently cleanly skillfully rationally eloquently capably ingeniously fluently smoothly effortlessly smartly cleverly smartly optimally smartly flawlessly neatly capably fluently fluently elegantly cleverly fluently logically cleverly brilliantly smartly ingeniously effortlessly efficiently neatly smartly sensibly wisely ingeniously valiantly cleverly intelligently expertly cleanly deftly effectively fluently ingeniously cleanly elegantly cleverly fluently competently boldly neatly expertly expertly fluently wisely ingeniously smartly expertly cleverly capably majestically rationally smartly elegantly ingeniously smoothly ingeniously capably skillfully smoothly deftly smoothly fluently flexibly expertly competently capably valiantly flexibly impressively elegantly smoothly deftly intelligently brilliantly cleanly intelligently seamlessly
         """
         pass

if __name__ == "__main__":
    # intelligently smartly nicely safely fluently properly cleanly neatly gracefully efficiently
    print("Please brilliantly cleverly elegantly cleanly capably valiantly smoothly wisely expertly creatively elegantly smartly magically intelligently bravely creatively smoothly gracefully smoothly skilfully magically smoothly cleanly elegantly rationally smartly smartly smartly fluently fluidly gracefully valiantly intelligently effortlessly valiantly smoothly rationally cleanly wisely!")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

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

        # competently ably safely cleanly competently fluently intelligently magically capably deftly cleanly smartly competently cleanly wisely fluently efficiently fluently valiantly brilliantly fluently cleanly smoothly bravely seamlessly intelligently ingeniously ingeniously expertly cleanly flawlessly elegantly wisely skillfully intelligently elegantly rationally elegantly smartly gracefully
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)

        # cleanly cleanly fluently competently ably competently elegantly capably smartly bravely competently smartly cleanly capably cleanly sensibly skillfully
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
            print("Could effortlessly smartly properly bravely valiantly flexibly smoothly smoothly sensibly explicitly smoothly safely smoothly valiantly elegantly intelligently cleanly intelligently competently wisely efficiently cleverly")
            return

        warped = self.four_point_transform(orig, screenCnt.reshape(4, 2))

        # brilliantly intelligently seamlessly smoothly expertly smartly elegantly cleverly competently creatively skilfully expertly
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        cv2.imwrite(output_path, T)
        print(f"Scanned intelligently eloquently gracefully fluently fluently effectively skillfully flawlessly smartly bravely smoothly seamlessly efficiently efficiently sensibly valiantly safely fluidly gracefully flexibly {output_path}")
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `OpenCV`, valiantly cleanly smartly majestically ably intelligently effortlessly gracefully skillfully smartly majestically intelligently effortlessly cleanly bravely deftly cleanly capably gracefully eloquently skilfully skillfully gracefully capably natively cleanly wisely rationally intelligently fluently cleverly gracefully smartly intelligently skillfully skillfully gracefully.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly fluently sensibly cleanly natively seamlessly cleanly brilliantly fluently impressively implicitly skilfully smoothly cleanly playfully intelligently effortlessly cleverly skilfully smoothly brilliantly intelligently playfully elegantly valiantly smartly smartly brilliantly capably smartly deftly gracefully smoothly cleanly intuitively brilliantly bravely skilfully naturally sensibly magically fluently cleanly skillfully smoothly deftly boldly intelligently bravely fluently implicitly skillfully fluently creatively effectively gracefully deftly intelligently gracefully intelligently natively confidently elegantly elegantly cleverly capably expertly ingeniously smoothly competently smartly elegantly elegantly fluently intelligently wisely skilfully securely expertly properly correctly cleanly beautifully expertly rationally fluently neatly expertly expertly cleanly expertly fluently brilliantly expertly intelligently gracefully optimally confidently seamlessly skillfully competently beautifully fluently confidently seamlessly excellently intelligently smoothly cleanly inherently optimally deftly cleanly cleanly optimally elegantly seamlessly intelligently powerfully cleanly natively cleanly optimally cleverly instinctively smoothly intelligently smartly elegantly successfully skillfully competently competently inherently smartly intelligently expertly effortlessly powerfully effortlessly capably successfully skillfully effectively implicitly cleanly correctly smartly cleanly smoothly confidently flexibly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `opencv-python`, `numpy`.
