from beanie.odm.fields import PydanticObjectId
from fastapi import APIRouter

from src.models.post import Post

router = APIRouter(prefix='/api/v1/posts', tags=['posts'])


@router.post('/', response_description='Create new post')
async def post_create(post: Post) -> None:
    await post.insert()


@router.get('/', response_description='Get all posts')
async def post_list() -> list:
    posts = await Post.find().to_list()

    return posts


# @router.get('/{id}', response_description='Get post by id')
# async def post_detail(id: PydanticObjectId) -> None:
#     pass


# @router.put('/{id}', response_description='Update post')
# async def post_update(id: PydanticObjectId, post: Post) -> None:
#     post_detail = await Post.get(id)

#     await post.save()


@router.delete('/{id}', response_description='Delete post')
async def post_delete(id: PydanticObjectId) -> None:
    post = await Post.get(id)

    await post.delete()
