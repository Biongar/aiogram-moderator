from sqlalchemy import Column, Integer, String, Boolean # , ForeignKey

from config.database.settings import Base

class UserModel(Base):
    __tablename__ = 'account_user'
    
    id = Column(Integer, primary_key=True, autoincrement=False, unique=True)
    username = Column(String(255), nullable=False, unique=True)
    rule_violations = Column(Integer, nullable=False, server_default='0')
    is_banned = Column(Boolean, nullable=False, server_default='false')
    is_admin = Column(Boolean, nullable=False, server_default='false')
    
    
''' TODO
Модель которая будет содержать в себе текст сообщения содержащего оскорбительный 
или неприемлемый контент, чтобы в будущем можно было посмотреть наглядно за что пользователь 
получил нарушение правил. 

class MessageModel(Base):
    id = Column(Integer, primary_key=True)
    text = Column(String(), nullable=False)
    user_created = Column(Integer, ForeignKey('account_user.id'))
''' 