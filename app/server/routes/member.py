from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import os

from app.server.db_member import (
    db_add_member,
    db_delete_member,
    db_get_member,
    db_get_all,
    db_update_member,
)
from app.server.models.member import (
    ErrorResponseModel,
    ResponseModel,
    MemberSchema,
    UpdateMemberModel,
)

 
router = APIRouter()

@router.post("/", response_description="Member data added into the database")
async def add_member_data(member: MemberSchema = Body(...)):
        member = jsonable_encoder(member)
        new_member = await db_add_member(member)
        return ResponseModel(new_member, "Member added successfully.")


@router.get("/", response_description="Get all member")
async def get_all_member():
    member = await db_get_all()
    if member:
        return ResponseModel(member, "Member data retrieved successfully")
    return ResponseModel(member, "Empty list returned")


@router.get("/{id}", response_description="Member data retrieved")
async def get_member(id):
    member = await db_get_member(id)
    if member:
        return ResponseModel(member, "Member data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Member doesn't exist.")


@router.put("/{id}")
async def update_member(id: str, req: UpdateMemberModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_member = await db_update_member(id, req)
    if updated_member:
        return ResponseModel(
            "Member with ID: {} name update is successful".format(id),
            "Member name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the member data.",
    )


@router.delete("/{id}", response_description="Member data deleted from the database")
async def delete_member_data(id: str):
    deleted_member = await db_delete_member(id)
    if deleted_member:
        return ResponseModel(
            "Member with ID: {} removed".format(id), "Member deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Member with id {0} doesn't exist".format(id)
    )