import pandas as pd

college_football_data = pd.read_csv("cfb.csv")

season = int(input("What season would you like to view? "))

season_data = college_football_data[college_football_data["Season"] == season]

if season_data.empty:
        print(f"The {season} season was not found.")
else:
    win_categories = {
    "10 or more wins:": [],
    "8-9 wins:": [],
    "6-7 wins:": [],
     "Fewer than 6 wins:": []
    }

    print(f"College Football Results for {season}")

    for index, row in season_data.iterrows():
        team_name = row["Team"].split("(")[0].strip()
        if row["Win"] >= 10:
            win_categories["10 or more wins:"].append(team_name)
        elif row["Win"] >= 8:
            win_categories["8-9 wins:"].append(team_name)
        elif row["Win"] >= 6:
            win_categories["6-7 wins:"].append(team_name)
        else:
            win_categories["Fewer than 6 wins:"].append(team_name)
            
    for category, teams in win_categories.items():
        if len(teams) == 0:
            print(category)
            print("No teams found.")
        else:
            print(category)
            print("\n".join(teams))
