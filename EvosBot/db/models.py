from db.configs import DB


class User(DB):

    def __init__(self,
                 *cols,
                 id: int = None,
                 user_id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 phone_number: str = None,
                 username: str = None,
                 lang: str = None,
                 created_at: str = None,
                 ):
        self.cols = cols
        self.id = id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.username = username
        self.lang = lang
        self.created_at = created_at


class SiteSetting(DB):
    def __init__(self,
                 *cols,
                 id: int = None,
                 contact: str = None,
                 address: str = None,
                 description: str = None,
                 longitude: float = None,
                 latitude: float = None,
                 about_company: str = None,
                 logo: str = None
                 ):
        self.cols = cols
        self.id = id
        self.contact = contact
        self.address = address
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.about_company = about_company
        self.logo = logo


class Region(DB):
    def __init__(self, *cols,
                 id: int = None,
                 name: str = None,
                 ):
        self.cols = cols
        self.id = id
        self.name = name

    def work_place_list(self, choose_region):
        query = """
            select wp.name from regions r 
            join districts d on r.id = d.region_id
            join branches b on d.id = b.district_id
            join branches_workplace bw on bw.branches_id = b.id
            join workplaces wp on bw.work_place_id = wp.id
            where r.name = %s;
        """
        self.cur.execute(query, (choose_region,))
        return self.cur.fetchall()

    def district_list(self, choose_region: str, workplace: str):
        query = """
                    select d.name from regions r 
                    join districts d on r.id = d.region_id
                    join branches b on d.id = b.district_id
                    join branches_workplace bw on bw.branches_id = b.id
                    join workplaces wp on bw.work_place_id = wp.id
                    where r.name = %s and wp.name = %s;
                """
        self.cur.execute(query, (choose_region, workplace))
        return self.cur.fetchall()

    def branches_list(self, choose_region: str, workplace: str, district_name: str):
        query = """
                            select b.* from regions r 
                            join districts d on r.id = d.region_id
                            join branches b on d.id = b.district_id
                            join branches_workplace bw on bw.branches_id = b.id
                            join workplaces wp on bw.work_place_id = wp.id
                            where r.name = %s and wp.name = %s and d.name = %s;
                        """
        self.cur.execute(query, (choose_region, workplace, district_name))
        return self.cur.fetchall()


class Category(DB):
    def __init__(self, *cols,
                 id: int = None,
                 name: str = None
                 ):
        self.cols = cols
        self.id = id
        self.name = name


class Product(DB):
    def __init__(self, *cols,
                 id: int = None,
                 name: str = None,
                 discount: float = None,
                 price: float = None,
                 aksiya: bool = None,
                 description: str = None,
                 photo: str = None,
                 category_id: int = None,
                 ):
        self.cols = cols
        self.id = id
        self.name = name
        self.discount = discount
        self.price = price
        self.aksiya = aksiya
        self.description = description
        self.photo = photo
        self.category_id = category_id



