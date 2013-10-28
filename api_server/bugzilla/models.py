from django.db import models

class attachment(models.Model):
    class Meta:
        verbose_name = ('attachment')
        verbose_name_plural = ('attachments')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    bug_id = models.IntegerField(null=True)
    datec = models.DateTimeField()
    description = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    systempath = models.CharField(max_length=500)
    isobsolete = models.IntegerField()
    submitter = models.IntegerField()

class bug(models.Model):
    class Meta:
        verbose_name = ('bug')
        verbose_name_plural = ('bugs')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=10, null=True)
    version = models.CharField(max_length=10, null=True)
    severity = models.CharField(max_length=45, null=True)
    hardware = models.CharField(max_length=45, null=True)
    priority = models.CharField(max_length=45, null=True)
    reporter = models.IntegerField()
    qa = models.IntegerField()
    docs = models.IntegerField()
    whiteboard = models.CharField(max_length=455, null=True)
    summary =models.CharField(max_length=450)
    description = models.TextField()
    reported = models.IntegerField()
    fixedinver = models.CharField(max_length=255, null=True)
    component_id = models.IntegerField()
    subcomponent_id = models.IntegerField()

class cc(models.Model):
    class Meta:
        verbose_name = ('cc')
        verbose_name_plural = ('cc')

    def __unicode__(self):
        pass

    bug_id = models.IntegerField(primary_key=True)
    who = models.IntegerField()

class comment(models.Model):
    class Meta:
        verbose_name = ('comment')
        verbose_name_plural = ('comments')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    user = models.IntegerField()
    datec = models.DateTimeField()
    bug = models.IntegerField()

class component_cc(models.Model):
    class Meta:
        verbose_name = ('component_cc')
        verbose_name_plural = ('component_cc')

    def __unicode__(self):
        pass

    component_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()

class component(models.Model):
    class Meta:
        verbose_name = ('component')
        verbose_name_plural = ('components')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=255, null=True)
    product_id = models.IntegerField(null=True)
    owner = models.IntegerField()
    qa = models.IntegerField(null=True)

class dependency(models.Model):
    class Meta:
        verbose_name = ('dependency')
        verbose_name_plural = ('dependencies')

    def __unicode__(self):
        pass

    blocked = models.IntegerField(primary_key=True)
    dependson = models.IntegerField()

class duplicate(models.Model):
    class Meta:
        verbose_name = ('duplicate')
        verbose_name_plural = ('duplicates')

    def __unicode__(self):
        pass

    dup = models.IntegerField(primary_key=True)
    dup_of = models.IntegerField()

class product(models.Model):
    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('products')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=500, null=True)

class release(models.Model):
    class Meta:
        verbose_name = ('release')
        verbose_name_plural = ('releases')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

class subcomponent(models.Model):
    class Meta:
        verbose_name = ('subcomponent')
        verbose_name_plural = ('subcomponents')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)
    component_id = models.IntegerField()

class subcomponent_owner(models.Model):
    class Meta:
        verbose_name = ('subcomponent_owner')
        verbose_name_plural = ('subcomponent_owners')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    subcomponent_id = models.IntegerField()
    subcomponent_owner = models.IntegerField(null=True)

class user(models.Model):
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __unicode__(self):
        pass

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=19, null=True, default=1)
    password = models.CharField(max_length=255)