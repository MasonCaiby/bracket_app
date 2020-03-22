import os, sys

import django
import pandas as pd

sys.path.append("./src") # add path to project root dir
os.environ["DJANGO_SETTINGS_MODULE"] = "bracket.settings"

# for more sophisticated setups, if you need to change connection settings (e.g. when using django-environ):
#os.environ["DATABASE_URL"] = "postgres://myuser:mypassword@localhost:54324/mydb"

# Connect to Django ORM
django.setup()

# process data
from webpage.models import ActiveTeam

file = "src/data/routes.csv"
def process_data(file):
    df = pd.read_csv(file)
    df_desc = df.sort_values(by="score", ascending=False).to_numpy()

    length = (len(df_desc)//2)
    result = []
    for match in zip(df_desc[:length], df_desc[::-1]):
        result.append(match[0].tolist())
        result.append(match[1].tolist())

    result = pd.DataFrame(result)
    result.columns = df.columns
    return result

def load_data(file):
    for i, row in process_data(file).iterrows():

        new_team = ActiveTeam(title=row["title"], link=row["link"], prev_score=row["score"], round_number=0, rank=i)
        new_team.save()

def delete_data():
    for value in ActiveTeam.objects.all():
        value.delete()