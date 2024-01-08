# mixins.py

class PolityIdMixin:
    def get_initial(self):
        initial = super().get_initial()
        polity_id_x = self.request.GET.get('polity_id_x')
        initial['polity'] = polity_id_x
        return initial
