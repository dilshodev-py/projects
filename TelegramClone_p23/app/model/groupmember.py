from app.model.db_control import GroupMemberDTO
from app.utils.main import CrudAbstract


class GroupMember(GroupMemberDTO, CrudAbstract):

    def save(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_val):
        pass

    def get(self):
        pass