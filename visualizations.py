import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings("ignore")

sns.set_theme(style="whitegrid")
COLORS = sns.color_palette("Set2", 10)

df = pd.read_csv("data/cleaned_job_data.csv")

all_skills = []
for s in df["Skills Required"]:
    all_skills.extend([x.strip() for x in s.split(",")])
top_skills = pd.Series(Counter(all_skills)).sort_values(ascending=False).head(15)

# 1. Top 10 Hiring Cities
fig, ax = plt.subplots(figsize=(10, 5))
city_data = df["City"].value_counts().head(10)
bars = ax.bar(city_data.index, city_data.values, color=COLORS)
ax.bar_label(bars, padding=3, fontsize=9)
ax.set_title("Top 10 Hiring Cities", fontsize=14, fontweight="bold")
ax.set_xlabel("City"); ax.set_ylabel("Number of Job Postings")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("outputs/1_top_cities.png", dpi=150)
plt.close()
print("[OK] Chart 1 saved: Top Hiring Cities")

# 2. Top 15 In-Demand Skills
fig, ax = plt.subplots(figsize=(12, 6))
top_skills.plot(kind="barh", ax=ax, color=sns.color_palette("Blues_r", 15))
ax.set_title("Top 15 In-Demand Skills for Data Analysts", fontsize=14, fontweight="bold")
ax.set_xlabel("Demand Count"); ax.set_ylabel("Skill")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/2_top_skills.png", dpi=150)
plt.close()
print("[OK] Chart 2 saved: Top Skills")

# 3. Average Salary by Experience
fig, ax = plt.subplots(figsize=(9, 5))
sal_exp = df.groupby("Experience Level")["Salary (LPA)"].mean().round(2).sort_values()
bars = ax.barh(sal_exp.index, sal_exp.values, color=sns.color_palette("Greens_d", len(sal_exp)))
ax.bar_label(bars, fmt="%.1f LPA", padding=4, fontsize=9)
ax.set_title("Average Salary by Experience Level (LPA)", fontsize=14, fontweight="bold")
ax.set_xlabel("Average Salary (LPA)")
plt.tight_layout()
plt.savefig("outputs/3_salary_by_experience.png", dpi=150)
plt.close()
print("[OK] Chart 3 saved: Salary by Experience")

