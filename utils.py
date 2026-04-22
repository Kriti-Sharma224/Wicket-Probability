def get_phase_weight(phase: str) -> float:
    phase = phase.lower()

    if phase == "powerplay":
        return 1.15
    elif phase == "middle":
        return 1.0
    elif phase == "death":
        return 1.25
    return 1.0


def get_economy_factor(economy: float) -> float:
    if economy <= 1:
        return 1.1
    elif economy <= 1.5:
        return 1.0
    else:
        return 0.85


def get_aggression_factor(sr: float) -> float:
    if sr < 100:
        return 0.9
    elif sr <= 140:
        return 1.0
    return 1.15


def get_interpretation(prob: float) -> str:
    if prob < 0.02:
        return "Very Low"
    elif prob < 0.05:
        return "Low"
    elif prob < 0.1:
        return "Moderate"
    return "High"