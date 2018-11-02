from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
	url(r'^', include('polls.urls')),
	url(r'^login', include('pages.urls')),
	url(r'^login', include('django.contrib.auth.urls')),
	url(r'^signup', include('users.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^blog/', include('blog.urls')),
]
