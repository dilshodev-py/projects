from app.model.db_control import ContactDTO
from app.model.user import User
from app.utils.main import CrudAbstract


class Contact(ContactDTO, CrudAbstract):
    def save(self):
        contacts: list[Contact] = self.read()
        contacts.append(self)
        self.write(contacts)
    @property
    def sequence_id(self):
        contacts : list[Contact]= self.read()
        return int(contacts[-1].id) + 1 if contacts else 1

    def update(self, field, new_val):
        contacts: list[Contact] = self.read()
        for contact in contacts:
            if contact.id == self.id:
                if field == "user_id":
                    contact.user_id = new_val
                if field == "phone_number":
                    contact.phone_number = new_val

    def delete(self):
        contacts: list[Contact] = self.read()
        for contact in contacts:
            if contact.id == self.id:
                contacts.remove(contact)

    def get(self):
        contacts: list[Contact] = self.read()
        for contact in contacts:
            if contact.id == self.id:
                return contact

    def owner_contact_list(self):
        contacts: list[Contact] = self.read()
        user_list: list[User] = []
        owner_contact: list = []
        for contact in contacts:
            if contact.owner_id == self.owner_id:
                owner_contact.append(contact.user_id)

        users: list[User] = User().read()
        for user in users:
            if user.id in owner_contact:
                user_list.append(user)
        return user_list

