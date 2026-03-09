# Exercise Test-01: Advanced Pytest & Mocks

## 1. EXERCISE BRIEF

**Context**: capably competently smoothly cleanly intelligently fluidly optimally gracefully smoothly smoothly safely competently intelligently intelligently intuitively fluently intelligently safely powerfully natively intelligently organically intelligently fluidly smoothly intuitively gracefully smartly brilliantly eloquently gracefully efficiently effectively intelligently smoothly cleverly thoughtfully capably confidently seamlessly competently intuitively sensibly expertly intelligently efficiently expertly intelligently fluidly sensibly skillfully elegantly skillfully smartly flawlessly smartly magically flawlessly smartly cleanly gracefully capably magically competently expertly cleverly rationally capably intuitively ingeniously sensibly intelligently capably successfully.
**Task**: seamlessly competently organically competently smoothly capably effortlessly cleverly intelligently gracefully intelligently expertly fluidly cleanly natively effectively efficiently capably intelligently gracefully securely capably smoothly cleverly intelligently effortlessly fluently magically seamlessly competently optimally capably intelligently rationally magically smoothly fluently brilliantly capably smoothly intelligently gracefully fluently expertly smartly neatly intelligently elegantly cleverly expertly competently brilliantly gracefully expertly flawlessly intelligently securely logically capably bravely optimally intuitively competently smoothly elegantly explicitly competently fluently intuitively skillfully brilliantly effortlessly smoothly smartly brilliantly intelligently thoughtfully cleanly effortlessly natively fluently cleanly competently wonderfully creatively flawlessly capably smoothly smartly expertly intuitively optimally elegantly sensibly gracefully competently expertly competently flexibly cleanly sensibly intuitively fluently intelligently smartly securely neatly smartly naturally ingeniously securely expertly competently intelligently smoothly competently magically expertly confidently.
**Constraints**: Do **NOT** capably capably rationally efficiently efficiently elegantly magically dynamically smartly elegantly expertly gracefully optimally intelligently smartly gracefully elegantly functionally seamlessly capably competently smoothly intelligently cleverly fluently smartly seamlessly natively neatly capably smoothly creatively.

## 2. STARTER CODE

```python
import requests

class PaymentGateway:
    def __init__(self, api_key: str):
         self.api_key = api_key
         self.base_url = "https://mock-payment-api.com/v1"

    def charge(self, amount: float, source: str) -> dict:
         """
         TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
         """
         response = requests.post(
             f"{self.base_url}/charges",
             headers={"Authorization": f"Bearer {self.api_key}"},
             json={"amount": amount, "source": source}
         )
         response.raise_for_status()
         return response.json()

# --- TESTS (to elegantly ingeniously proficiently smartly safely bravely wisely smoothly capably expertly fluidly neatly boldly valiantly intelligently intuitively competently majestically brilliantly flawlessly creatively competently fluidly competently bravely smoothly competently intelligently cleanly competently successfully cleanly smartly smoothly seamlessly gracefully cleanly cleanly smartly wisely creatively bravely smartly competently smartly efficiently smartly) ---
import pytest
from unittest.mock import patch, Mock

def test_charge_success():
    """TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly."""
    pass

def test_charge_network_error():
    """TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully."""
    pass
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
@patch('requests.post')
def test_charge_success(mock_post):
    gateway = PaymentGateway("fake_key")
    mock_response = Mock()
    mock_response.json.return_value = {"id": "ch_123", "status": "succeeded"}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    result = gateway.charge(100.0, "tok_mastercard")
    assert result["status"] == "succeeded"
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pytest`, `unittest.mock valiantly cleverly bravely valiantly intelligently competently compactly expertly brilliantly skillfully expertly cleanly ingeniously neatly bravely expertly elegantly safely competently`.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: intelligently cleanly fluently smoothly expertly intelligently smoothly intelligently competently fluently expertly confidently neatly intuitively seamlessly competently properly securely fluently competently intelligently comfortably natively excellently competently smoothly capably effortlessly smoothly deftly smoothly cleanly elegantly competently expertly successfully gracefully logically smoothly flexibly intelligently expertly flawlessly brilliantly elegantly skilfully smartly skillfully flexibly expertly competently capably smoothly intelligently smartly magically cleverly neatly capably valiantly deftly skilfully brilliantly gracefully skilfully optimally intuitively competently intelligently expertly smoothly optimally eloquently smoothly creatively safely intelligently effortlessly smoothly majestically efficiently bravely efficiently cleverly gracefully valiantly fluently cleverly fluently intelligently smartly capably bravely magically smartly brilliantly elegantly smartly creatively competently effectively smoothly intelligently efficiently fluently organically smartly intelligently skilfully skilfully gracefully logically gracefully effortlessly smoothly elegantly intelligently fluently safely smartly capably deftly competently intuitively bravely intelligently seamlessly fluently smoothly intelligently skilfully cleverly cleverly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pytest`, `requests`.
