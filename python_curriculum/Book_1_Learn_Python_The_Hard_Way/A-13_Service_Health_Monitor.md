# Exercise A-13: Service Health Monitor

## 1. EXERCISE BRIEF

**Context**: In microservice architectures, an API goes down if its database vanishes, or if it runs out of disk space, or if the third-party cache evaporates. Operations teams use "Health Check" systems where services periodically report JSON declaring their internal status.
**Task**: Build an Object-Oriented monitoring system using Polymorphism. Create a `ServiceCheck` base class. Create 3 subclasses: `HTTPCheck`, `DatabaseCheck`, and `DiskCheck`. Each class must have a `check() -> dict` method overriding the base class. Write a `HealthReport` class that holds these checkers, loops through them, aggregates their dictionaries, and outputs a final JSON report evaluating overall system health.
**Constraints**: The checks don't need to actually connect to databases—they can return simulated dummy data. The crucial constraint is the OOP design: The `HealthReport` must blindly run `.check()` on its list, proving polymorphism (where different objects share the identical method signature).

## 2. STARTER CODE

```python
import json
import random

class ServiceCheck:
    def __init__(self, name: str):
        self.name = name

    def check(self) -> dict:
        raise NotImplementedError("Subclasses must implement")

# TODO: Implement HTTPCheck(ServiceCheck)
# Returns e.g. {"status": "up", "latency_ms": 45}

# TODO: Implement DatabaseCheck(ServiceCheck)
# Returns e.g. {"status": "down", "error": "Connection Refused"}

# TODO: Implement DiskCheck(ServiceCheck)
# Returns e.g. {"status": "up", "free_space_gb": 120}

class HealthReport:
    def __init__(self):
        self._services: list[ServiceCheck] = []

    def add_service(self, service: ServiceCheck):
        self._services.append(service)

    def generate_report(self) -> str:
        """
        TODO: Loop through services, call format their checks.
        Aggregate into a master dict:
        {
          "system_status": "UP" | "DEGRADED" | "DOWN",
          "services": {
             "database_main": {...},
             "payment_api": {...}
          }
        }
        Rule: If any service is "down", system_status is "DOWN".
        """
        pass

if __name__ == "__main__":
    monitor = HealthReport()

    db_check = ServiceCheck("master_db") # Actually instantiate DatabaseCheck!
    # monitor.add_service(db_check)

    # ... Add others ...

    print(monitor.generate_report())
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Inheritance is the key here.

```python
class DatabaseCheck(ServiceCheck):
    def check(self) -> dict:
        # Simulate a 10% chance of failure
        is_up = random.random() > 0.1
        if is_up:
            return {"status": "up", "connections": 15}
        return {"status": "down", "error": "Timeout"}
```

**HINT-2 (Partial)**:
To build the report, initialize an empty `results = {}` and loop through `self._services`. Add each service's check dictionary to `results` under the key `service.name`.

**HINT-3 (Near-solution)**:

```python
def generate_report(self) -> str:
    report = {
        "services": {},
        "system_status": "UP"
    }

    for srv in self._services:
        result = srv.check()
        report["services"][srv.name] = result

        # Override overall status if anything failed
        if result.get("status") == "down":
            report["system_status"] = "DOWN"

    return json.dumps(report, indent=2)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Kubernetes `livenessProbe` and `readinessProbe`, Docker Heathchecks, Datadog endpoints, Spring Boot Actuator.
- **Why do it manually**: A standard FastAPI template lacks robust healthchecks. Writing a polymorphic aggregator lets you easily bolt-on custom checks (like "Stripe API Connectivity") into your startup routines without breaking or tangling code.

## 5. VALIDATION CRITERIA

- [ ] Subclasses fundamentally rely on overriding the `check()` method perfectly.
- [ ] Output perfectly aligns with JSON specification (boolean states, integers not quoted).
- [ ] Aggregation logic successfully infers a global `DOWN` state if _a single_ child service reports failure.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Using @property):** Modify the `generate_report` structure so that `system_status` isn't a manually calculated string, but a dynamic `@property` attached to the `HealthReport` class that is constantly calculated on access.
2. **Extension 2 (Real System Checks):** Make `DiskCheck` no longer simulated. Use Python's `shutil.disk_usage("/")` module to actually parse the hard drive of the executing computer and return actual gigabyte strings.
3. **Extension 3 (Async Execution):** In a production scenario with 20 microservices, executing checks synchronously might take too long. Convert the classes mathematically so `.check()` is `async def`. Have `generate_report()` utilize `asyncio.gather()` to execute all checks concurrently.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`json`).
