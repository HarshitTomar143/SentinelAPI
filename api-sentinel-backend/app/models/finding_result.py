from dataclasses import dataclass

@dataclass
class FindingResult:
    title : str
    description : str
    severity : str
    passed : bool
    recommendation: str