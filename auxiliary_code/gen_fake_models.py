from faker import Faker

from web_app import db
from web_app.models import User, Post

fake = Faker()


def create_users(users_number=10, *, posts_per_user=0):
    users_to_add = list()
    for _ in range(users_number):
        new_user = User(username=fake.unique.first_name())
        db.session.add(new_user)
        users_to_add.append(new_user)
        # we don't want to call `db.session.commit()` here,
        # to prevent many db connections
        # at the same time we can't add `Posts` here,
        # because `User.id` will be set in database after calling `db.session.commit()`
    db.session.commit()
    # now user instances have assigned `User.id`

    for new_user in users_to_add:
        create_posts(posts_per_user, user_id=new_user.id)


def delete_all():
    User.query.delete()
    Post.query.delete()
    db.session.commit()


def create_posts(n=10, *, user_id=None):
    for _ in range(n):
        p = Post(content=fake.unique.text(), user_id=user_id)
        db.session.add(p)
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    delete_all()
    create_users(20, posts_per_user=10)
