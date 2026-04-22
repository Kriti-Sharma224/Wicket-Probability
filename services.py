from schemas import WicketProbInput
from utils import (
    get_phase_weight,
    get_economy_factor,
    get_aggression_factor,
    get_interpretation,
)


def process_wicket_probability(data: WicketProbInput):
    # Derived stats from events
    balls = sum(1 for e in data.events if e.is_legal)
    wickets = sum(1 for e in data.events if e.is_wicket)
    runs = sum(e.runs for e in data.events)

    if balls == 0:
        return {
            "balls_bowled": 0,
            "wickets": 0,
            "base_probability": 0,
            "economy": 0,
            "final_probability": 0,
            "interpretation": "No Data"
        }

    # Base probability
    base_prob = wickets / balls

    # Economy
    economy = runs / balls

    # Factors
    economy_factor = get_economy_factor(economy)
    phase_weight = get_phase_weight(data.match_phase)
    aggression_factor = get_aggression_factor(data.batter_strike_rate)

    # Final probability
    final_prob = base_prob * economy_factor * phase_weight * aggression_factor
    final_prob = min(max(final_prob, 0), 1)

    return {
        "balls_bowled": balls,
        "wickets": wickets,
        "base_probability": round(base_prob, 4),
        "economy": round(economy, 2),
        "final_probability": round(final_prob, 4),
        "interpretation": get_interpretation(final_prob),
    }