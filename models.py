from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP

db = SQLAlchemy()
Base = db.Model

class Title(Base):
    __tablename__ = 't_title'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Description(Base):

    __tablename__ = 't_description'

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    title_id = Column(Integer, ForeignKey('t_title.id'))

class Photo(Base):
    __tablename__ = 't_photo'

    id = Column(Integer, primary_key=True)
    photo = Column(Text)
    title_id = Column(Integer, ForeignKey('t_title.id'))

class PublishTime(Base):
    __tablename__ = 't_publish_time'

    id = Column(Integer, primary_key=True)
    datetime = Column(TIMESTAMP)
    title_id = Column(Integer, ForeignKey('t_title.id'))

class Post(Base):
    __tablename__ = 't_post'

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    comment = Column(Text)
    title_id = Column(Integer, ForeignKey('t_title.id'))
    photo_id = Column(Integer, ForeignKey('t_photo.id'))
    publish_time_id = Column(Integer, ForeignKey('t_publish_time.id'))

class Article(Base):
    __tablename__ = 't_article'

    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('t_title.id'))
    photo_id = Column(Integer, ForeignKey('t_photo.id'))
    publish_time_id = Column(Integer, ForeignKey('t_publish_time.id'))
    description_id = Column(Integer, ForeignKey('t_description.id'))
    post_id = Column(Integer, ForeignKey('t_post.id'))