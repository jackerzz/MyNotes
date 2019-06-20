from . import OAuth_Base


class OAuth_WEIXIN(OAuth_Base):
    def get_auth_url(self):
        pass

    def get_access_token(self, code):
        pass

    def get_open_id(self):
        pass

    def get_user_info(self):
        pass

    def get_email(self):
        pass
