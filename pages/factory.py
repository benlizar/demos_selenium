from pages.organization_page import PageOrganization
from pages.page_login import PageLogin


class PageFactory(object):
    login = PageLogin()
    organization = PageOrganization()
