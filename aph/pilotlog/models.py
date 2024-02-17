from django.db import models


class User(models.Model):
    user_id = models.IntegerField(unique=True)

    class Meta:
        app_label = 'pilotlog'


class Aircraft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guid = models.CharField(max_length=36, unique=True)
    platform = models.IntegerField(null=True)
    _modified = models.DateTimeField(null=True)

    # Meta Fields
    fin = models.CharField(max_length=100, blank=True)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(default=0)
    make = models.CharField(max_length=100)
    run2 = models.BooleanField(default=False)
    aircraft_class = models.IntegerField(null=True)
    model = models.CharField(max_length=100)
    power = models.IntegerField(null=True)
    seats = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100)
    complex = models.BooleanField(default=False)
    cond_log = models.IntegerField(null=True)
    fav_list = models.BooleanField(default=False)
    category = models.IntegerField(null=True)
    high_perf = models.BooleanField(default=False)
    sub_model = models.CharField(max_length=100, blank=True)
    aerobatic = models.BooleanField(default=False)
    ref_search = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    tailwheel = models.BooleanField(default=False)
    default_app = models.IntegerField(null=True)
    default_log = models.IntegerField(null=True)
    default_ops = models.IntegerField(null=True)
    device_code = models.IntegerField(null=True)
    aircraft_code = models.CharField(max_length=36)
    default_launch = models.IntegerField(null=True)
    record_modified = models.DateTimeField(null=True)
    table = models.CharField(max_length=36)
    meta = models.CharField(max_length=36)

    year = models.IntegerField(null=True)
    gear_type = models.CharField(max_length=100, blank=True)
    engine_type = models.CharField(max_length=100, blank=True)
    high_performance = models.BooleanField(default=False)
    pressurized = models.BooleanField(default=False)
    taa = models.BooleanField(default=False)
