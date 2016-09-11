from django.views.generic import TemplateView
import indicoio
import indico

indicoio.config.api_key = indico.INDICO_KEY

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)