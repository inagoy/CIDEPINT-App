"""Users seeds."""
from src.core.models.privileges import Role
from src.core.models.user import User
from src.core.models.user_role_institution import UserRoleInstitution
from src.core.database import db
from src.core.bcrypt import bcrypt


def create_admins():
    """Create a new admin user with super admin privileges."""
    super_admin_role = Role.query.filter_by(name="Super Admin").first()
    data = {
        "first_name": "Super",
        "last_name": "Admin",
        "email": "admin@example.com",
        "username": "admin_username",
        "password": "Admin123",
        "address": "78 nro 87",
        "phone_number": "2214785685",
        "gender": 'Masculino',
        "document_type": 'DNI',
        "document": '21233566',
        "auth_method": 'App',
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
    """
    create_admins()

    users_data = [
        {"first_name": "John",
         "last_name": "Doe",
         "email": "john@example.com",
         "username": "john_doe",
         "password":  "Password123",
         "address": "478 nro 123",
         "phone_number": "2219995685",
         "gender": 'Masculino',
         "document_type": 'DNI',
         "document": '40233566',
         "auth_method": 'App',
         "active": True,
         },


        {"first_name": "Jane",
         "last_name": "Smith",
         "email": "jane@example.com",
         "username": "jane_smith",
         "password":  "Password123",
         "address": "148 nro 456",
         "phone_number": "1545785685",
         "gender": 'Femenino',
         "document_type": 'DNI',
         "document": '39233566',
         "auth_method": 'App',
         "active": True,
         },

        {"first_name": "Juan Ignacio",
         "last_name": "Perez",
         "email": "juaniperez@example.com",
         "username": "juaniperez",
         "password":  "Password123",
         "address": "13 nro 789",
         "phone_number": "2214785686",
         "gender": 'Masculino',
         "document_type": 'DNI',
         "document": '21233561',
         "auth_method": 'App',
         "active": True
         }
    ]

    for user_data in users_data:
        user_data["password"] = (bcrypt.generate_password_hash
                                 (user_data["password"].encode("utf-8")))
        user = User.save(**user_data)
        print(f"Created user: {user.first_name} {user.last_name}")

    owner = Role.query.filter_by(name="Owner").first()
    administrator = Role.query.filter_by(name="Administrator").first()
    operator = Role.query.filter_by(name="Operator").first()
    UserRoleInstitution.insert(
        role_id=owner.id,
        user_id=2,
        institution_id=1
    )
    UserRoleInstitution.insert(
        role_id=administrator.id,
        user_id=3,
        institution_id=1
    )
    UserRoleInstitution.insert(
        role_id=operator.id,
        user_id=4,
        institution_id=1
    )
