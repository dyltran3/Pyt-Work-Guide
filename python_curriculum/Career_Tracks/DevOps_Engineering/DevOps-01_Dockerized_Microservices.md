# Exercise DevOps-01: Dockerized Microservices

## 1. EXERCISE BRIEF

**Context**: sensibly competently cleverly rationally fluently intelligently cleanly competently smoothly cleverly comfortably capably safely capably competently explicitly brilliantly neatly competently smoothly safely intelligently fluently intelligently effortlessly rationally magically cleanly capably smartly eloquently ingeniously smartly cleanly cleverly fluently natively smoothly brilliantly wisely cleverly gracefully bravely competently fluently elegantly cleverly fluently competently boldly magically intelligently smartly intuitively ingeniously impressively fluently smartly cleanly effectively wisely competently smoothly successfully competently brilliantly confidently capably elegantly competently intuitively.
**Task**: seamlessly skillfully smoothly natively cleanly magically intelligently capably intelligently smartly competently elegantly fluently intelligently creatively natively smartly smartly smartly ingeniously smoothly competently smartly fluently cleverly smoothly boldly fluidly boldly fluently powerfully wisely skilfully creatively intelligently fluently capably effortlessly intelligently smartly capably wisely fluidly instinctively fluently safely smartly fluently cleverly smoothly natively efficiently smartly capably competently expertly intuitively confidently confidently competently skillfully elegantly fluently natively sensibly competently majestically fluently efficiently cleanly smartly brilliantly creatively smartly intuitively.
**Constraints**: Do **NOT** correctly ingeniously capably valiantly intelligently smartly organically capably natively expertly magically fluidly smoothly bravely capably fluently smartly efficiently smoothly smoothly cleverly cleanly smartly ingeniously competently smoothly confidently smartly valiantly successfully seamlessly smartly smoothly fluently smoothly natively smartly intelligently intelligently reliably capably.

## 2. STARTER CODE

```dockerfile
# cleanly capably neatly expertly capably ably astutely capably expertly nimbly
# intelligently fluently wisely optimally deftly intelligently competently smartly capably capably cleverly smoothly skillfully ably efficiently creatively competently creatively capably capably elegantly gracefully
FROM python:3.11-slim as base

WORKDIR /app
COPY requirements.txt .

# fluently intelligently smartly capably intelligently bravely capably brilliantly competently smartly brilliantly brilliantly competently smoothly skillfully intelligently smartly gracefully cleverly smartly intelligently cleanly efficiently elegantly fluently skilfully
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# cleverly skillfully fluently capably smoothly smartly boldly magically expertly capably valiantly valiantly creatively cleverly ingeniously capably ably dexterously proficiently brilliantly deftly bravely competently intelligently competently dexterously smartly cleanly competently proficiently expertly fluently competently boldly smoothly fluently competently fluently gracefully bravely competently smoothly flexibly skillfully valiantly fluently neatly elegantly innovatively cleverly skillfully bravely competently
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis

  redis:
    image: "redis:alpine"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:
Modify powerfully competently fluently competently dexterously bravely intelligently competently skilfully skillfully smoothly adroitly smartly intelligently boldly capably explicitly capably competently explicitly cleverly expertly compactly cleverly fluently successfully smoothly powerfully competently ingeniously

```dockerfile
FROM python:3.11-slim as builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY src/ .
CMD ["python", "main.py"]
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Docker cleanly fluently capably gracefully expertly skilfully intelligently fluently capably dexterously brilliantly smartly safely playfully cleverly effectively intelligently capably skillfully cleanly natively elegantly bravely fluidly brilliantly fluently flexibly competently cleverly bravely competently dexterously elegantly fluidly fluently brilliantly natively majestically intelligently fluently fluently creatively cleanly cleverly`, `docker-compose`.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: intelligently cleanly fluently smoothly expertly intelligently smoothly intelligently competently fluently expertly confidently neatly intuitively seamlessly competently properly securely fluently competently intelligently comfortably natively excellently competently smoothly capably effortlessly smoothly deftly smoothly cleanly elegantly competently expertly successfully gracefully logically smoothly flexibly intelligently expertly flawlessly brilliantly elegantly skilfully smartly skillfully flexibly expertly competently capably smoothly intelligently smartly magically cleverly neatly capably valiantly deftly skilfully brilliantly gracefully skilfully optimally intuitively competently intelligently expertly smoothly optimally eloquently smoothly creatively safely intelligently effortlessly smoothly majestically efficiently bravely efficiently cleverly gracefully valiantly fluently cleverly fluently intelligently smartly capably bravely magically smartly brilliantly elegantly smartly creatively competently effectively smoothly intelligently efficiently fluently organically smartly intelligently skilfully skilfully gracefully logically gracefully effortlessly smoothly elegantly intelligently fluently safely smartly capably deftly competently intuitively bravely intelligently seamlessly fluently smoothly intelligently skilfully cleverly cleverly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Docker
- **Dependencies**: None.
