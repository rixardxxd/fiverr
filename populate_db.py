#!/usr/bin/env python
# coding=utf-8
# add test instances of different models

import os


def populate():
    john = add_user('John', 'john@qq.com', '1')
    john.save()
    david = add_user('David', 'david@qq.com', '2')
    david.save()
    mike = add_user('Mike', 'mike@qq.com', '3')
    mike.save()

    cat_revise = add_category("revise")
    cat_revise.save()
    sub_cat_resume = add_sub_category("resume", cat_revise)
    sub_cat_resume.save()
    cat_compose = add_category("compose")
    cat_compose.save()
    sub_cat_music = add_sub_category("music", cat_compose)
    sub_cat_music.save()
    cat_goods = add_category("goods")
    cat_goods.save()
    sub_cat_car = add_sub_category("car", cat_goods)
    sub_cat_car.save()

    tag_resume = add_tag("resume")
    tag_resume.save()
    tag_cool = add_tag("cool stuff")
    tag_cool.save()
    tag_useful = add_tag("very useful")
    tag_useful.save()

    gig_resume = add_gig("Revise Resume", john, "Good John can revise resume", sub_cat_resume, 2, "这是砸发达阿三范德萨发生打法是否")
    gig_resume.save()
    gig_music = add_gig("Compose songs", david, "David will make excellent music", sub_cat_music, 10, "Please upload the basic songs")
    gig_music.save()
    gig_car = add_gig("Good car!", mike, "Mike has a good car to sell", sub_cat_car, 5, "Got a good car")
    gig_car.save()


    # add tags for gig
    gig_resume.tags.add(tag_resume, tag_useful)
    gig_music.tags.add(tag_cool, tag_useful)
    gig_car.tags.add(tag_cool)

    #add ratings for gig
    gig_resume.rating.add(score=5,user=john,ip_address='127.0.0.1',order_id='1')
    gig_resume.rating.add(score=4,user=david,ip_address='127.0.0.1',order_id='1')
    gig_resume.rating.add(score=3,user=mike,ip_address='127.0.0.1',order_id='1')
    gig_resume.rating.add(score=2,user=mike,ip_address='127.0.0.1',order_id='2')

    gig_music.rating.add(score=2,user=mike,ip_address='127.0.0.1',order_id='3')

    gig_car.rating.add(score=3,user=mike,ip_address='127.0.0.1',order_id='4')

    print "/////////////////////////"
    img_resume = add_image(gig_resume, "/static/img/img1.jpeg")
    print "/////////////////////////"
    img_resume.save()


def add_tag(tag_content):
    tag, created = Tag.objects.get_or_create(tag_content=tag_content)
    print tag
    return tag


def add_sub_category(sub_cat, cat):
    sub_category, created = SubCategory.objects.get_or_create(sub_category_name=sub_cat,
                                                     category=cat)
    print sub_category
    return sub_category


def add_category(cat):
    category, created = Category.objects.get_or_create(category_name=cat)
    print category
    return category


def add_image(gig, img_url):
    img, created = Image.objects.get_or_create(gig=gig)
    img.image = img_url
    print img
    return img


def add_gig(title, seller, desc, sub_cat, duration, instr):
    gig, created = Gig.objects.get_or_create(title=title,
                                    seller=seller,
                                    rating_score=0,
                                    rating_votes=0,
                                    description=desc,
                                    sub_category=sub_cat,
                                    duration=duration,
                                    instruction=instr)
    print gig
    return gig


def add_user(username, email, password):
    try:
        new_user = User.objects.create_user(username, email, password)
    except IntegrityError:
        return User.objects.get(username=username, email=email)
    return new_user


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fiverr.settings')
    from website.models import *
    from django.contrib.auth.models import User
    from django.db.utils import IntegrityError
    populate()

