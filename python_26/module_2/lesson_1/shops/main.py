categories = []
products = []


class Category:
    def __init__(self,
                 id = None,
                 name = None,
                 image = None):
        self.id = id
        self.name = name
        self.image = image

    def save(self):
        self.id = categories[-1].id + 1 if categories else 1
        categories.append(self)

    def delete(self):
        for category in categories:
            if category.id == self.id:
                categories.remove(category)



    def update(self , field , new_value):
        for category in categories:
            if category.id == self.id:
                if field == "name":
                    category.name = new_value
                elif field == "image":
                    category.image = new_value


    def get(self):
        for category in categories:
            if category.id == self.id:
                return category

    def search(self):
        result = []
        for category in categories:
            if self.name.lower() in category.name.lower():
                result.append(self)
        return result


while True:
    menu = """
        1) category
        2) product
        3) exit
        >>>"""
    key = input(menu)
    if key == "1":
        menu = """
            *) search
            1) add
            2) list
            3) update
            4) delete
            5) get
            0) back
            >>>"""
        match input(menu):
            case "*":
                name = input("search : ")
                filter = Category(name = name).search()
                for category in filter:
                    print(f"{category.id}) {category.name}")


            case "1":
                name = input("Name : ")
                image = input("Image : ")
                Category(name = name , image=image).save()
            case "2":
                print(categories)
            case "3":
                pass





    elif key == "2":
        pass

    elif key == "3":
        break





