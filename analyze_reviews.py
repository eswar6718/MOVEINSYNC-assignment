
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("moveinsync_reviews.csv")

print("=" * 40)
print("MOVEINSYNC REVIEW ANALYSIS")
print("=" * 40)

print("\nTotal reviews:", len(df))

print("\nRating distribution:")
rating_counts = df["score"].value_counts().sort_index()
print(rating_counts)

print("\nRating percentages:")
print((rating_counts / len(df) * 100).round(2).astype(str) + "%")

print("\nAverage rating:", round(df["score"].mean(), 2), "/ 5")

negative = df[df["score"].isin([1, 2])]
print("\nNegative reviews (1 and 2 stars):", len(negative))
print("Negative review percentage:",
      round(len(negative) / len(df) * 100, 2), "%")

print("\nSaving rating chart...")

rating_counts.plot(kind="bar", rot=0)
plt.title("MoveInSync Review Rating Distribution")
plt.xlabel("Star Rating")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

print("\nChart saved as rating_distribution.png")
