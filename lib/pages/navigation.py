from lib.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Navigation(BasePage):
    HOME = (By.LINK_TEXT, 'Home')
    SERVICES = {
        'general': (By.LINK_TEXT, 'Services'),
        'dropdown': {
            'all_services': (By.LINK_TEXT, 'All Services'),
            'software_development': (By.LINK_TEXT, 'Software Development'),
            'qa': (By.LINK_TEXT, 'QA'),
            'big_data': (By.LINK_TEXT, 'Big Data'),
            'data_analytics': (By.LINK_TEXT, 'Data Analytics'),
            'data_science': (By.LINK_TEXT, 'Data Science'),
            'ux_ui_design': (By.LINK_TEXT, 'UX/UI Design'),
            'agile_product_management': (By.LINK_TEXT, 'Agile Product Management'),
            'product_design': (By.LINK_TEXT, 'Product Design'),
            'cloud_and_on_premises_devops': (By.LINK_TEXT, 'Cloud and On-premises DevOps')
        }
    }
    CAREERS = {
        'general': (By.LINK_TEXT, 'Careers'),
        'dropdown': {
            'jobs': (By.LINK_TEXT, 'Jobs'),
            'internship': (By.LINK_TEXT, 'Internship'),
            'atlanters_in_focus': (By.LINK_TEXT, 'Atlanters in Focus'),
            'culture': (By.LINK_TEXT, 'Culture')
        }
    }
    BLOG = {
        'general': (By.LINK_TEXT, 'Blogs'),
        'dropdown': {
            'all_blogs': (By.LINK_TEXT, 'All Blogs'),
            'software_development': (By.LINK_TEXT, 'Software Development'),
            'qa_test_automation': (By.LINK_TEXT, 'QA / Test Automation'),
            'big_data': (By.LINK_TEXT, 'Big Data'),
            'data_science_analytics': (By.LINK_TEXT, 'Data Science & Analytics'),
            'product_management': (By.LINK_TEXT, 'Product Management'),
            'ux_ui': (By.LINK_TEXT, 'UX/UI'),
            'tech_bites': (By.LINK_TEXT, 'Tech Bites'),
            'news': (By.LINK_TEXT, 'News')
        }
    }
    CONTACT = (By.LINK_TEXT, 'Contact')