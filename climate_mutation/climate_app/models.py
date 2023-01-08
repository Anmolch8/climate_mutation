from django.db import models



class disaster(models.Model):
    title=models.CharField(max_length=3000)
    date=models.DateField()
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='disaster_pics',blank=True,null=True)
    description=models.TextField()
    def __str__(self):
        return self.title       
class images_of_change(models.Model):
    from_date=models.DateField()
    to_date=models.DateField()
    before_image=models.ImageField(upload_to='change_pics',blank=True)
    after_image=models.ImageField(upload_to='change_pics',blank=True)
    description=models.TextField()
    def __str__(self):
        return self.from_date
class video(models.Model):
    title=models.CharField(max_length=3000)
    link=models.URLField()
    description=models.TextField()
    def __str__(self):
        return self.title

class blog(models.Model):
    title=models.CharField(max_length=3000)
    image=models.ImageField(upload_to='blogs_pics',blank=True)
    description=models.TextField()
    added_on=models.DateField()
    author=models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return self.title

class ngo(models.Model):
    name=models.CharField(max_length=500)
    cause=models.CharField(max_length=500)
    website=models.URLField()
    address=models.TextField()
    contact_number=models.CharField(max_length=12)
    logo=models.ImageField(upload_to='ngos_pics',blank=True)
    description=models.TextField()
    def __str__(self):
        return self.name


class faq(models.Model):
    question=models.TextField()
    answer=models.TextField()
    def __str__(self):
        return self.question
# class volunteer(models.Model):
#     name=models.CharField(max_length=500)
#     image=models.ImageField(upload_to='volunteer_pics',blank=True)
#     about=models.TextField()
#     def __str__(self):
#         return self.name
class causes_category(models.Model):
     category_name=models.CharField(max_length=2000)
     def __str__(self):
         return str(self.category_name)
class cause(models.Model):
    cat=models.ForeignKey(causes_category, on_delete=models.CASCADE) 
    title=models.CharField(max_length=3000)
    image=models.ImageField(upload_to='climate_change_pics',blank=True)
    description=models.TextField()
    def __str__(self):
        return self.title
class evidence(models.Model):
    title=models.CharField(max_length=3000)
    image=models.ImageField(upload_to='evidence_pics',blank=True)
    description=models.TextField()
    def __str__(self):
        return self.title        
class effect(models.Model):
      title=models.CharField(max_length=3000)
      image=models.ImageField(upload_to='climate_change_effects_pics',blank=True)
      description=models.TextField()
      def __str__(self):
        return self.title

class action(models.Model):
      title=models.CharField(max_length=3000)
      image=models.ImageField(upload_to='prevention_pics',blank=True)
      description=models.TextField()
      def __str__(self):
        return self.title
class expert(models.Model):
    name=models.CharField(max_length=500)
    expertise=models.CharField(max_length=500) 
    image=models.ImageField(upload_to='expert_pics',blank=True,null=True)
    conatct=models.CharField(max_length=1000,null=True)   
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name
class user_register(models.Model):
    fname=models.CharField(max_length=300)
    lname=models.CharField(max_length=300)
    user_email=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    dob=models.DateField(blank=True,null=True)
    address=models.CharField(max_length=5000,blank=True,null=True)
    city=models.CharField(max_length=500,blank=True,null=True)
    pincode=models.CharField(max_length=10,blank=True,null=True)
    profile_pic=models.FileField(upload_to='profile_pics',blank=True,null=True)

    #confirm_password=models.CharField(max_length=16)
    def __str__(self):
        return self.fname+' '+self.lname
class user_login(models.Model):
    login_name=models.CharField(max_length=300)
    login_pass=models.CharField(max_length=16)
    def __str__(self):
        return self.login_name
class review(models.Model):
    user_name=models.CharField(max_length=500)
    heading=models.CharField(max_length=5000)
    description=models.TextField()
    def __str__(self):
        return self.heading   
class help_support(models.Model):
    user_name=models.CharField(max_length=500)
    help_heading=models.CharField(max_length=5000)
    help_description=models.TextField()
    def __str__(self):
        return self.help_heading           

     
class contact(models.Model):
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    subject=models.CharField(max_length=5000)
    message=models.TextField()
    def __str__(self):
        return self.name
class entitie(models.Model):
    entity_id=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class dataset(models.Model):
    entity_id=models.ForeignKey(entitie, on_delete=models.CASCADE)
    name=models.CharField(max_length=1000)
    description=models.TextField()
    n_columns=models.PositiveIntegerField()
    n_rows=models.PositiveIntegerField()
    columns_names=models.CharField(max_length=5000)
    columns_description=models.TextField()
    download_link=models.CharField(max_length=500,blank=True)
    def __str__(self):
       return  self.name         
class visuals(models.Model):
    entity_id=models.ForeignKey(entitie, on_delete=models.CASCADE,db_constraint=False)
    visual_name=models.CharField(max_length=3000)
    link=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.visual_name
class perdiction(models.Model):
    entity_id=models.ForeignKey(entitie, on_delete=models.CASCADE,db_constraint=False)
    perdiction_name=models.CharField(max_length=3000)
    link=models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.perdiction_name




           





    