# 4. Average Salary by City
fig, ax = plt.subplots(figsize=(10, 5))
sal_city = df.groupby("City")["Salary (LPA)"].mean().round(2).sort_values(ascending=False)
bars = ax.bar(sal_city.index, sal_city.values, color=sns.color_palette("OrRd", len(sal_city)))
ax.bar_label(bars, fmt="%.1f", padding=3, fontsize=9)
ax.set_title("Average Salary by City (LPA)", fontsize=14, fontweight="bold")
ax.set_xlabel("City"); ax.set_ylabel("Avg Salary (LPA)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("outputs/4_salary_by_city.png", dpi=150)
plt.close()
print("[OK] Chart 4 saved: Salary by City")

# 5. Remote / Hybrid / On-site Pie
fig, ax = plt.subplots(figsize=(7, 7))
remote_data = df["Remote"].value_counts()
ax.pie(remote_data.values, labels=remote_data.index, autopct="%1.1f%%",
       colors=sns.color_palette("Pastel1", len(remote_data)), startangle=140,
       wedgeprops={"edgecolor": "white", "linewidth": 1.5})
ax.set_title("Work Mode Distribution\n(Remote / Hybrid / On-site)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/5_remote_split.png", dpi=150)
plt.close()
print("[OK] Chart 5 saved: Remote Split")

# 6. Top Companies Hiring Freshers
fig, ax = plt.subplots(figsize=(10, 5))
freshers = df[df["Experience Level"].str.contains("Fresher", case=False)]
fc = freshers["Company"].value_counts().head(10)
bars = ax.bar(fc.index, fc.values, color=sns.color_palette("Set3", 10))
ax.bar_label(bars, padding=3, fontsize=9)
ax.set_title("Top 10 Companies Hiring Freshers", fontsize=14, fontweight="bold")
ax.set_xlabel("Company"); ax.set_ylabel("Fresher Job Postings")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("outputs/6_fresher_companies.png", dpi=150)
plt.close()
print("[OK] Chart 6 saved: Fresher Companies")

# 7. Industry Distribution
fig, ax = plt.subplots(figsize=(9, 5))
ind_data = df["Industry"].value_counts()
bars = ax.barh(ind_data.index, ind_data.values, color=sns.color_palette("tab10", len(ind_data)))
ax.bar_label(bars, padding=3, fontsize=9)
ax.set_title("Job Distribution by Industry", fontsize=14, fontweight="bold")
ax.set_xlabel("Number of Jobs")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/7_industry_distribution.png", dpi=150)
plt.close()
print("[OK] Chart 7 saved: Industry Distribution")

# 8. Salary Distribution Box Plot
fig, ax = plt.subplots(figsize=(11, 5))
order = ["Fresher (0-1 Yr)", "Junior (1-3 Yrs)", "Mid (3-5 Yrs)", "Senior (5+ Yrs)"]
present = [o for o in order if o in df["Experience Level"].unique()]
sns.boxplot(data=df, x="Experience Level", y="Salary (LPA)", order=present,
            palette="Set2", ax=ax)
ax.set_title("Salary Distribution by Experience Level", fontsize=14, fontweight="bold")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig("outputs/8_salary_distribution.png", dpi=150)
plt.close()
print("[OK] Chart 8 saved: Salary Distribution")

# 9. Heatmap - Avg Salary: City x Experience
fig, ax = plt.subplots(figsize=(13, 6))
pivot = df.pivot_table(values="Salary (LPA)", index="City",
                       columns="Experience Level", aggfunc="mean").round(1)
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5,
            cbar_kws={"label": "Avg Salary (LPA)"}, ax=ax)
ax.set_title("Avg Salary Heatmap: City x Experience Level", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/9_salary_heatmap.png", dpi=150)
plt.close()
print("[OK] Chart 9 saved: Salary Heatmap")

# 10. Dashboard Summary (2x3 grid)
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Job Market Pulse Analyzer - Dashboard", fontsize=18, fontweight="bold", y=1.01)

city_data = df["City"].value_counts().head(8)
axes[0, 0].bar(city_data.index, city_data.values, color=COLORS)
axes[0, 0].set_title("Top Hiring Cities"); axes[0, 0].tick_params(axis="x", rotation=45)

top_skills.head(10).plot(kind="barh", ax=axes[0, 1], color=sns.color_palette("Blues_r", 10))
axes[0, 1].set_title("Top 10 In-Demand Skills"); axes[0, 1].invert_yaxis()

remote_data = df["Remote"].value_counts()
axes[0, 2].pie(remote_data.values, labels=remote_data.index, autopct="%1.1f%%",
               colors=sns.color_palette("Pastel1", 3))
axes[0, 2].set_title("Work Mode Split")

sal_exp = df.groupby("Experience Level")["Salary (LPA)"].mean().round(2).sort_values()
axes[1, 0].barh(sal_exp.index, sal_exp.values, color=sns.color_palette("Greens_d", 4))
axes[1, 0].set_title("Avg Salary by Experience")

fc = freshers["Company"].value_counts().head(8)
axes[1, 1].bar(fc.index, fc.values, color=sns.color_palette("Set3", 8))
axes[1, 1].set_title("Top Fresher-Hiring Companies"); axes[1, 1].tick_params(axis="x", rotation=45)

ind_data = df["Industry"].value_counts()
axes[1, 2].barh(ind_data.index, ind_data.values, color=sns.color_palette("tab10", len(ind_data)))
axes[1, 2].set_title("Jobs by Industry"); axes[1, 2].invert_yaxis()

plt.tight_layout()
plt.savefig("outputs/10_dashboard.png", dpi=150, bbox_inches="tight")
plt.close()
print("[OK] Chart 10 saved: Full Dashboard")

print("\n[DONE] All charts saved in outputs/ folder!")
