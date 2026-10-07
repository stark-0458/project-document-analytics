import pandas as pd
from faker import Faker
import random

fake = Faker()

projects = []

for i in range(1, 501):
    projects.append({
        "ProjectID": i,
        "ProjectName": f"Project_{i}",
        "Country": random.choice(["India", "Netherlands", "UK", "USA"]),
        "Manager": fake.name(),
        "Budget": random.randint(100000, 1000000)
    })

df = pd.DataFrame(projects)

df.to_csv("projects.csv", index=False)

print("projects.csv created successfully")