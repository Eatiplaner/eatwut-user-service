def auto_increment_id(func):
    def inner(cls, sender, document, **kwargs):
        document.ID = cls.objects.count() + 1

        return func(cls, sender, document, **kwargs)

    return inner
