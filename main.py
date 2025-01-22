from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.playstore import get_app_details
from src.get_important_info import extract_important_info
from src.gambling_or_gamming import extract_important_gg
from src.get_important_info_permissions import extract_important_info_permissions
from src.get_important_info_reviews import extract_important_info_reviews
import asyncio
import json

app = FastAPI()
app.add_middleware(
    allow_origins=["*"],
    CORSMiddleware,
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

@app.get("/classify")
async def classify_game_gamble(game_name: str):
    app_info, app_permissions, app_reviews = await get_app_details(game_name)

    from_description = await extract_important_info(app_info)

    from_permissions = await extract_important_info_permissions(app_permissions)

    from_reviews = await extract_important_info_reviews(app_reviews)

    result = await extract_important_gg("Information from description " + from_description + 
                                        " Information from permissions " + from_permissions + 
                                        " Information from reviews " + from_reviews)
    return {"result": json.loads(result)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
