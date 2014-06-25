from alert.search.models import Citation, Docket
from alert.search.models import Court
from alert.search.models import Document

from django.contrib import admin


class CitationAdmin(admin.ModelAdmin):
    # This needs to be disabled for performance reasons.
    #list_display = ('docket_number', 'federal_cite', 'case_name', )
    search_fields = ['case_name', 'docket_number', 'federal_cite_one']


class DocumentAdmin(admin.ModelAdmin):
    # ordering is brutal. Don't put it here. Sorry.
    #list_display = ('citation',)
    #list_filter = ('court',)
    fields = ('citation', 'docket', 'source', 'sha1', 'date_filed', 'download_url', 'local_path', 'precedential_status',
              'blocked', 'date_blocked', 'extracted_by_ocr', 'time_retrieved', 'date_modified',
              'cases_cited', 'citation_count', 'plain_text', 'nature_of_suit', 'judges', 'html', 'html_lawbox',
              'html_with_citations', )
    raw_id_fields = ('citation', 'cases_cited', 'docket')
    search_fields = ['plain_text', 'html', 'html_lawbox']
    readonly_fields = ('time_retrieved', 'date_modified', 'citation_count')
    list_filter = (
        'source',
    )


class CourtAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'short_name',
        'position',
        'in_use',
        'pk'
    )
    list_filter = (
        'jurisdiction',
        'in_use',
    )


admin.site.register(Document, DocumentAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(Citation, CitationAdmin)
admin.site.register(Docket, admin.ModelAdmin)

