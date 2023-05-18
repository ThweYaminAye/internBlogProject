from django.contrib import admin
from . models import Post,PostImage


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','slug','status','created_on',)
#     list_filter = ('status',)
#     search_fields = ['title','content']
#     prepopulated_fields = {'slug':('title',)}
#
# admin.site.register(Post,PostAdmin)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
