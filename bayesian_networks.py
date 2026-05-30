from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# BUILD BAYESIAN NETWORK

bayesian_model = DiscreteBayesianNetwork([

    ("Disease", "Fever"),
    ("Disease", "Cough"),
    ("Disease", "Fatigue")

])


# DISEASE PROBABILITY TABLE

disease_cpd = TabularCPD(
    variable="Disease",
    variable_card=2,
    values=[
        [0.7],
        [0.3]
    ]
)


# FEVER PROBABILITY TABLE

fever_cpd = TabularCPD(
    variable="Fever",
    variable_card=2,

    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],

    evidence=["Disease"],
    evidence_card=[2]
)


# COUGH PROBABILITY TABLE

cough_cpd = TabularCPD(
    variable="Cough",
    variable_card=2,

    values=[
        [0.7, 0.3],
        [0.3, 0.7]
    ],

    evidence=["Disease"],
    evidence_card=[2]
)


# FATIGUE PROBABILITY TABLE

fatigue_cpd = TabularCPD(
    variable="Fatigue",
    variable_card=2,

    values=[
        [0.9, 0.4],
        [0.1, 0.6]
    ],

    evidence=["Disease"],
    evidence_card=[2]
)


# ADD CPDs TO MODEL

bayesian_model.add_cpds(
    disease_cpd,
    fever_cpd,
    cough_cpd,
    fatigue_cpd
)


# DISPLAY MODEL INFORMATION

print("Bayesian Network Structure")

print("Nodes Present:")
print(bayesian_model.nodes())

print("\nConnections:")
print(bayesian_model.edges())


print("\nModel Verification")
print("Is Model Correct ? :", bayesian_model.check_model())


# CREATE INFERENCE OBJECT

query_engine = VariableElimination(
    bayesian_model
)


# GIVEN SYMPTOMS

print("\nObserved Symptoms")

symptoms = {
    "Fever": 1,
    "Cough": 1
}

print("Fever = Yes")
print("Cough = Yes")


# RUN QUERY

prediction = query_engine.query(
    variables=["Disease"],
    evidence=symptoms
)


# DISPLAY RESULT

print("\nPredicted Disease Probability")
print(prediction)


print("\nExplanation:")
print("The Bayesian Network estimates")
print("the chance of disease occurrence")
print("using the provided symptoms.")


print("\nSymptoms Considered:")

symptom_names = [
    "Fever",
    "Cough",
    "Fatigue"
]

for symptom in symptom_names:
    print("-", symptom)
