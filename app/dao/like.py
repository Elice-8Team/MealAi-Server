from app.database.database import engine
from sqlalchemy.sql import text


def get_feed_likes(feed_id: int):
    with engine.connect() as conn:
        data = {"feed_id": feed_id}
        statement = text("""SELECT COUNT(*) FROM Likes WHERE feed_id = :feed_id""")
        likes = conn.execute(statement, data).scalar()
        return likes


def get_feed_likes_user(feed_id: int, user_id: int):
    with engine.connect() as conn:
        data = {"feed_id": feed_id, "user_id": user_id}
        statement = text(
            """SELECT COUNT(*) FROM Likes WHERE feed_id = :feed_id AND user_id = :user_id"""
        )
        result = conn.execute(statement, data).scalar()
        return result


def push_likes(feed_id: int, user_id: int):
    with engine.connect() as conn:
        data = {"feed_id": feed_id, "user_id": user_id}
        statement = text(
            """DELETE FROM Likes WHERE feed_id = :feed_id AND user_id = :user_id"""
        )
        conn.execute(statement, data)
        conn.commit()


def cancel_likes(feed_id: int, user_id: int):
    with engine.connect() as conn:
        data = {"feed_id": feed_id, "user_id": user_id}
        statement = text("""INSERT INTO Likes VALUES(:feed_id,:user_id)""")
        conn.execute(statement, data)
        conn.commit()


def delete_likes(session, feed_id: int):
    data = {"feed_id": feed_id}
    statement = text("""DELETE FROM Likes WHERE feed_id=:feed_id""")
    session.execute(statement, data)


def count_my_likes_feeds(user_id: int):
    with engine.connect() as conn:
        data = {"user_id": user_id}
        statement = text(
            """SELECT COUNT(*) AS feeds_num FROM Feed AS F LEFT OUTER JOIN Likes AS L ON F.feed_id = L.feed_id WHERE L.user_id = :user_id"""
        )
        result = conn.execute(statement, data)
        row = result.mappings().first()
        return row.feeds_num


def get_my_likes_feeds(user_id: int, skip: int, limit: int):
    with engine.connect() as conn:
        data = {"user_id": user_id, "skip": skip, "limit": limit}
        statement = text(
            """SELECT * FROM Feed AS F LEFT OUTER JOIN Likes AS L ON F.feed_id = L.feed_id WHERE L.user_id = :user_id ORDER BY F.created_at DESC, F.feed_id LIMIT :skip,:limit"""
        )
        result = conn.execute(statement, data)
        feeds = result.mappings().all()
        return feeds, count_my_likes_feeds(user_id)
