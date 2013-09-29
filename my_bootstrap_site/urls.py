from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bootstrap_example.views.home', name='home'),
    # url(r'^django_bootstrap_example/', include('django_bootstrap_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^/$', 'my_bootstrap_site.views.Home'),

    url(r'home$', 'my_bootstrap_site.views.Home'),

	url(r'say_my_name[/]$', 'my_bootstrap_site.views.SayMyName'),

	url(r'say_my_name/(?P<called_name>\w+)$', 'my_bootstrap_site.views.SayMyName'),
)
