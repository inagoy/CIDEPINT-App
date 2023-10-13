from src.core.database import db
from datetime import datetime


class SiteConfig(db.Model):
    __tablename__ = "site_config"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    items_per_page = db.Column(db.Integer, default=100)
    contact_info = db.Column(db.String(255))
    maintenance_mode = db.Column(db.Boolean, default=False)
    maintenance_message = db.Column(db.Text)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def save(cls, **kwargs) -> object:
        site_config = SiteConfig(**kwargs)
        db.session.add(site_config)
        db.session.commit()
        return site_config

    @classmethod
    def get_config(cls) -> object:
        site_config = cls.query.first()
        return site_config

    @classmethod
    def update(cls, **kwargs) -> object:
        site_config = cls.query.first()
        if site_config:
            for key, value in kwargs.items():
                setattr(site_config, key, value)
            site_config.updated_at = datetime.utcnow()
            db.session.add(site_config)
            db.session.commit()
        return site_config

    @classmethod
    def in_maintenance_mode(cls) -> bool:
        site_config = cls.query.first()
        return site_config.maintenance_mode

    @classmethod
    def get_items_per_page(cls) -> int:
        site_config = cls.query.first()
        return site_config.items_per_page

    @classmethod
    def get_maintenance_message(cls) -> str:
        site_config = cls.query.first()
        return site_config.maintenance_message

    @classmethod
    def get_contact_info(cls) -> str:
        site_config = cls.query.first()
        return site_config.contact_info
