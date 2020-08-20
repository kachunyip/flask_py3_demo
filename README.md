# simple social blog demo

##### set a email account in config.py to send message 

```python
flask shell
from app import db
db.drop_all()
db.create_all()

Role.insert_roles()

from app import fake
fake.users(20)
fake.posts(50)

User.add_self_follows()

``` 