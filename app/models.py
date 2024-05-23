from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Company(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    body: so.Mapped[Optional[str]] = so.mapped_column(sa.String(512))
    phone: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32))

    flats: so.WriteOnlyMapped['Flat'] = so.relationship(back_populates='author')

    def __repr__(self):
        return f'Company: {self.name}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Flat(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    f_type: so.Mapped[str] = so.mapped_column(sa.String(32))
    price: so.Mapped[str] = so.mapped_column(sa.String(16), index=True)
    address: so.Mapped[str] = so.mapped_column(sa.String(64))
    square: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), index=True)
    num_of_rooms: so.Mapped[Optional[int]]
    body: so.Mapped[Optional[str]] = so.mapped_column(sa.String(512))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    company_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Company.id), index=True)

    author: so.Mapped[Company] = so.relationship(back_populates='flats')

    def __repr__(self):
        return f'Flat {self.f_type} {self.price}'

    @login.user_loader
    def load_user(id):
        return db.session.get(Company, int(id))
