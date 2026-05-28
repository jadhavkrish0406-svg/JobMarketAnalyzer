import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

job_titles = [
    "Data Analyst", "Senior Data Analyst", "Junior Data Analyst",
    "Business Analyst", "Data Scientist", "BI Analyst",
    "Marketing Analyst", "Financial Analyst", "Operations Analyst",
    "Product Analyst"
]

companies = [
    "TCS", "Infosys", "Wipro", "HCL Technologies", "Tech Mahindra",
    "Accenture", "Cognizant", "IBM India", "Capgemini", "Deloitte",
    "Amazon India", "Flipkart", "Swiggy", "Zomato", "Paytm",
    "HDFC Bank", "ICICI Bank", "Axis Bank", "Reliance Jio", "Byju's",
    "Ola", "Razorpay", "PhonePe", "MakeMyTrip", "Nykaa"
]

cities = [
    "Bangalore", "Mumbai", "Hyderabad", "Chennai", "Pune",
    "Delhi", "Noida", "Gurgaon", "Kolkata", "Ahmedabad"
]

experience_levels = ["Fresher (0-1 yr)", "Junior (1-3 yrs)", "Mid (3-5 yrs)", "Senior (5+ yrs)"]

skills_pool = [
    "Python", "SQL", "Excel", "Power BI", "Tableau",
    "R", "Machine Learning", "Statistics", "Pandas", "NumPy",
    "Data Visualization", "ETL", "Spark", "Hadoop", "AWS",
    "Azure", "Google Analytics", "JIRA", "Communication", "Storytelling"
]

industries = ["IT Services", "E-Commerce", "Banking & Finance", "Healthcare", "EdTech", "Logistics", "Retail"]

def random_skills():
    n = random.randint(3, 7)
    return ", ".join(random.sample(skills_pool, n))

def salary_by_exp(exp):
    if exp == "Fresher (0-1 yr)":
        return round(random.uniform(3.0, 6.5), 1)
    elif exp == "Junior (1-3 yrs)":
        return round(random.uniform(5.0, 10.0), 1)
    elif exp == "Mid (3-5 yrs)":
        return round(random.uniform(9.0, 18.0), 1)
    else:
        return round(random.uniform(16.0, 35.0), 1)

n = 1000
data = {
    "Job Title": [random.choice(job_titles) for _ in range(n)],
    "Company": [random.choice(companies) for _ in range(n)],
    "City": [random.choice(cities) for _ in range(n)],
    "Experience Level": [random.choice(experience_levels) for _ in range(n)],
    "Industry": [random.choice(industries) for _ in range(n)],
    "Skills Required": [random_skills() for _ in range(n)],
    "Remote": [random.choice(["Yes", "No", "Hybrid"]) for _ in range(n)],
    "Job Postings Count": [random.randint(1, 50) for _ in range(n)],
}
data["Salary (LPA)"] = [salary_by_exp(e) for e in data["Experience Level"]]

df = pd.DataFrame(data)
df.to_csv("data/job_market_data.csv", index=False)
print(f"Dataset created: {len(df)} records saved to data/job_market_data.csv")
