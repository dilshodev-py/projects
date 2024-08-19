from app.model.db_control import ChannelMemberDTO
from app.utils.main import CrudAbstract


class ChannelMember(ChannelMemberDTO, CrudAbstract):
    def save(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_val):
        pass

    def get(self):
        pass