# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from geonode.urls import urlpatterns
from django.urls import include, path

try: 
    from django.views.generic import TemplateView
    from homecollections.models import HomeCollection

    class HomePageView(TemplateView):
        template_name = "index.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['collections'] = HomeCollection.objects.all()
            return context
        
    urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
    ] + urlpatterns
except Exception as e:
    print(e)
    pass

try:
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail import urls as wagtail_urls
    from wagtail.documents import urls as wagtaildocs_urls
    if wagtail_urls not in urlpatterns:
        urlpatterns += [
            path('cms/', include(wagtailadmin_urls)),
            path('documents/', include(wagtaildocs_urls)),
            path('pages/', include(wagtail_urls)),
        ] 
except Exception as e:
    print(e)
    pass