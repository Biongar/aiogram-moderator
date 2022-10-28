from config.database.settings import database

from .models import UserModel

users = UserModel.__table__

class UserManager:
    async def get_all_users(self, limit: int = 10, offset: int = 0) -> list[UserModel]:
        query = users.select().limit(limit).offset(offset).order_by('username')
        return await database.fetch_all(query)
    
    async def get_by_id(self, pk: int) -> UserModel:
        query = users.select().where(users.c.id==pk)
        return await database.fetch_one(query)
    
    async def get_by_username(self, username: str) -> UserModel:
        query = users.select().where(users.c.username==username)
        return await database.fetch_one(query)
    
    async def increase_violations(self, pk: int):
        query = users.update().where(users.c.id==pk).values(rule_violations=users.c.rule_violations + 1)
        return await database.execute(query)
    
    async def promote_user(self, pk: int):
        query = users.update().where(users.c.id==pk).values(is_admin=True)
        return await database.execute(query)
    
    async def downgrade_user(self, pk: int):
        query = users.update().where(users.c.id==pk).values(is_admin=False)
        return await database.execute(query)
        
    async def ban_user(self, pk: int):
        query = users.update().where(users.c.id==pk).values(is_banned=True)
        return await database.execute(query)
    
    async def unban_user(self, pk: int):
        query = users.update().where(users.c.id==pk).values(is_banned=False, rule_violations=0)
        return await database.execute(query)
    
    async def create(self, user: UserModel):
        query = users.insert().values(**user)
        return await database.execute(query)

        