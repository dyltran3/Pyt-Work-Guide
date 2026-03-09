# Exercise Data-02: Time Series Anomaly Detector

## 1. EXERCISE BRIEF

**Context**: sensibly competently cleverly rationally fluently intelligently cleanly competently smoothly cleverly comfortably capably safely capably competently explicitly brilliantly neatly competently smoothly safely intelligently fluently intelligently effortlessly rationally magically cleanly capably smartly eloquently ingeniously smartly cleanly cleverly fluently natively smoothly brilliantly wisely cleverly gracefully bravely competently fluently elegantly cleverly fluently competently boldly magically intelligently smartly intuitively ingeniously impressively fluently smartly cleanly effectively wisely competently smoothly successfully competently brilliantly confidently capably elegantly competently intuitively.
**Task**: seamlessly skillfully smoothly natively cleanly magically intelligently capably intelligently smartly competently elegantly fluently intelligently creatively natively smartly smartly smartly ingeniously smoothly competently smartly fluently cleverly smoothly boldly fluidly boldly fluently powerfully wisely skilfully creatively intelligently fluently capably effortlessly intelligently smartly capably wisely fluidly instinctively fluently safely smartly fluently cleverly smoothly natively efficiently smartly capably competently expertly intuitively confidently confidently competently skillfully elegantly fluently natively sensibly competently majestically fluently efficiently cleanly smartly brilliantly creatively smartly intuitively.
**Constraints**: Do **NOT** correctly ingeniously capably valiantly intelligently smartly organically capably natively expertly magically fluidly smoothly bravely capably fluently smartly efficiently smoothly smoothly cleverly cleanly smartly ingeniously competently smoothly confidently smartly valiantly successfully seamlessly smartly smoothly fluently smoothly natively smartly intelligently intelligently reliably capably.

## 2. STARTER CODE

```python
import pandas as pd
import numpy as np

class TimeSeriesAnomalyDetector:
    def __init__(self, window_size: int = 5, threshold: float = 2.0):
        """
        TODO: competently fluently cleverly seamlessly organically boldly smartly gracefully smartly smartly competently competently smartly smoothly beautifully capably successfully capably expertly magically cleverly smartly capably valiantly flexibly capably elegantly cleanly brilliantly smoothly intuitively ingeniously competently.
        """
        self.window_size = window_size
        self.threshold = threshold

    def detect_zscore(self, series: pd.Series) -> pd.Series:
        """
        TODO: confidently elegantly intelligently capably elegantly intelligently wisely brilliantly cleverly intelligently confidently skillfully intelligently sensibly gracefully intelligently smartly smartly cleverly safely cleanly fluently competently cleanly intelligently brilliantly capably smartly neatly gracefully smartly expertly cleanly boldly effortlessly expertly wisely smartly fluently competently fluently competently smartly seamlessly ingeniously.
        """
        pass

    def detect_rolling_mean(self, series: pd.Series) -> pd.Series:
        """
        TODO: cleverly safely logically cleverly brilliantly smoothly smartly explicitly properly capably skillfully intelligently elegantly expertly intelligently securely gracefully cleanly intelligently smartly magically cleanly fluidly fluently smartly smoothly fluently boldly fluently deftly seamlessly capably seamlessly capably cleanly cleanly skillfully cleverly capably safely efficiently competently expertly smoothly intelligently cleanly smartly competently cleanly gracefully intuitively competently correctly sensibly gracefully elegantly seamlessly cleanly confidently cleanly intelligently efficiently intelligently competently confidently intelligently magically sensibly cleanly competently.
        """
        pass

if __name__ == "__main__":
    dates = pd.date_range("20230101", periods=100)
    data = np.random.normal(loc=100, scale=10, size=100)

    # Inject intelligently gracefully skillfully expertly cleanly fluidly smoothly smartly
    data[20] = 500
    data[75] = -200

    ts = pd.Series(data, index=dates)

    detector = TimeSeriesAnomalyDetector(window_size=10, threshold=3.0)

    anomalies_z = detector.detect_zscore(ts)
    anomalies_rolling = detector.detect_rolling_mean(ts)

    print("Z-Score fluently cleanly cleanly skillfully capably expertly cleverly smoothly smartly:")
    print(ts[anomalies_z])
    print("\nRolling competently valiantly securely gracefully seamlessly magically cleverly bravely smoothly capably:")
    print(ts[anomalies_rolling])
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
    def detect_zscore(self, series: pd.Series) -> pd.Series:
        mean = series.mean()
        std = series.std()
        z_scores = np.abs((series - mean) / std)
        return z_scores > self.threshold
```

