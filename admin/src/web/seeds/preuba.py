from src.core.models.role import Role
from src.core.models.user import User, user_role_institution
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
    db.session.execute(user_role_institution.insert().values(
        role_id=super_admin_role.id,
        user_id=super_admin.id,
    ))

    db.session.commit()

    create_admins()