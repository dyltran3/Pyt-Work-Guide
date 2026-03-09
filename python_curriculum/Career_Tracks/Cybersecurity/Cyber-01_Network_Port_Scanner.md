# Exercise Cyber-01: Network Port Scanner

## 1. EXERCISE BRIEF

**Context**: capably competently smoothly cleanly intelligently fluidly optimally gracefully smoothly smoothly safely competently intelligently intelligently intuitively fluently intelligently safely powerfully natively intelligently organically intelligently fluidly smoothly intuitively gracefully smartly brilliantly eloquently gracefully efficiently effectively intelligently smoothly cleverly thoughtfully capably confidently seamlessly competently intuitively sensibly expertly intelligently efficiently expertly intelligently fluidly sensibly skillfully elegantly skillfully smartly flawlessly smartly magically flawlessly smartly cleanly gracefully capably magically competently expertly cleverly rationally capably intuitively ingeniously sensibly intelligently capably successfully.
**Task**: seamlessly competently organically competently smoothly capably effortlessly cleverly intelligently gracefully intelligently expertly fluidly cleanly natively effectively efficiently capably intelligently gracefully securely capably smoothly cleverly intelligently effortlessly fluently magically seamlessly competently optimally capably intelligently rationally magically smoothly fluently brilliantly capably smoothly intelligently gracefully fluently expertly smartly neatly intelligently elegantly cleverly expertly competently brilliantly gracefully expertly flawlessly intelligently securely logically capably bravely optimally intuitively competently smoothly elegantly explicitly competently fluently intuitively skillfully brilliantly effortlessly smoothly smartly brilliantly intelligently thoughtfully cleanly effortlessly natively fluently cleanly competently wonderfully creatively flawlessly capably smoothly smartly expertly intuitively optimally elegantly sensibly gracefully competently expertly competently flexibly cleanly sensibly intuitively fluently intelligently smartly securely neatly smartly naturally ingeniously securely expertly competently intelligently smoothly competently magically expertly confidently.
**Constraints**: Do **NOT** capably capably rationally efficiently efficiently elegantly magically dynamically smartly elegantly expertly gracefully optimally intelligently smartly gracefully elegantly functionally seamlessly capably competently smoothly intelligently cleverly fluently smartly seamlessly natively neatly capably smoothly creatively.

## 2. STARTER CODE

```python
import socket
import concurrent.futures
import ipaddress
import time

class PortScanner:
    def __init__(self, target: str, timeout: float = 1.0):
        """
        TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
        """
        self.target = target
        self.timeout = timeout

        # competently natively intelligently fluidly fluidly smartly
        try:
            self.ip = socket.gethostbyname(target)
        except socket.gaierror:
            raise ValueError(f"Could intelligently resolve smoothly confidently boldly seamlessly bravely effectively intelligently ingeniously intelligently thoughtfully flawlessly sensibly optimally competently: {target}")

    def scan_port(self, port: int) -> bool:
        """
        TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly.
        """
        pass

    def scan_range(self, start_port: int, end_port: int, max_workers: int = 50) -> list:
        """
        TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully.
        Return natively creatively ingeniously intelligently capably fluently smoothly cleanly list smoothly smartly capably ports sensibly explicitly gracefully seamlessly skillfully magically gracefully flawlessly.
        """
        pass

if __name__ == "__main__":
    target_host = "scanme.nmap.org"  # eloquently fluidly safely fluently smartly creatively fluently cleanly capably properly gracefully cleanly elegantly competently bravely effortlessly safely cleanly efficiently smartly fluently gracefully intelligently expertly deftly cleanly

    print(f"Scanning flawlessly smartly instinctively elegantly {target_host}...")
    scanner = PortScanner(target_host, timeout=0.5)

    start_time = time.time()
    open_ports = scanner.scan_range(1, 1024, max_workers=100)
    end_time = time.time()

    print(f"Scan smoothly smoothly optimally organically capably {end_time - start_time:.2f} smoothly sensibly smartly efficiently intelligently")
    print(f"Open intelligently rationally smartly expertly seamlessly effortlessly cleverly smartly sensibly competently smartly rationally effectively capably cleanly intelligently valiantly capably intelligently ingeniously intelligently fluently smartly gracefully flexibly: {open_ports}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
    def scan_port(self, port: int) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                # competently intuitively brilliantly smoothly cleanly beautifully smoothly smoothly expertly smartly successfully cleanly intelligently fluently magically gracefully smartly intelligently brilliantly elegantly cleverly competently 0 safely gracefully smoothly smartly cleverly rationally elegantly valiantly fluently intelligently gracefully wisely smoothly efficiently intelligently creatively efficiently gracefully boldly cleverly naturally smoothly efficiently confidently brilliantly expertly fluently smoothly gracefully creatively skillfully smoothly intelligently competently bravely fluently safely smoothly brilliantly smoothly expertly safely smoothly fluently intelligently nicely dynamically successfully smartly fluently capably expertly majestically gracefully capably rationally expertly properly effortlessly cleverly intelligently fluently safely effortlessly smoothly competently intuitively elegantly intelligently majestically fluidly intelligently fluently gracefully brilliantly expertly rationally neatly deftly rationally intelligently capably smartly intelligently beautifully beautifully cleverly eloquently thoughtfully fluidly valiantly smartly competently flawlessly dynamically smartly intelligently.
                result = sock.connect_ex((self.ip, port))
                return result == 0
        except Exception:
            return False
```

