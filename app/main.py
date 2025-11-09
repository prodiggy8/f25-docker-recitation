from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

MICROSERVICE_LINK = "https://appbox.qatar.cmu.edu/313-teams/team_name/"

MENTORS = ["Seckhen", "Aadi", "Steve", "Seckhen", "Aadi", "Steve"]

@app.get("/team_info/{team_id}")
def get_team_info(team_id: str):

    if team_id is None:
        raise HTTPException(status_code=404, detail="Missing team id")

    team_id = team_id.lower()

    response = requests.get(MICROSERVICE_LINK + team_id)
    # You can check out what the response body looks like in the terminal using the print statement
    data = response.json()

    team_name = data.get("team_name", None)

    # Fix this to return correct values for correct team ids.
    if team_name != None:
        return {
            "team_id" : team_id,
            "team_name": team_name,
            "mentor": MENTORS[int(team_id) - 1]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid team id")
