import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from . import db


__all__ = ['User', 'Role', '__tables']


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
    realname = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    gender = db.Column(db.SmallInteger, default=0)    # 0:Secret 1:M 2:F
    age = db.Column(db.SmallInteger)
    register_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        pass

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return dict(id=self.id, username=self.username)

    def __repr__(self):
        return '<User, username: {}, role: {}>'.format(self.username, self.role.name)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role, name: {}, id: {}>'.format(self.name, self.id)

    @staticmethod
    def add_test_data():
        super_role = Role(name='Super')
        admin_role = Role(name='Admin')
        user_role = Role(name='User')
        super_user = User(username='super', password='super', role=super_role)
        admin_user = User(username='admin', password='admin', role=admin_role)
        user_user = User(username='user', password='user', role=user_role)

        db.session.add_all([super_role, admin_role, user_role, super_user, admin_user, user_user])
        db.session.commit()


__tables = {
    'users': User
}
