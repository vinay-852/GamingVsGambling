from google_play_scraper import app, Sort, reviews, reviews_all, permissions, search
import asyncio

# Get app from search
async def get_appId_from_search(query, lang="en", country="us", n_hits=1):
    result = await asyncio.to_thread(search, query, lang=lang, country=country, n_hits=n_hits)
    return result[0]['appId']

# Get app info
async def get_app_info(appId, lang="en", country="us"):
    app_info = await asyncio.to_thread(app, appId, lang=lang, country=country)
    return app_info

# Get all reviews of an app
async def get_reviews(appId, lang="en", country="us"):
    result = await asyncio.to_thread(reviews, appId, lang=lang, country=country, count=50, sort=Sort.MOST_RELEVANT)
    return result

# Get all permissions of an app
async def get_permissions(appId, lang="en", country="us"):
    result = await asyncio.to_thread(permissions, appId, lang=lang, country=country)
    return result

# Get app details including description, permissions, and reviews
async def get_app_details(query, lang="en", country="us"):
    app_id = await get_appId_from_search(query, lang, country)
    app_info = await get_app_info(app_id, lang, country)
    app_permissions = await get_permissions(app_id, lang, country)
    app_reviews = await get_reviews(app_id, lang, country)
    return app_info, app_permissions, app_reviews
