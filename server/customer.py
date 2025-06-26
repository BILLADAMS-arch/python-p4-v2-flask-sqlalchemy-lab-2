class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='customer')

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'
