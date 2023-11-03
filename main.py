from fastapi import FastAPI
import uvicorn
import random


players = ['Peter','Enes','Rick']

app = FastAPI()

@app.get("/{player}")
async def get_player(player: str):
    oponents = [item for item in players if item != player]
    oponent = random.choice(oponents)
    players.remove(oponent)
    return {"Your oponent is": oponent}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
