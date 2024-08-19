from app.model.db_control import GroupDTO
from app.utils.main import CrudAbstract


class Group(GroupDTO, CrudAbstract):

    def save(self):
        groups: list[Group] = self.read()
        groups.append(self)
        self.write(groups)

    def update(self, field, new_val):
        groups: list[Group] = self.read()
        for group in groups:
            if group.id == self.id:
                if field == "username":
                    group.username = new_val
                if field == "status":
                    group.status = new_val
                if field == "name":
                    group.name = new_val
                if field == "bio":
                    group.bio = new_val
                if field == "link":
                    group.link = new_val
                if field == "photo":
                    group.photo = new_val

    def delete(self):
        groups: list[Group] = self.read()
        for group in groups:
            if group.id == self.id:
                groups.remove(group)

    def get(self):
        groups: list[Group] = self.read()
        for group in groups:
            if group.id == self.id:
                return group