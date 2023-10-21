"""Site Config seeds."""
from src.core.models.site_config import SiteConfig
from src.core.database import db


def seed_site_config() -> None:
    """
    Seed site config in the database with initial data.

    This function populates the database with initial site config data
    for testing and development purposes.
    """
    site_config_data = {}
    site_config = SiteConfig(**site_config_data)
    db.session.add(site_config)
    db.session.commit()
    print("Setting Empty Site Configuration")
