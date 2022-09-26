from django.contrib import admin
from home.models import interactionrating, languagerating, review
from home.models import rating,qualityrating
from home.models import Info
from home.models import pageinfo


# Register your models here.
admin.site.register(review);
admin.site.register(rating);
admin.site.register(Info);
admin.site.register(pageinfo);
admin.site.register(languagerating);
admin.site.register(interactionrating);
admin.site.register(qualityrating);




