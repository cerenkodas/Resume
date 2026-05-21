from django.db import models


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=100, default="Ceren Kodaş CV")
    full_name = models.CharField(max_length=100, default="Ceren Kodaş")
    copyright_text_tr = models.CharField(max_length=200, default="Tüm Hakları Saklıdır")
    copyright_text_en = models.CharField(max_length=200, default="All Rights Reserved")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_title


class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, help_text="Example: bi bi-linkedin")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return self.platform_name


class HomeHero(models.Model):
    title_tr = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    typed_text_tr = models.CharField(max_length=250)
    typed_text_en = models.CharField(max_length=250)
    description_tr = models.TextField()
    description_en = models.TextField()
    profile_image = models.ImageField(upload_to="home/", blank=True, null=True)
    button_1_text_tr = models.CharField(max_length=100, blank=True)
    button_1_text_en = models.CharField(max_length=100, blank=True)
    button_1_url = models.CharField(max_length=200, blank=True)
    button_2_text_tr = models.CharField(max_length=100, blank=True)
    button_2_text_en = models.CharField(max_length=100, blank=True)
    button_2_url = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Home Hero"
        verbose_name_plural = "Home Hero"

    def __str__(self):
        return self.title_en


class HomeFloatingCard(models.Model):
    title_tr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="Example: bi bi-code-slash")
    css_class = models.CharField(max_length=50, blank=True, help_text="Example: design, code, creativity")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Home Floating Card"
        verbose_name_plural = "Home Floating Cards"

    def __str__(self):
        return self.title_en


class AboutInfo(models.Model):
    eyebrow_tr = models.CharField(max_length=100, default="Kendim Hakkında")
    eyebrow_en = models.CharField(max_length=100, default="About Me")
    title_tr = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_1_tr = models.TextField()
    description_1_en = models.TextField()
    description_2_tr = models.TextField(blank=True)
    description_2_en = models.TextField(blank=True)
    description_3_tr = models.TextField(blank=True)
    description_3_en = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to="about/", blank=True, null=True)
    quote_tr = models.TextField(blank=True)
    quote_en = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About Info"
        verbose_name_plural = "About Info"

    def __str__(self):
        return self.title_en


class AboutCard(models.Model):
    CARD_TYPES = [
        ("personal", "Personal Info"),
        ("interest", "Interest"),
    ]

    card_type = models.CharField(max_length=20, choices=CARD_TYPES)
    title_tr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    value_tr = models.CharField(max_length=200, blank=True)
    value_en = models.CharField(max_length=200, blank=True)
    description_tr = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, help_text="Example: bi bi-person")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["card_type", "order"]
        verbose_name = "About Card"
        verbose_name_plural = "About Cards"

    def __str__(self):
        return f"{self.title_en} - {self.card_type}"


class ResumeEducation(models.Model):
    school_name_tr = models.CharField(max_length=200)
    school_name_en = models.CharField(max_length=200)
    department_tr = models.CharField(max_length=200, blank=True)
    department_en = models.CharField(max_length=200, blank=True)
    date_text_tr = models.CharField(max_length=100)
    date_text_en = models.CharField(max_length=100)
    gpa = models.CharField(max_length=50, blank=True)
    description_tr = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Resume Education"
        verbose_name_plural = "Resume Education"

    def __str__(self):
        return self.school_name_en


class ResumeExperience(models.Model):
    company_name = models.CharField(max_length=150)
    position_tr = models.CharField(max_length=150)
    position_en = models.CharField(max_length=150)
    date_text_tr = models.CharField(max_length=100)
    date_text_en = models.CharField(max_length=100)
    description_tr = models.TextField()
    description_en = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Resume Experience"
        verbose_name_plural = "Resume Experience"

    def __str__(self):
        return f"{self.company_name} - {self.position_en}"


class ExperienceSkill(models.Model):
    experience = models.ForeignKey(
        ResumeExperience,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    skill_text_tr = models.CharField(max_length=255)
    skill_text_en = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Experience Skill"
        verbose_name_plural = "Experience Skills"

    def __str__(self):
        return self.skill_text_en


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=150)
    year = models.CharField(max_length=20)
    description_tr = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return f"{self.certificate_name} - {self.organization}"


class SkillGroup(models.Model):
    title_tr = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    description_tr = models.TextField()
    description_en = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="Example: bi bi-code-slash")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Skill Group"
        verbose_name_plural = "Skill Groups"

    def __str__(self):
        return self.title_en


class SkillItem(models.Model):
    skill_group = models.ForeignKey(
        SkillGroup,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Skill Item"
        verbose_name_plural = "Skill Items"

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description_tr = models.TextField()
    description_en = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    is_github_active = models.BooleanField(default=True)
    technologies = models.ManyToManyField(Technology, blank=True, related_name="projects")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    title_tr = models.CharField(max_length=150, default="İletişim Bilgileri")
    title_en = models.CharField(max_length=150, default="Contact Info")
    description_tr = models.TextField()
    description_en = models.TextField()
    location_tr = models.CharField(max_length=150)
    location_en = models.CharField(max_length=150)
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.email

class ProfessionalSkill(models.Model):
    title_tr = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    percentage = models.PositiveIntegerField(default=50)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Professional Skill"
        verbose_name_plural = "Professional Skills"

    def __str__(self):
        return f"{self.title_en} - {self.percentage}%"