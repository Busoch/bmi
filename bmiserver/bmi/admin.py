from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe
import plotly.graph_objects as go

from .models import BMIRecord


class BMIRecordInline(admin.TabularInline):
    model = BMIRecord
    extra = 0
    fields = ("weight", "height", "bmi", "category", "created_at")
    readonly_fields = ("bmi", "category", "created_at")


class CustomUserAdmin(BaseUserAdmin):
    inlines = [BMIRecordInline]

    def bmi_chart(self, obj):
        """Render a BMI history chart for this user"""
        records = BMIRecord.objects.filter(user=obj).order_by("created_at")

        if not records.exists():
            return "No BMI records yet."

        dates = [r.created_at.strftime("%Y-%m-%d") for r in records]
        bmis = [r.bmi for r in records]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=bmis, mode="lines+markers", name="BMI"))
        fig.update_layout(
            title="BMI History Over Time",
            xaxis_title="Date",
            yaxis_title="BMI",
            height=400,
        )

        # Embed as HTML
        return mark_safe(fig.to_html(full_html=False))

    bmi_chart.short_description = "BMI Trend"

    # Add chart to user detail page
    readonly_fields = ("bmi_chart",)
    fieldsets = BaseUserAdmin.fieldsets + (
        ("BMI Analysis", {"fields": ("bmi_chart",)}),
    )


# Unregister default User admin and register custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(BMIRecord)
class BMIRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "weight", "height", "bmi", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("user__username", "category")
    ordering = ("-created_at",)
