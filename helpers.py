from models import db, Title, Description, Photo, PublishTime, Post, Article

def get_index_page_data():
    # Извлекаем все данные для связей в один раз
    titles = {title.id: title.name for title in db.session.query(Title).all()}
    photos = {photo.id: photo.photo for photo in db.session.query(Photo).all()}
    descriptions = {description.id: description.text for description in db.session.query(Description).all()}
    publish_times = {time.id: time.datetime for time in db.session.query(PublishTime).all()}
    # Извлекаем все статьи
    articles = db.session.query(Article).all()

    # Формируем результат
    result = []
    for article in articles:
        # Получаем значения из словарей, если ключ существует, иначе присваиваем значение по умолчанию
        title_name = titles.get(article.title_id, 'Unknown Title')
        photo_name = photos.get(article.photo_id, 'images/bad.jpeg')  # Укажите реальный путь к фото по умолчанию
        description_name = descriptions.get(article.description_id, 'No description available')
        publish_time_datetime = publish_times.get(article.publish_time_id, 'Unknown Time')


        result.append({
            'id': article.id,
            'title_id': article.title_id,
            'title_name': title_name,
            'photo_id': article.photo_id,
            'photo_name': photo_name,
            'description_id': article.description_id,
            'description_name': description_name,
            'publish_time_id': article.publish_time_id,
            'publish_time_datetime': publish_time_datetime,
            'post_id': article.post_id,
        })

    data = {
        'result': result
    }

    return data



def get_post_data(post_id):
    result = []
    post = db.session.query(Post).filter_by(id=post_id).first()

    title = db.session.query(Title).filter_by(id=post.title_id).first()
    photo = db.session.query(Photo).filter_by(id=post.photo_id).first()
    publish_time = db.session.query(PublishTime).filter_by(id=post.publish_time_id).first()


    result.append ({
            'id': post.id,
            'text': post.text,
            'comment': post.comment,
            'title_name': title.name,
            'photo_name': photo.photo,
            'publish_time': publish_time.datetime,
    })

    data = {'result':result}
    return data


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

    