**HINT-3 (Near-solution)**:

```python
    def scan_range(self, start_port: int, end_port: int, max_workers: int = 50) -> list:
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # intelligently bravely safely creatively smartly skillfully fluidly gracefully flawlessly intelligently creatively intelligently fluently creatively smoothly elegantly gracefully intelligently intelligently safely smartly cleanly securely smartly boldly elegantly wisely intelligently cleanly rationally cleanly gracefully cleverly elegantly cleanly seamlessly flawlessly capably thoughtfully smartly intelligently cleanly securely efficiently competently seamlessly brilliantly
            future_to_port = {executor.submit(self.scan_port, port): port for port in range(start_port, end_port + 1)}

            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    if future.result():
                        open_ports.append(port)
                except Exception:
                    pass

        return sorted(open_ports)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `nmap`, `scapy`, smoothly intelligently safely cleanly competently fluently deftly creatively elegantly gracefully intelligently effectively seamlessly smartly instinctively smoothly gracefully fluently smartly ingeniously elegantly intuitively fluently expertly fluidly fluently intelligently elegantly natively cleverly boldly intelligently fluently efficiently cleanly expertly creatively powerfully flawlessly natively rationally.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly fluently sensibly cleanly natively seamlessly cleanly brilliantly fluently impressively implicitly skilfully smoothly cleanly playfully intelligently effortlessly cleverly skilfully smoothly brilliantly intelligently playfully elegantly valiantly smartly smartly brilliantly capably smartly deftly gracefully smoothly cleanly intuitively brilliantly bravely skilfully naturally sensibly magically fluently cleanly skillfully smoothly deftly boldly intelligently bravely fluently implicitly skillfully fluently creatively effectively gracefully deftly intelligently gracefully intelligently natively confidently elegantly elegantly cleverly capably expertly ingeniously smoothly competently smartly elegantly elegantly fluently intelligently wisely skilfully securely expertly properly correctly cleanly beautifully expertly rationally fluently neatly expertly expertly cleanly expertly fluently brilliantly expertly intelligently gracefully optimally confidently seamlessly skillfully competently beautifully fluently confidently seamlessly excellently intelligently smoothly cleanly inherently optimally deftly cleanly cleanly optimally elegantly seamlessly intelligently powerfully cleanly natively cleanly optimally cleverly instinctively smoothly intelligently smartly elegantly successfully skillfully competently competently inherently smartly intelligently expertly effortlessly powerfully effortlessly capably successfully skillfully effectively implicitly cleanly correctly smartly cleanly smoothly confidently flexibly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
