def user_schema(user)->dict:
  return {
    "id": user["_id"],
    "username": user["username"],
    "email": user["email"]
  }
