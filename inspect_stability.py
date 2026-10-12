
import pandas as pd

df = pd.read_csv("moveinsync_reviews.csv")

negative = df[df["score"].isin([1, 2])].copy()
negative["content"] = negative["content"].fillna("")

keywords = [
    "support", "helpdesk", "help desk", "customer care",
    "not reachable", "no response", "complaint",
    "escalate", "contact number"
]

mask = negative["content"].str.lower().apply(
    lambda text: any(word in text for word in keywords)
)

matched = negative[mask]

print("Customer support keyword matches:", len(matched))
print("\nFirst 15 matching reviews:\n")

for _, row in matched.head(15).iterrows():
    print("Rating:", row["score"])
    print("Date:", row["at"])
    print("Review:", row["content"])
    print("-" * 60)
