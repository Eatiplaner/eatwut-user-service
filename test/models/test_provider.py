from app.model.provider import Provider
from test import BaseMock
from test.setup.data import provider_facebook, provider_youtube, \
    provider_instagram, provider_tiktok


class TestProviderModel(BaseMock):
    def test_create_provider_with_valid_data(self):
        provider = Provider(
            url="fake.com",
            display_on_profile=False
        )
        provider.save()

        assert provider.type == "unknown"

    def test_create_provider_with_facebook_url(self):
        provider_fb = Provider(**provider_facebook)
        provider_fb.save()

        # Check Generated type of url
        assert provider_fb.type == "facebook"

    def test_create_provider_with_youtube_url(self):
        provider_ytb = Provider(**provider_youtube)
        provider_ytb.save()

        # Check Generated type of url
        assert provider_ytb.type == "youtube"

    def test_create_provider_with_tiktok_url(self):
        provider_tt = Provider(**provider_tiktok)
        provider_tt.save()

        # Check Generated type of url
        assert provider_tt.type == "tiktok"

    def test_create_provider_with_instagram_url(self):
        provider_insta = Provider(**provider_instagram)
        provider_insta.save()

        # Check Generated type of url
        assert provider_insta.type == "instagram"

    def test_create_provider_with_missing_fields(self):
        with self.assertRaises(Exception):
            Provider(
                display_on_profile=False
            ).save()
