import numpy as np
from scipy.integrate import odeint

# Define the SIR model differential equations
def sir_model(y, t, contact_rate, recovery_rate):
    susceptible, infected, recovered = y
    N = susceptible + infected + recovered  # Total population
    
    # Define the differential equations
    dSdt = -contact_rate * susceptible * infected / N  # Rate of susceptible individuals becoming infected
    dIdt = contact_rate * susceptible * infected / N - recovery_rate * infected  # Rate of infected individuals transitioning to recovered
    dRdt = recovery_rate * infected  # Rate of infected individuals recovering
    
    return [dSdt, dIdt, dRdt]

def simulate_disease_progression(age, initial_infected, contact_rate, recovery_rate, disease_duration):
    # Initial conditions: [susceptible, infected, recovered]
    susceptible_initial = 1000 - initial_infected  # Assuming population of 1000 for simplicity
    infected_initial = initial_infected
    recovered_initial = 0

    # Time points (e.g., days)
    time = np.linspace(0, disease_duration, disease_duration)

    # Solve ODE
    solution = odeint(sir_model, [susceptible_initial, infected_initial, recovered_initial], time, args=(contact_rate, recovery_rate))

    susceptible, infected, recovered = solution.T  # Transpose to get arrays for each compartment

    return time, susceptible, infected, recovered
