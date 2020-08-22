from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    # 文章列表显示更详细的信息
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    # 表单展现的字段
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
