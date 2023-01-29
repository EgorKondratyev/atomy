from django.contrib import admin

from admin_panel.models import Users, Sentences
from django.utils.safestring import mark_safe

admin.site.site_title = 'Веб админ-панель для управление ботом Atomy'
admin.site.site_header = 'Веб админ-панель для управление ботом Atomy'


class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_id', 'full_name', 'get_language_html', 'city', 'sex', 'email')
    list_display_links = ('pk', 'user_id',)
    search_fields = ('user_id', 'full_name')
    list_filter = ('language', )

    fields = ('user_id', 'get_username', 'get_language_html', 'city', 'full_name', 'sex', 'birth_date', 'phone_number',
              'postal_code', 'address', 'email', 'purpose_registration')
    readonly_fields = ('user_id', 'get_language_html', 'city', 'full_name', 'sex', 'birth_date', 'phone_number',
                       'postal_code', 'address', 'email', 'purpose_registration', 'get_username')

    def get_queryset(self, request):
        qs = super(UsersAdmin, self).get_queryset(request)
        return qs.filter(register_status=True)

    def get_language_html(self, object):
        if object.language:
            return 'Русский'
        else:
            return 'Английский'
    get_language_html.short_description = 'Язык'

    def get_username(self, object):
        if object.username:
            return f'ID: {object.username} | Ссылка: https://t.me/{object.username[1:]}'
    get_username.short_description = 'Ссылка на аккаунт'


admin.site.register(Users, UsersAdmin)


class SentencesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type_sentence', 'get_language_html', 'sentence', 'get_html_photo')
    list_display_links = ('pk', 'type_sentence')
    search_fields = ('type_sentence', 'sentence')
    ordering = ['pk']
    fieldsets = (
        (None, {
            'fields': ('sentence', 'get_html_photo', 'photo')
        }),
        ('Дополнительная информация', {
            'classes': ('collapse',),
            'fields': ('type_sentence', 'get_language_html'),
        }),
    )
    readonly_fields = ('type_sentence', 'get_language_html', 'get_html_photo')
    empty_value_display = 'Пусто'
    list_max_show_all = 250
    list_per_page = 160

    def get_language_html(self, object):
        if object.language:
            return 'Русский'
        else:
            return 'Английский'
    get_language_html.short_description = 'Язык'

    def get_html_photo(self, object):
        if object.photo:
            print(object.photo.url)
            return mark_safe(f'<img src="{object.photo.url}" width=50>')
    get_html_photo.short_description = 'Фото'

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Sentences, SentencesAdmin)