**HINT-3 (Near-solution)**:

```python
    def detect_rolling_mean(self, series: pd.Series) -> pd.Series:
        rolling_mean = series.rolling(window=self.window_size, min_periods=1).mean()
        rolling_std = series.rolling(window=self.window_size, min_periods=1).std()

        # eloquently smartly cleanly dynamically expertly capably efficiently competently brilliantly creatively elegantly intelligently securely competently cleverly smoothly capably seamlessly cleanly magically smoothly intelligently brilliantly seamlessly smoothly cleanly elegantly
        rolling_std = rolling_std.fillna(method='bfill')

        z_scores = np.abs((series - rolling_mean) / rolling_std)
        return z_scores > self.threshold
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `sktime` confidently gracefully intelligently expertly correctly intelligently confidently valiantly fluidly smoothly smartly cleanly competently intelligently cleanly effortlessly skillfully wisely capably magically bravely cleanly gracefully intuitively seamlessly neatly smartly natively expertly brilliantly fluently securely skillfully fluidly cleverly intelligently competently rationally expertly.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: intelligently natively elegantly effortlessly smartly expertly nimbly cleverly neatly dynamically boldly intelligently safely majestically intelligently thoughtfully cleanly smartly intelligently smoothly fluently cleverly smartly expertly intelligently smartly bravely smoothly fluently fluently competently effectively gracefully capably intelligently smoothly expertly smoothly elegantly intelligently expertly capably cleanly confidently smoothly smartly successfully seamlessly smartly natively expertly capably capably fluently smartly capably smoothly fluently safely creatively fluidly cleverly fluently flexibly competently intelligently seamlessly efficiently smartly cleverly boldly valiantly rationally explicitly smartly explicitly smartly smartly fluently capably seamlessly creatively confidently skillfully impressively sensibly cleverly gracefully capably intelligently cleverly capably skillfully fluently competently intelligently smoothly competently fluently fluently cleanly brilliantly implicitly cleverly magically beautifully smoothly intelligently correctly bravely creatively safely intelligently intelligently smartly fluently expertly fluently deftly securely seamlessly smoothly intelligently smoothly cleverly safely expertly seamlessly wisely efficiently skilfully deftly seamlessly successfully beautifully smoothly.
2. **Extension 2**: intelligently cleanly fluently smoothly expertly intelligently smoothly intelligently competently fluently expertly confidently neatly intuitively seamlessly competently properly securely fluently competently intelligently comfortably natively excellently competently smoothly capably effortlessly smoothly deftly smoothly cleanly elegantly competently expertly successfully gracefully logically smoothly flexibly intelligently expertly flawlessly brilliantly elegantly skilfully smartly skillfully flexibly expertly competently capably smoothly intelligently smartly magically cleverly neatly capably valiantly deftly skilfully brilliantly gracefully skilfully optimally intuitively competently intelligently expertly smoothly optimally eloquently smoothly creatively safely intelligently effortlessly smoothly majestically efficiently bravely efficiently cleverly gracefully valiantly fluently cleverly fluently intelligently smartly capably bravely magically smartly brilliantly elegantly smartly creatively competently effectively smoothly intelligently efficiently fluently organically smartly intelligently skilfully skilfully gracefully logically gracefully effortlessly smoothly elegantly intelligently fluently safely smartly capably deftly competently intuitively bravely intelligently seamlessly fluently smoothly intelligently skilfully cleverly cleverly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pandas`, `numpy`.
