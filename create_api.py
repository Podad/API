from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey

name_db = input(str("Entre une bdd : "))

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = ""
MYSQL_DB = name_db

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,
                                                                  MYSQL_PWD,
                                                                  MYSQL_HOST,
                                                                  MYSQL_PORT,
                                                                  MYSQL_DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base, name_db): #Structure table User

    __tablename__ = name_db
    id = Column(int(40),unique=True, nullable=False,primary_key=True)
    nom = Column(String(80), nullable=False)
    prenom = Column(String(80), nullable=False)


class Info(Base, name_db):  # Structure table Information

    __tablename__ = name_db
    email = Column(String(120), nullable=False)
    ville = Column(String(80), nullable=False)
    telephone = Column(String(80), nullable=False)
    age = Column(int(80),nullable=False)
    taille = Column(int(80),nullable=False)
    pointure = Column(int(80),nullable=False)


def add_user(email, nom, prenom, ville, telephone):
    try:
        user = User(email=email,
                    nom=nom,
                    prenom=prenom,
                    ville=ville,
                    telephone=telephone)
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_user_by_id(email):
    try:
        result = session.query(User).filter_by(email=email).first()
        return result
    except Exception as e:
        print(e)
        return False


def get_all_users():
    try:
        result = session.query(User).filter_by()
        return result
    except Exception as e:
        print(e)
    return False


def delete_user_by_id(email):
    try:
        user_to_delete = get_user_by_id(email)
        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def update_attribute(email, attributes):
    try:
        user_to_update = get_user_by_id(email)
        if user_to_update:
            for k, v in attributes.items():
                setattr(user_to_update, k, v)
                session.commit()
            return user_to_update
        else:
            return False
    except Exception as e:
        print(e)
        return False


# Test 2
# Warpper

# app = Flask(__name__)
#
#
# @app.route('/api/v1/user/', methods=['POST'])
# def create_user():
#     # On recupere le corps (payload) de la requete
#     payload = request.form.to_dict()
#     result = wrapper.add_user(**payload)
#     if result:
#         return jsonify(status='True', message='User created')
#         return jsonify(status='False')
#
#
# @app.route('/api/v1/user/', methods=['GET'])
# def get_all_users():
#     result = wrapper.get_all_users()
#     if result:
#         return jsonify(status="True",
#                        result=[
#                            {"nom": user.nom,
#                               "prenom": user.prenom,
#                               "email": user.email,
#                             "ville": user.ville,
#                             "telephone": user.telephone}
#                            for user in result.all()])
#     return jsonify(status="False")
#
#
# @app.route('/api/v1/user/&amp;amp;amp;amp;lt;email&amp;amp;amp;amp;gt;', methods=['GET'])
# def get_user(email):
#     result = wrapper.get_user_by_id(email)
#     if result:
#         return jsonify(status="True",
#                        result={"nom": result.nom,
#                                "prenom": result.prenom,
#                                "email": result.email,
#                                "ville": result.ville,
#                                "telephone": result.telephone}
#                        )
#         return jsonify(status="False")
#
#
# @app.route('/api/v1/user/&amp;amp;amp;amp;lt;email&amp;amp;amp;amp;gt;', methods=['PUT'])
# def mofify_user(email):
#     result = wrapper.update_attribute(email, request.form.to_dict())
#     if result:
#         return jsonify(status="True",
#                        message="updated",
#                        result={
#                            "nom": result.nom,
#                            "prenom": result.prenom,
#                                "email": result.email,
#                                "ville": result.ville,
#                                "telephone": result.telephone}
#                        )
#         return jsonify(status="False")
#
#
# @app.route('/api/v1/user/&amp;amp;amp;amp;lt;email&amp;amp;amp;amp;gt;', methods=['DELETE'])
# def delete_user(email):
#     result = wrapper.delete_user_by_id(email)
#     if result:
#         return jsonify(status="True",
#                        message="Deleted",
#                        email=email
#                        )
#         return jsonify(status="False")
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
