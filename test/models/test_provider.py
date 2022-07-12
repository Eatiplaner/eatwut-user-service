from app.model.provider import Provider
from test import BaseMock


class TestProviderModel(BaseMock):
    def test_create_provider_with_valid_data(self):
        provider = Provider(
            url="fake.com",
            display_on_profile=False
        )
        provider.save()

        assert provider.type == "unknown"

    def test_create_provider_with_facebook_url(self):
        provider_facebook = Provider(
            url="https://www.facebook.com/bavuongdaradi.3990",
            display_on_profile=True
        )
        provider_facebook.save()

        # Check Generated type of url
        assert provider_facebook.type == "facebook"

    def test_create_provider_with_youtube_url(self):
        provider_youtube = Provider(
            url="https://www.youtube.com/channel/UCctlr1pyEUxjXKbLwa0Xz4A",
            display_on_profile=True
        )
        provider_youtube.save()

        # Check Generated type of url
        assert provider_youtube.type == "youtube"

    def test_create_provider_with_tiktok_url(self):
        provider_tiktok = Provider(
            url="https://vt.tiktok.com/ZSReaombM/",
            display_on_profile=True
        )
        provider_tiktok.save()

        # Check Generated type of url
        assert provider_tiktok.type == "tiktok"

    def test_create_provider_with_instagram_url(self):
        provider_instagram = Provider(
            url="https://instagram.com/im.khoms/",
            display_on_profile=True
        )
        provider_instagram.save()

        # Check Generated type of url
        assert provider_instagram.type == "instagram"

    def test_create_provider_with_missing_fields(self):
        with self.assertRaises(Exception):
            Provider(
                display_on_profile=False
            ).save()
