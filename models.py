from dataclasses import dataclass


@dataclass
class TargetGPU:
    priority: int
    name: str
    max_used: float
    max_new: float


@dataclass
class Listing:
    source: str
    listing_id: str
    title: str
    gpu_name: str
    price: float
    condition: str
    url: str