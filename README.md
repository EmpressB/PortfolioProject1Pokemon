# Pokémon Base Stat Analysis

## Project Overview
This project explores Pokémon data collected from the PokéAPI (https://pokeapi.co/). 
The goal is to analyze what factors influence a Pokémon's overall strength, 
measured by their Base Stat Total.

## Analytical Questions

### What does your dataset explore?
This dataset explores the characteristics and battle statistics of 1,025 Pokémon, 
including their types, physical attributes, and individual base stats.

### Dependent Variable
- **Variable:** `base_stat_total`
- **Type:** Quantitative
- **Description:** The sum of all six base stats (HP, Attack, Defense, 
Special Attack, Special Defense, Speed)

### Independent Variables
| Variable | Type |
|----------|------|
| hp | Quantitative |
| attack | Quantitative |
| defense | Quantitative |
| special_attack | Quantitative |
| special_defense | Quantitative |
| speed | Quantitative |
| height | Quantitative |
| weight | Quantitative |
| type_1 | Categorical |
| type_2 | Categorical |

### Dataset Size
- **Rows:** 1,025 Pokémon
- **Columns:** 13 features

## Project Structure


## Data Collection
Data is collected via the RESTful PokéAPI using the `src/data_ingestion.py` script.

## How to Run
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Run data ingestion: `python src/data_ingestion.py`

## Team
- Data Engineer: Shaday Brown