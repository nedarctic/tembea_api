from django.contrib import admin
from .models import Site, SiteImage, SiteActivity, Eatery, MenuItem, EateryImage

##Models associated with sites
admin.site.register(Site)
admin.site.register(SiteImage)
admin.site.register(SiteActivity)

##Models associated with eateries

admin.site.register(Eatery)
admin.site.register(MenuItem)
admin.site.register(EateryImage)
