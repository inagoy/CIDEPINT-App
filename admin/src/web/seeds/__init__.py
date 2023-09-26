from . import institutions
from . import privileges
from . import users
from . import services


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
    privileges.seed_privileges()
    institutions.seed_institutions()
    services.seed_services()
    users.seed_users()
    print("Seeds Done!")
