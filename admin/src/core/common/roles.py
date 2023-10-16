from src.core.models.privileges import Role
from src.core.models.user_role_institution import UserRoleInstitution


def is_superuser(user_id) -> bool:
    role = UserRoleInstitution.get_roles_institutions_of_user(user_id=user_id)
    raise NotImplementedError
    if not role:
        return False
    return Role.get_role_by_id(id=role[0].id).name == "Super Admin"
