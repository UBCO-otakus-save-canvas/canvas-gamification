from django.forms import RadioSelect
from django.forms import Textarea


class RadioInlineSelect(RadioSelect):
    template_name = 'widgets/radio_inline.html'
    option_template_name = 'widgets/radio_inline_option.html'

    def __init__(self, attr=None, choices=()):
        super().__init__(attr, choices)


class JSONEditor(Textarea):
    template_name = 'widgets/jsoneditor.html'

    def __init__(self, attrs=None, schema=None):
        super().__init__(attrs)
        self.schema = schema

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['schema'] = self.schema
        return context

    class Media:
        js = (
            'https://cdn.jsdelivr.net/npm/@json-editor/json-editor@latest/dist/jsoneditor.min.js',
        )
