from django import template

register = template.Library()


@register.inclusion_tag('blog_index.html')
def unique(posts):
    List = []
    for post in posts:
        for category in post.categories.all:
            if category.name not in List:
                List.append(category.name)
    names = List
    return {'tags': tags}
        



