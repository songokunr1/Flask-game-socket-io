from app import db


class User(db.Model):
    """User model"""
    """ doc
    from app import db
    from models import User
    db.create_all()
    user_1 = User(username="pawel", password="pawel")
    db.session.add(user_1)
    db.session.commit()
    User.query.all()
    User.query.filter_by(username="pawel').all() #list of object
    User.query.filter_by(username="pawel').first() # element (object)
    user = User.query.filter_by(username="pawel').first()
    user.id
    
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25))

    def __repr__(self):
        return f"{self.username}"


# gracz 1
#: karty w rece, id gracza, name,(player1, cpu)
# sprawdzanie czy gracz ma jeszcze jakieś karty w rączce


# obiekt gra
# karta, id, nr
#methody:
# lista kart w kolejności rosnącej,
# usuwanie ostatniej karty
# czy sprawdzanie czy karty są jeszcze na kupce
#

# środek
# jedna rekord, aktualna karta na środku
# wyciąganie i podmienianie
