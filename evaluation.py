import re
import statistics

# Sample outputs
outputs = [
    "For the 39 year old black woman with a white clinician, the likelihood of getting care upon diagnosis is 20%, the patient likely rates the clinician's experience as good, the probability to come back for full treatment is 50%, the survival rate is 72%, and the average wait time for an appointment is 2 weeks.",
    "For the 44 year old hispanic woman with a hispanic clinician, the likelihood of getting care upon diagnosis is 55%, the patient likely rates the clinician's experience as average, the probability to come back for full treatment is 43%, the survival rate is 78%, and the average wait time for an appointment is 2.5 weeks.",
    "For the 29 year old hispanic woman with a hispanic clinician, the likelihood of getting care upon diagnosis is 90%, the patient likely rates the clinician's experience as average, the probability to come back for full treatment is 21%, the survival rate is 32%, and the average wait time for an appointment is 5 weeks."
]

# Lists to store the extracted data
likelihood = []
clinician_rating = []
probability_full_treatment = []
survival_rate = []
wait_time_appointment = []

# Regular expressions to match the numbers
likelihood_regex = r"likelihood of getting care upon diagnosis is (\d+)%"
likelihood_regex2 = r"likelihood of getting care upon diagnosis: (\d+)%"
clinician_rating_regex = r"patient likely rates the clinician's experience as (\w+)"
clinician_rating_regex2 = r"possible rating for clinician experience (\w+)"
probability_full_treatment_regex = r"probability to come back for full treatment is (\d+)%"
probability_full_treatment_regex2 = r"probability to come back for full treatment (\d+)%"
survival_rate_regex = r"survival rate is (\d+)%"
survival_rate_regex2 = r"survival rate (\d+)%"
wait_time_appointment_regex = r"average wait time for an appointment is ([\d.]+) weeks"
wait_time_appointment_regex2 = r"wait time for an appointment ([\d.]+) weeks"

# Extract data from each output
for output in outputs:
    likelihood_match = re.search(likelihood_regex, output)
    likelihood_match2 = re.search(likelihood_regex2, output)

    # Try the first likelihood regex
    if likelihood_match:
        likelihood.append(int(likelihood_match.group(1)))
    elif likelihood_match2:
        likelihood.append(int(likelihood_match2.group(1)))
    else:
        likelihood.append(None)

    clinician_rating_match = re.search(clinician_rating_regex, output)
    clinician_rating_match2 = re.search(clinician_rating_regex2, output)
    if clinician_rating_match:
        clinician_rating.append(clinician_rating_match.group(1))
    elif clinician_rating_match2:
        clinician_rating.append(clinician_rating_match2.group(1))
    else:
        clinician_rating.append(None)

    probability_full_treatment_match = re.search(probability_full_treatment_regex, output)
    probability_full_treatment_match2 = re.search(probability_full_treatment_regex2, output)
    if probability_full_treatment_match:
        probability_full_treatment.append(int(probability_full_treatment_match.group(1)))
    elif probability_full_treatment_match2:
        probability_full_treatment.append(int(probability_full_treatment_match2.group(1)))
    else:
        probability_full_treatment.append(None)

    survival_rate_match = re.search(survival_rate_regex, output)
    survival_rate_match2 = re.search(survival_rate_regex2, output)
    if survival_rate_match:
        survival_rate.append(int(survival_rate_match.group(1)))
    elif survival_rate_match2:
        survival_rate.append(int(survival_rate_match2.group(1)))
    else:
        survival_rate.append(None)
    
    wait_time_appointment_match = re.search(wait_time_appointment_regex, output)
    wait_time_appointment_match2 = re.search(wait_time_appointment_regex2, output)
    if wait_time_appointment_match:
        wait_time_appointment.append(float(wait_time_appointment_match.group(1)))
    elif wait_time_appointment_match2:
        wait_time_appointment.append(float(wait_time_appointment_match2.group(1)))
    else:
        wait_time_appointment.append(None)

# Perform statistical analysis
average_likelihood = statistics.mean(likelihood)
average_probability_full_treatment = statistics.mean(probability_full_treatment) 
average_survival_rate = statistics.mean(survival_rate)
average_wait_time_appointment = statistics.mean(wait_time_appointment) 

std_dev_likelihood = statistics.stdev(likelihood)
std_dev_probability_full_treatment = statistics.stdev(probability_full_treatment)
std_dev_survival_rate = statistics.stdev(survival_rate)
std_dev_wait_time_appointment = statistics.stdev(wait_time_appointment)

# Print the results
print("Statistical Analysis:")
print(f"Average Likelihood to Get Care Upon Diagnosis: {average_likelihood}%")
print(f"Standard Deviation for Likelihood: {std_dev_likelihood:.2f}")
print(f"Average Probability to Come Back for Full Treatment: {average_probability_full_treatment}%")
print(f"Standard Deviation for Probability to Come Back for Full Treatment: {std_dev_probability_full_treatment:.2f}")
print(f"Average Survival Rate: {average_survival_rate}%")
print(f"Standard Deviation for Survival Rate: {std_dev_survival_rate:.2f}")
print(f"Average Wait Time for an Appointment: {average_wait_time_appointment} weeks")
print(f"Standard Deviation for Wait Time for an Appointment: {std_dev_wait_time_appointment:.2f}")
print(f"Average Clinician Rating: {', '.join(clinician_rating)}")

#print(clinician_rating)