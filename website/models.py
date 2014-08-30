from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class Gig(models.Model):

    seller = models.ForeignKey(User)
    rating_avg = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)
    description = models.CharField(required=True, max_length=5000, min_length=250);
    category = models.ForeignKey('Category')
    sub_category = models.ForeignKey('SubCategory')
    tag = models.ManyToManyField('Tag')
    duration = models.IntegerField(default=0)
    instruction = models.CharField(required=False, max_length=5000)

    def __unicode__(self):
        return u'gig_id: {} ____ seller: {} ____ rating_avg: {} ____ rating_count: {} ____ category: {} ____ sub_category: {} ____ tag: {} ____ duration: {}'\
            .format(self.id, self.seller, self.rating_avg, self.rating_count, self.category, self.sub_category, self.tag, self.duration)


class Order(models.Model):
    buyer = models.ForeignKey(User)
    gig = models.ForeignKey(Gig)
    status = models.CharField(require=True)
    purchase_ts = models.DateTimeField(auto_now_add=True)
    close_ts = models.DateTimeField();

    def __unicode__(self):
        return u'order_id: {} ____ buyer: {} ____ gig: {} ____ status: {} ____ purchase_ts: {} ____ close_ts: {}'\
            .format(self.id, self.buyer, self.gig, self.status, self.purchase_ts, self.close_ts)


class Payment(models.Model):
    order = models.OneToOneField('Order')
    payment_ts = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'payment_id: {} ____ order: {} ____ payment_ts: {}'\
            .format(self.id, self.order, self.payment_ts)


class Message(models.Model):
    order = models.ForeignKey('Order')
    message_content = models.CharField(required=True, max_length=5000);

    def __unicode__(self):
        return u'message_id: {} ____ order: {} ____ message_content: {}'\
            .format(self.id, self.order, self.message_content)


class Rating(models.Model):
    order = models.OneToOneField('Order')
    rating = models.IntegerField(default=0)
    comment = models.CharField(required=False, max_length=5000);
    rating_ts = models.DateTimeField(auto_now_add=True);

    def __unicode__(self):
        return u'rating_id: {} ____ order: {} ____ rating: {} ____ comment: {} ____ rating_ts: {}'\
            .format(self.id, self.order, self.rating, self.comment, self.rating_ts)


class Tag(models.Model):
    tag_content = models.CharField(required=True, max_length=100)

    def __unicode__(self):
        return u'tag_id: {} ____ tag_content: {}'\
            .format(self.id, self.tag_content)


class Category(models.Model):
    category_name = models.CharField(required=True, max_length=100)

    def __unicode__(self):
        return u'category_id: {} ____ category_name: {}'\
            .format(self.id, self.category_name)


class SubCategory(models.Model):
    sub_category_name = models.CharField(required=True, max_length=100)

    def __unicode__(self):
        return u'sub_category_id: {} ____ sub_category_name: {}'\
            .format(self.id, self.sub_category_name)


class Image(models.Model):
    gig = models.ForeignKey(Gig)

    def __unicode__(self):
        return u'image_id: {} ____ gig: {}'\
            .format(self.id, self.gig)










