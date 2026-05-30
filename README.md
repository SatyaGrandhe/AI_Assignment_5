# ARTIFICIAL INTELLIGENCE MINI PROJECTS

## TABLE OF CONTENTS

1. Search Algorithms using Tic-Tac-Toe
2. Test Cases for Search Algorithms
3. AI Travel Planner
4. Knowledge Graph Implementation
5. Bayesian Network Implementation
6. Conclusion


### 1. SEARCH ALGORITHMS USING TIC-TAC-TOE
   

## Objective

The main objective of this project is to implement and compare different Artificial Intelligence search algorithms using the Tic-Tac-Toe game.

## Algorithms Implemented

• Minimax Algorithm
• Alpha-Beta Pruning
• Heuristic Alpha-Beta Search
• Monte Carlo Tree Search (MCTS)

## Project Description

This project demonstrates how AI algorithms make decisions in a game environment. The algorithms analyze the board positions and select the best possible move for the player.

## Algorithm Explanation

1. Minimax Algorithm

   * Explores all possible game states.
   * Maximizes the player's winning chance.
   * Minimizes the opponent's advantage.

2. Alpha-Beta Pruning

   * Optimized version of Minimax.
   * Eliminates unnecessary branches.
   * Reduces search complexity.

3. Heuristic Alpha-Beta Search

   * Uses heuristic evaluation functions.
   * Applies depth-limited search.
   * Improves execution efficiency.

4. Monte Carlo Tree Search

   * Uses random simulations.
   * Selects moves with the highest success probability.
   * Widely used in intelligent game systems.

## Files Included

• search_algorithms.py
• test_search_algorithms.py

## Execution

python search_algorithms.py

python test_search_algorithms.py

## Expected Output

The algorithms should generate valid and optimal moves according to the Tic-Tac-Toe board configuration.


### 2. TEST CASES FOR SEARCH ALGORITHMS

## Objective

The purpose of this module is to validate the correctness of the implemented search algorithms.

## Description

Different board configurations are tested to evaluate the performance of the algorithms under multiple scenarios.

## Algorithms Tested

• Minimax Algorithm
• Alpha-Beta Search
• Heuristic Alpha-Beta Search
• Monte Carlo Tree Search

## Test Cases Included

• Winning move test
• Opponent blocking test
• Empty board test
• Draw state test

## Execution

python test_search_algorithms.py

## Expected Output

All algorithms should return appropriate moves according to the provided board state.

### 3. AI TRAVEL PLANNER


## Objective

The objective of this project is to build a simple AI-based travel planner that generates personalized travel recommendations.

## Project Description

The system provides:
• Tourist place recommendations
• Food suggestions
• Hotel selection based on budget
• Travel cost estimation
• Personalized day-wise tour plan

## Knowledge Base Includes

• Tourist attractions
• Food recommendations
• Hotel categories
• Transport information

## Supported Cities

• Hyderabad
• Visakhapatnam
• Bengaluru

## User Inputs

• Destination city
• Budget
• Number of days
• Travel interest
• Food preference

## Generated Outputs

• Recommended tourist places
• Food suggestions
• Estimated trip cost
• Personalized itinerary

## Execution

python travel_planner.py

## Expected Output

The system generates a personalized travel plan according to the user’s preferences and budget.

### 4. KNOWLEDGE GRAPH IMPLEMENTATION

## Objective

The objective of this project is to understand Knowledge Graphs and their role in representing structured relationships.

## Description

The implementation connects cities with:
• Tourist places
• Food recommendations
• Transport facilities

## Example Relationships

Hyderabad → has_place → Charminar

Hyderabad → has_food → Hyderabadi Biryani

Hyderabad → has_transport → Metro

## Features

• Relationship mapping
• Knowledge representation
• Information retrieval
• Graph exploration

## Tools Explored

• Neo4j
• RDFLib
• Protégé
• GraphDB
• NetworkX

## Execution

python knowledge_graphs.py

## Expected Output

The system displays information related to tourist places, food recommendations, and transport options for a selected city.

### 5. BAYESIAN NETWORK IMPLEMENTATION

## Objective

The purpose of this project is to understand probabilistic reasoning and inferencing using Bayesian Networks.

## Project Description

This implementation predicts disease probability using symptoms such as:
• Fever
• Cough
• Fatigue

## Problem Representation

Disease → Fever

Disease → Cough

Disease → Fatigue

## Inference

The Bayesian Network performs probabilistic inference using observed symptoms.

## Concepts Covered

• Conditional Probability
• Probabilistic Reasoning
• Uncertainty Modeling
• Inference Mechanisms

## Libraries / Tools Used

• pgmpy
• GeNIe
• Netica
• BayesiaLab
• bnlearn

## Installation Requirement

pip install pgmpy

## Execution

python bayesian_networks.py

## Expected Output

The system predicts disease probability based on the given symptoms using Bayesian inference.

### 6. CONCLUSION

These projects demonstrate important Artificial Intelligence concepts including:

• Search Algorithms
• Intelligent Decision Making
• AI-Based Planning Systems
• Knowledge Representation
• Probabilistic Inference
• Game Playing AI

The implementations provide practical understanding of how AI techniques can be applied in planning, reasoning, prediction, and problem-solving applications.
