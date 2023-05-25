from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.sessions.models import Session


# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name


class BaseNetwork(models.Model):
    icon_chois = (
        ('fab fa-facebook-f', "Facebook"),
        ('fa-brands fa-instagram', "Instagram"),
        ('fa-brands fa-telegram', "Telegram"),
        ('fa-brands fa-github', "Github"),
        ('fab fa-youtube', "Youtube"),
        ('fa-brands fa-linkedin', "LinkedIn"),
        ('fab fa-twitter', "Twitter"),
        ('fab fa-dribbble', "Web"),
    )
    icon = models.CharField(max_length=80, choices=icon_chois)
    link = models.URLField()

    def __str__(self):
        return self.icon


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Base(models.Model):
    icon = models.ImageField(upload_to='web_icon', default="web_icon/ali3.jpg", blank=True)
    title = models.CharField(max_length=255, default='Base Title', blank=True)
    copyright = models.ForeignKey(Network, on_delete=models.SET_NULL, related_name='copyright', null=True, blank=True)
    network = models.ManyToManyField(BaseNetwork, related_name='basenetwork')
    header_network = models.ManyToManyField(Network, related_name="header_network")
    header_network_header = models.CharField(max_length=60, default="Ijtimoiy havolalar:")

    def __str__(self):
        return "base.html"


class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='portfolio')
    description = RichTextField()
    github_link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    coloborator = models.ManyToManyField(Network)
    tag = models.ManyToManyField(Tag)
    view = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.id)])

    def increment_view_count(self, request):
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)
        if not self.postview_set.filter(session=session):
            self.view += 1
            self.save()

            PostView.objects.create(post=self, session=session)


class PostView(models.Model):
    post = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.post


class Index(models.Model):
    title1 = models.CharField(max_length=60, blank=True, null=True)
    title2 = models.CharField(max_length=60, blank=True, null=True)
    header_buy = models.CharField(max_length=30, blank=True, null=True)
    header_buy_hover = models.CharField(max_length=30, blank=True, null=True)
    title_discription = models.CharField(max_length=255, blank=True, null=True)
    head_img = models.ImageField(upload_to='head_img', blank=True, null=True)
    title_footer = models.CharField(max_length=80, blank=True, null=True)
    title_footer_link = models.URLField(blank=True, null=True)
    title_footer_hover = models.CharField(max_length=80, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    contact = models.ForeignKey(Network, on_delete=models.SET_NULL, blank=True, null=True)
    portfolio_h3 = models.CharField(max_length=60, blank=True, null=True)
    portfolio_h2 = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return "index.html"


class Comment(models.Model):
    post = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.CharField(max_length=60)
    body = models.CharField(max_length=2000)
    email = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.post} -> {self.user}"

    class Meta:
        ordering = '-created',


class About(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=84)
    img = models.ImageField(upload_to='about_img/')
    description = RichTextField()


class Contact_msg(models.Model):
    Option = (
        ('fikr', 'Fikr-Mulohaza'),
        ('ijobiy', 'Ijobiy'),
        ('salbiy', 'Salbiy'),
        ('ish', 'Ish'),
        ('shaxsiy', 'Shaxsiy'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    option = models.CharField(choices=Option, max_length=30)
    message = models.TextField()


class Contact(models.Model):
    img_header = models.ImageField()
    contact_about = models.CharField(max_length=800)
    location = models.CharField(max_length=200)
    number = models.CharField(max_length=50)
    contact_link = models.URLField()
    contact_name = models.CharField(max_length=60)
    follow = models.ManyToManyField(BaseNetwork)


class PortfolioMedia(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True, blank=True)
    img = models.ImageField(upload_to='portfolio/img')

    def __str__(self):
        return self.portfolio.name
