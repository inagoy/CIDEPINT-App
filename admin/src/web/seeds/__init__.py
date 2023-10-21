"""Seeds the database with initial data."""
from . import institutions
from . import privileges
from . import users
from . import services
from . import config


def run_seeds():
    """
    Run seed scripts to populate the database with initial data.

    This function calls individual seed scripts for institutions, roles, users,
      and permissions to populate the database with initial data for testing
      and development purposes.

    Args:
        None

    Returns:
        None
    """
    print("Running seeds...")
    config.seed_site_config()
    privileges.seed_privileges()
    institutions.seed_institutions()
    services.seed_services()
    users.seed_users()
    services.seed_service_requests()
    services.seed_notes()
    print("Seeds Done!")
