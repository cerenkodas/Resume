from django.contrib import admin
from .models import (
    SiteSetting,
    SocialMedia,
    HomeHero,
    HomeFloatingCard,
    AboutInfo,
    AboutCard,
    ResumeEducation,
    ResumeExperience,
    ExperienceSkill,
    Certificate,
    SkillGroup,
    SkillItem,
    Technology,
    Project,
    ContactInfo,
)


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'full_name', 'is_active')
    list_filter = ('is_active',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'url', 'icon_class', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('platform_name',)
    ordering = ('order',)


@admin.register(HomeHero)
class HomeHeroAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_tr', 'is_active')
    list_filter = ('is_active',)


@admin.register(HomeFloatingCard)
class HomeFloatingCardAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_tr', 'icon_class', 'css_class', 'order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)


@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_tr', 'is_active')
    list_filter = ('is_active',)


@admin.register(AboutCard)
class AboutCardAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_tr', 'card_type', 'order', 'is_active')
    list_filter = ('card_type', 'is_active')
    search_fields = ('title_en', 'title_tr')
    ordering = ('card_type', 'order')


@admin.register(ResumeEducation)
class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ('school_name_en', 'school_name_tr', 'date_text_en', 'gpa', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('school_name_en', 'school_name_tr', 'department_en', 'department_tr')
    ordering = ('order',)


class ExperienceSkillInline(admin.TabularInline):
    model = ExperienceSkill
    extra = 1


@admin.register(ResumeExperience)
class ResumeExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position_en', 'position_tr', 'date_text_en', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('company_name', 'position_en', 'position_tr')
    ordering = ('order',)
    inlines = [ExperienceSkillInline]


@admin.register(ExperienceSkill)
class ExperienceSkillAdmin(admin.ModelAdmin):
    list_display = ('experience', 'skill_text_en', 'skill_text_tr', 'order')
    search_fields = ('skill_text_en', 'skill_text_tr')
    ordering = ('order',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'organization', 'year', 'order', 'is_active')
    list_filter = ('year', 'organization', 'is_active')
    search_fields = ('certificate_name', 'organization')
    ordering = ('order',)


class SkillItemInline(admin.TabularInline):
    model = SkillItem
    extra = 1


@admin.register(SkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_tr', 'icon_class', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title_en', 'title_tr')
    ordering = ('order',)
    inlines = [SkillItemInline]


@admin.register(SkillItem)
class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_group', 'order')
    search_fields = ('name',)
    ordering = ('order',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_url', 'is_github_active', 'order', 'is_active')
    list_filter = ('is_active', 'is_github_active', 'technologies')
    search_fields = ('title', 'description_en', 'description_tr')
    filter_horizontal = ('technologies',)
    ordering = ('order',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'location_en', 'location_tr', 'is_active')
    list_filter = ('is_active',)