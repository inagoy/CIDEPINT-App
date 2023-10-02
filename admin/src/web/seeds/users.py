from ...core.models.privileges import Role
from src.core.models.user import User
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.database import db


def create_admins():
    super_admin_role = Role.query.filter_by(name="Super Administrador").first()
    super_admin = User.save(
        first_name="Super",
        last_name="Admin",
        email="super_admin@example.com",
        username="super_admin_username",
        password="admin123"
    )
    UserRoleInstitution.insert(
        role_id=super_admin_role.id,
        user_id=super_admin.id
    )

    db.session.commit()


def seed_users() -> None:
    """
    Seed users in the database with initial data.

    This function populates the database with initial user data
    for testing and development purposes.

    Args:
        None

    Returns:
        None
    """

    users_data = [
        {"first_name": "John",
         "last_name": "Doe",
         "email": "john@example.com",
         "username": "john_doe",
         "password":  "12345678"
         },


        {"first_name": "Jane",
         "last_name": "Smith",
         "email": "jane@example.com",
         "username": "jane_smith",
         "password":  "password123"
         }
    ]

    for user_data in users_data:
        user = User.save(**user_data)
        print(f"Created user: {user.first_name} {user.last_name}")

    create_admins()
