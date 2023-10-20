from src.core.models.privileges import Role
from src.core.models.user import User
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.database import db
from src.core.bcrypt import bcrypt


def create_admins():
    """
    Creates a new admin user with super admin privileges.

    Returns:
        None
    """
    super_admin_role = Role.query.filter_by(name="Super Admin").first()
    data = {
        "first_name": "Super",
        "last_name": "Admin",
        "email": "admin@example.com",
        "username": "admin_username",
        "password": "admin123",
        "address": "78 nro 87",
        "phone_number": "2214785685",
        "gender": 'Masculino',
        "document_type": 'DNI',
        "document": '21233566',
        "active": True
    }
    data["password"] = (bcrypt.generate_password_hash(data["password"]
                                                      .encode("utf-8")))
    super_admin = User.save(**data)
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
    create_admins()

    users_data = [
        {"first_name": "John",
         "last_name": "Doe",
         "email": "john@example.com",
         "username": "john_doe",
         "password":  "12345678",
         "address": "478 nro 123",
         "phone_number": "2219995685",
         "gender": 'Masculino',
         "document_type": 'DNI',
         "document": '40233566',
         "active": True,
         },


        {"first_name": "Jane",
         "last_name": "Smith",
         "email": "jane@example.com",
         "username": "jane_smith",
         "password":  "password123",
         "address": "148 nro 456",
         "phone_number": "1545785685",
         "gender": 'Femenino',
         "document_type": 'DNI',
         "document": '39233566',
         "active": True,
         }
    ]

    for user_data in users_data:
        user_data["password"] = (bcrypt.generate_password_hash
                                 (user_data["password"].encode("utf-8")))
        user = User.save(**user_data)
        print(f"Created user: {user.first_name} {user.last_name}")
