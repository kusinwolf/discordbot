# Third party imports
import sqlalchemy

# Application imports
from models import database


class Feeds(database.Base):
    __tablename__ = "feeds"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, nullable=False
    )
    streamer_name = sqlalchemy.Column(
        sqlalchemy.String, unique=True, nullable=False
    )
    delivery_message = sqlalchemy.Column(sqlalchemy.String)
    post_to_channel = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        """
        Custom String representation

        :returns: String representation of the data
        :rtype: str
        """
        return "<Feed(id='{id}', username='{streamer_name}')>".format(
            **self.__dict__
        )

    def to_dict(self):
        """
        Custom Dictionary/Json-able representation

        :returns: Dict representation of the data
        :rtype: dict
        """
        return {
            "id": self.id,
            "streamer_name": self.streamer_name,
            "delivery_message": self.delivery_message,
            "post_to_channel": self.post_to_channel,
        }
