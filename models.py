import mongoengine as me

me.connect(host='mongodb+srv://kallutoname:63WfDdOjXrUHnYIM@cluster0.u1c0q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class Author(me.Document):
    fullname = me.StringField(required=True, unique=True)
    born_date = me.StringField()
    born_location = me.StringField()
    description = me.StringField()

class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, required=True)
    quote = me.StringField(required=True)
