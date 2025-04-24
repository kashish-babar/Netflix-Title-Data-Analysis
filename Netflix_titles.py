##importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## importing dataset
df = pd.read_csv(r"C:\Users\kashi\Downloads\netflix_titles_nov_2019.csv.zip")

print(df.head())
print(df.info())
print(df.describe())


## hadling missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")


df["date_added"].dropna(inplace=True)


df["rating"] = df["rating"].fillna(df["rating"].mode()[0])
print(df["rating"].isnull().sum())
print(df.isnull().sum())
print(df.shape)



## analyze the data
print(df["type"].value_counts())
print(df["release_year"].value_counts())
print(df["country"].value_counts())


## data visualization

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="release_year", palette="Set2")
plt.title("Count of Movies and TV Shows by Release Year")
plt.xticks(rotation=90)
plt.show()  # shows that the most number of movies and tv shows are released in 2018 and 2019


plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="type", palette="Set2")
plt.title("Count of Movies and TV Shows")
plt.xticks(rotation=90)
plt.show()  # shows that the most number of movies and tv shows are movies


plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="rating", palette="Set2")
plt.title("Count of Movies and TV Shows by Rating")
plt.xticks(rotation=90)
plt.show()  # shows that the most number of movies and tv shows are TV-MA

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="country", palette="Set2")
plt.title("Count of Movies and TV Shows by Country")
plt.xticks(rotation=90)
plt.show()  # shows that the most number of movies and tv shows are from USA
