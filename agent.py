from ScraperTools import tools


class Agent:
    def __init__(self, url, zip):
        self.zip = zip
        self.main_url = url
        self.main_soup = tools.get_soup(self.main_url)
        self.profile = self.get_profile()

    def get_profile(self):
        name = tools.get_elem(self.main_soup, "h1", "data-tn", "profile-name").get_text(),
        email = tools.get_elem(self.main_soup, "a", "data-tn", "profile-email"),
        phone = tools.get_elem(self.main_soup, "a", "data-tn", "profile-phone"),
        facebook = self.main_soup.select('a[href*="facebook.com/"]')[0].attrs["href"],
        instagram = self.main_soup.select('a[href*="instagram.com/"]')[0].attrs["href"]
        if phone is None:
            phone = "None"
        else:
            phone = phone[0].attrs["href"].replace("tel:", "")
        if isinstance(facebook, tuple):
            facebook = facebook[0]
        if isinstance(instagram, tuple):
            instagram = instagram[0]
        #linkedin = self.main_soup.select('a[href*="linkedin.com/"]')[0].attrs["href"]
        profile = {
            "zip": self.zip,
            "name": name[0] if name else None,
            "email": email[0].attrs["href"].replace("mailto:", "") if email is not None else None,
            "phone": phone,
            "facebook": facebook if facebook else None,
            "instagram": instagram if instagram else None,
        #    "linkedin": linkedin if linkedin else None,
            "url": self.main_url

        }
        return profile
