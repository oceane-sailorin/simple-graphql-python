from main import db


class Resident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    installed = db.Column(db.Boolean, default=False)
    installation_date = db.Column(db.Date)

    def resident_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "installed": self.installed,
            "installation_date": str(self.installation_date)
        }