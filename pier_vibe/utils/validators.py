"""Input validation and safety bounds checking."""


class InputValidator:
    """Validate bridge and environmental parameters."""
    
    WATER_DEPTH_RANGE = (0, 200)  # meters
    PIER_DIAMETER_RANGE = (0.5, 10)  # meters
    D50_RANGE = (0.01, 10)  # mm
    VELOCITY_RANGE = (0, 10)  # m/s
    WAVE_HEIGHT_RANGE = (0, 20)  # meters
    BSHI_RANGE = (0, 1)
    
    @classmethod
    def validate_water_depth(cls, depth: float) -> float:
        if depth < cls.WATER_DEPTH_RANGE[0] or depth > cls.WATER_DEPTH_RANGE[1]:
            raise ValueError(f"Water depth {depth}m out of range {cls.WATER_DEPTH_RANGE}")
        return depth
    
    @classmethod
    def validate_pier_diameter(cls, D: float) -> float:
        if D < cls.PIER_DIAMETER_RANGE[0] or D > cls.PIER_DIAMETER_RANGE[1]:
            raise ValueError(f"Pier diameter {D}m out of range {cls.PIER_DIAMETER_RANGE}")
        return D
    
    @classmethod
    def validate_d50(cls, d50: float) -> float:
        if d50 < cls.D50_RANGE[0] or d50 > cls.D50_RANGE[1]:
            raise ValueError(f"d50 {d50}mm out of range {cls.D50_RANGE}")
        return d50
    
    @classmethod
    def validate_bshi(cls, bshi: float) -> float:
        if bshi < cls.BSHI_RANGE[0] or bshi > cls.BSHI_RANGE[1]:
            raise ValueError(f"BSHI {bshi} out of range {cls.BSHI_RANGE}")
        return bshi
    
    @classmethod
    def validate_positive(cls, value: float, name: str) -> float:
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")
        return value
