import pandas as pd
from collections import Counter

def run_analysis():
    df = pd.read_csv("data/cleaned_job_data.csv")

    print("=" * 50)
    print("       JOB MARKET PULSE - KEY INSIGHTS")
    print("=" * 50)

    print("\n[1] TOP 5 HIRING CITIES:")
    city_counts = df["City"].value_counts().head(5)
    print(city_counts.to_string())

    print("\n[2] TOP 10 HIRING COMPANIES:")
    company_counts = df["Company"].value_counts().head(10)
    print(company_counts.to_string())

    print("\n[3] TOP 15 IN-DEMAND SKILLS:")
    all_skills = []
    for skills in df["Skills Required"]:
        all_skills.extend([s.strip() for s in skills.split(",")])
    skill_counts = Counter(all_skills)
    top_skills = pd.Series(skill_counts).sort_values(ascending=False).head(15)
    print(top_skills.to_string())

    print("\n[4] AVERAGE SALARY BY EXPERIENCE (LPA):")
    salary_exp = df.groupby("Experience Level")["Salary (LPA)"].mean().round(2).sort_values(ascending=False)
    print(salary_exp.to_string())

    print("\n[5] AVERAGE SALARY BY CITY (LPA):")
    salary_city = df.groupby("City")["Salary (LPA)"].mean().round(2).sort_values(ascending=False)
    print(salary_city.to_string())

    print("\n[6] REMOTE / HYBRID / ON-SITE SPLIT:")
    remote_counts = df["Remote"].value_counts()
    print(remote_counts.to_string())

    print("\n[7] TOP COMPANIES HIRING FRESHERS:")
    freshers = df[df["Experience Level"].str.contains("Fresher", case=False)]
    fresher_companies = freshers["Company"].value_counts().head(10)
    print(fresher_companies.to_string())

    print("\n[8] JOBS BY INDUSTRY:")
    industry_counts = df["Industry"].value_counts()
    print(industry_counts.to_string())

    with pd.ExcelWriter("outputs/analysis_summary.xlsx", engine="openpyxl") as writer:
        city_counts.to_frame("Job Count").to_excel(writer, sheet_name="Top Cities")
        company_counts.to_frame("Job Count").to_excel(writer, sheet_name="Top Companies")
        top_skills.to_frame("Demand Count").to_excel(writer, sheet_name="Top Skills")
        salary_exp.to_frame("Avg Salary LPA").to_excel(writer, sheet_name="Salary by Experience")
        salary_city.to_frame("Avg Salary LPA").to_excel(writer, sheet_name="Salary by City")
        remote_counts.to_frame("Count").to_excel(writer, sheet_name="Remote Split")
        fresher_companies.to_frame("Fresher Jobs").to_excel(writer, sheet_name="Fresher Companies")
        industry_counts.to_frame("Count").to_excel(writer, sheet_name="Industry Split")

    print("\n[OK] Full analysis saved to outputs/analysis_summary.xlsx")
    return df, top_skills

if __name__ == "__main__":
    run_analysis()
