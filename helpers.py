from models import db, Title, Description, Photo, PublishTime, Post, Article

def get_index_page_data():
    titles = db.session.query(Title).all()
    photos = db.session.query(Photo).all()
    descriptions = db.session.query(Description).all()
    publish_times = db.session.query(PublishTime).all()

    data = {
        'titles': titles,
        'photos': photos,
        'descriptions': descriptions,
        'publish_times': publish_times,
    }

    result = []
    articles = db.session.query(Article).all()

    for article in articles:
        title = db.session.query(Title).filter(Title.id == article.title_id).first()
        photo = db.session.query(Photo).filter(Photo.id == article.photo_id).first()
        description = db.session.query(Description).filter(Description.id == article.description_id).first()
        publish_time = db.session.query(PublishTime).filter(PublishTime.id == article.publish_time_id).first()

        result.append({
            'id': article.id,
            'title_id': title.id,
            'title_name': title.name,
            'photo_id': photo.id,
            'photo_name': photo.photo,
            'description_id': description.id,
            'description_name': description.text,
            'publish_time_id': publish_time.id,
            'publish_time_datetime': publish_time.datetime,
        })

    data['result'] = result

    return data


# def get_post_data(post_id=post.id):



# def get_title():
#     titles =  db.session.query(Title).all()

#     result = []

#     for title in titles:
#         result.append({
#             'id': title.id,
#             'name': title.name,
#         })
#     return result

# def get_description():
#     descriptions = db.session.query(Description).all()
    
#     result = []

#     for description in descriptions:
#         title = db.session.query(Title).filter(
#             Title.id == description.title_id
#         ).first()

#         result.append({
#             'id': description.id,
#             'text': description.text,
#             'title_id': title.id
#         })

#     return result

# def get_images():
#     images = db.session.query(Photo).all()

#     result = []

#     for image in images:
#         image = db.session.query(Photo).filter(
#             Photo.id == image.photo
#         ).first()

#         result.append({
#             'id': image.id,
#             'image': image.photo
#         })

#     return result

    