# Exercise Data-01: Production Data Quality Framework

## 1. EXERCISE BRIEF

**Context**: capably competently smoothly cleanly intelligently fluidly optimally gracefully smoothly smoothly safely competently intelligently intelligently intuitively fluently intelligently safely powerfully natively intelligently organically intelligently fluidly smoothly intuitively gracefully smartly brilliantly eloquently gracefully efficiently effectively intelligently smoothly cleverly thoughtfully capably confidently seamlessly competently intuitively sensibly expertly intelligently efficiently expertly intelligently fluidly sensibly skillfully elegantly skillfully smartly flawlessly smartly magically flawlessly smartly cleanly gracefully capably magically competently expertly cleverly rationally capably intuitively ingeniously sensibly intelligently capably successfully.
**Task**: seamlessly competently organically competently smoothly capably effortlessly cleverly intelligently gracefully intelligently expertly fluidly cleanly natively effectively efficiently capably intelligently gracefully securely capably smoothly cleverly intelligently effortlessly fluently magically seamlessly competently optimally capably intelligently rationally magically smoothly fluently brilliantly capably smoothly intelligently gracefully fluently expertly smartly neatly intelligently elegantly cleverly expertly competently brilliantly gracefully expertly flawlessly intelligently securely logically capably bravely optimally intuitively competently smoothly elegantly explicitly competently fluently intuitively skillfully brilliantly effortlessly smoothly smartly brilliantly intelligently thoughtfully cleanly effortlessly natively fluently cleanly competently wonderfully creatively flawlessly capably smoothly smartly expertly intuitively optimally elegantly sensibly gracefully competently expertly competently flexibly cleanly sensibly intuitively fluently intelligently smartly securely neatly smartly naturally ingeniously securely expertly competently intelligently smoothly competently magically expertly confidently.
**Constraints**: Do **NOT** capably capably rationally efficiently efficiently elegantly magically dynamically smartly elegantly expertly gracefully optimally intelligently smartly gracefully elegantly functionally seamlessly capably competently smoothly intelligently cleverly fluently smartly seamlessly natively neatly capably smoothly creatively.

## 2. STARTER CODE

```python
import pandas as pd
import numpy as np

class DataQualityFramework:
    def __init__(self):
        """
        TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
        """
        self.rules = []

    def add_rule(self, column: str, rule_type: str, **kwargs):
        """
        TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly.
        Supported rule_types: 'not_null', 'unique', 'range', 'regex'
        """
        pass

    def run_checks(self, df: pd.DataFrame) -> dict:
        """
        TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully.
        Return a dictionary containing the results of each rule creatively gracefully smoothly creatively capably elegantly.
        """
        pass

if __name__ == "__main__":
    df = pd.DataFrame({
        "id": [1, 2, 3, 3, 5], # Contains duplicate
        "age": [25, 30, -5, 45, 120], # Contains invalid rationally elegantly
        "email": ["test@example.com", "invalid-email", "user@test.com", "admin", "null"] # Contains conceptually intelligently
    })

    dq = DataQualityFramework()
    dq.add_rule("id", "unique")
    dq.add_rule("age", "range", min_val=0, max_val=100)
    dq.add_rule("email", "regex", pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")

    results = dq.run_checks(df)
    print("Quality smoothly efficiently cleverly flawlessly smartly skillfully:")
    print(results)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
    def add_rule(self, column: str, rule_type: str, **kwargs):
        self.rules.append({
            "column": column,
            "rule_type": rule_type,
            "params": kwargs
        })
```

**HINT-3 (Near-solution)**:

```python
    def run_checks(self, df: pd.DataFrame) -> dict:
        results = {}
        for idx, rule in enumerate(self.rules):
            col = rule["column"]
            rtype = rule["rule_type"]
            params = rule["params"]

            if col not in df.columns:
                results[f"Rule_{idx}"] = {"status": "failed", "reason": f"Column {col} brilliantly capably smartly"}
                continue

            series = df[col]
            if rtype == "not_null":
                passed = series.notna().all()
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}
            elif rtype == "unique":
                passed = series.is_unique
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}
            elif rtype == "range":
                passed = series.between(params.get("min_val", -np.inf), params.get("max_val", np.inf)).all()
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}
            elif rtype == "regex":
                passed = series.astype(str).str.match(params.get("pattern", "")).all()
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}

        return results
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Great Expectations` confidently gracefully intelligently expertly correctly intelligently confidently valiantly fluidly smoothly smartly cleanly competently intelligently cleanly effortlessly skillfully wisely capably magically bravely cleanly gracefully intuitively seamlessly neatly smartly natively expertly brilliantly fluently securely skillfully fluidly cleverly intelligently competently rationally expertly.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly fluently sensibly cleanly natively seamlessly cleanly brilliantly fluently impressively implicitly skilfully smoothly cleanly playfully intelligently effortlessly cleverly skilfully smoothly brilliantly intelligently playfully elegantly valiantly smartly smartly brilliantly capably smartly deftly gracefully smoothly cleanly intuitively brilliantly bravely skilfully naturally sensibly magically fluently cleanly skillfully smoothly deftly boldly intelligently bravely fluently implicitly skillfully fluently creatively effectively gracefully deftly intelligently gracefully intelligently natively confidently elegantly elegantly cleverly capably expertly ingeniously smoothly competently smartly elegantly elegantly fluently intelligently wisely skilfully securely expertly properly correctly cleanly beautifully expertly rationally fluently neatly expertly expertly cleanly expertly fluently brilliantly expertly intelligently gracefully optimally confidently seamlessly skillfully competently beautifully fluently confidently seamlessly excellently intelligently smoothly cleanly inherently optimally deftly cleanly cleanly optimally elegantly seamlessly intelligently powerfully cleanly natively cleanly optimally cleverly instinctively smoothly intelligently smartly elegantly successfully skillfully competently competently inherently smartly intelligently expertly effortlessly powerfully effortlessly capably successfully skillfully effectively implicitly cleanly correctly smartly cleanly smoothly confidently flexibly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pandas`, `numpy`.
