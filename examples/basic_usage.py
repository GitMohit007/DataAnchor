from dataclasses import dataclass, field, asdict
import json
import time
from data_anchor import DataAnchor

@dataclass
class TestDC(DataAnchor):
    temperature: float = 0.0
    unit: str = "C"
    timestamp: float = 0.0

    def __post_init__(self):
        super().__init__()

    def to_bytes(self) -> bytes:
        return json.dumps(asdict(self)).encode("utf-8")
    
    def from_bytes_dict(self, data: bytes):
        return json.loads(data.decode("utf-8"))

if __name__ == "__main__":
    # Create an instance of the dataclass
    test = TestDC(1.0, "C")
    test.temperature = 30.0
    test.unit = "C"
    test.timestamp = 1234567890
    test2 = TestDC()
    
    print(f"Initial data Written: {test}")
    test.push()
    # time.sleep(0.00000001)
    
    test.temperature = 100.0
    test.unit = "C"
    test.timestamp = 1234567999
    print(f"DataClass modified but not written to shm {test}")  # Expected: 1.0 C
    
    test.temperature = 200.0
    test.unit = "K"
    test.timestamp = time.time()
    test.push()
    print(f"DataClass written to shm {test}")  # Expected: 200.0 C
    # time.sleep(0.00000001)
    
    test.pull()
    print(f"DataClass updated from shm {test}")  # Expected: 200.0 C
    print(f"testing singleton {test2}")  # Expected: 200.0 C
    # Clean up shared memory
    test.close_shared_memory()
