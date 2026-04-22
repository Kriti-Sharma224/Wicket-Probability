# Wicket Probability Model API

## Run Locally
pip install -r requirements.txt
uvicorn main:app --reload

## Endpoint
POST /bowling/wicket-probability

## Example Request
{
  "balls_bowled": 60,
  "wickets": 2,
  "runs_conceded": 45,
  "match_phase": "middle"
}

## Example Response
{
  "base_probability": 0.0333,
  "phase_adjustment": 1.0,
  "final_probability": 0.0333,
  "interpretation": "Low Wicket Probability"
}

## Admin Handover Documentation:

# 1. API Name
Wicket Probability Model API

# 2. Objective
This API estimates the likelihood of a bowler taking a wicket based on past performance and match context. Instead of treating wickets as fixed outcomes, it models them probabilistically using historical efficiency and contextual adjustments like match phase and economy rate.

# 3. Scientific Principle Used

i) Frequentist Probability → Wickets per ball

ii) Contextual Weighting Model → Adjust probability using match phase and economy

iii) Heuristic Adjustment → Reflect real-world cricket dynamics (pressure phases)

# 4. Input Fields

-> Field	Type	Description

i) balls_bowled	int	Total legal deliveries bowled

ii) wickets	int	Total wickets taken

iii) runs_conceded	int	Total runs conceded

iv) match_phase	str	powerplay / middle / death

# 5. Derived Variables

-> Variable	Meaning

i) base_probability	wickets per ball

ii) economy	runs per ball

iii) economy_factor	control adjustment based on economy

iv) phase_weight	contextual match phase multiplier

# 6. Final Output Fields

-> Field	Meaning

i) base_probability	raw wicket likelihood

ii) phase_adjustment	match phase influence

iii) final_probability	adjusted wicket probability

iv) interpretation	human-readable category

# 7. Example Request

{

  "balls_bowled": 60,
  
  "wickets": 3,
  
  "runs_conceded": 50,
  
  "match_phase": "death"
  
}

# 8. Example Response

{

  "base_probability": 0.05,
  
  "phase_adjustment": 1.3,
  
  "final_probability": 0.065,
  
  "interpretation": "Moderate Wicket Probability"
  
}

# 9. Validation Errors

-> balls_bowled must be > 0

-> wickets cannot be negative

-> runs_conceded cannot be negative

-> invalid match_phase defaults to neutral weight

# 10. Assumptions

-> Each ball is an independent probabilistic event

-> Match phase impacts wicket likelihood

-> Economy reflects bowler control and pressure

-> Model is simplified but realistic for MVP

# 11. New Model Fields Proposed
-> match_phase (categorical contextual variable)
