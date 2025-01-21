from fastapi import FastAPI
from src.resource.user.api import user_router
from src.resource.post.api import user_post
from src.resource.comment.api import user_comment
from src.resource.follow.api import user_follow

app = FastAPI(title="SOCIAL_MEDIA_APP")

app.include_router(user_router)
app.include_router(user_post)
app.include_router(user_comment)
app.include_router(user_follow)