from django.views.generic import TemplateView
import indicoio
import indico
from indicoio.custom import Collection

hipsterv2 = Collection("Hipster V2")
indicoio.config.api_key = indico.INDICO_KEY

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': "Some value",
        }
        return self.render_to_response(context)