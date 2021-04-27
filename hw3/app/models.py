from app import db

class User(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)
    #author
    author = db.Column(db.String(256))
    # message (linkd to Messages table)
    messages = db.relationship('Messages', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User: {}>'
        #f'<User{}>'

class Messages(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)
    # message (string, not unique, can't be null)
    messages = db.Column(db.String(256))
    # user_id link to id (int)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # write __repr__ that outputs
    def __repr__(self):
        return '<Message: {}>'.format(self.message)
    # <Message: MESSAGE_GOES_HERE>

