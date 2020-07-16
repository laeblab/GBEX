from django.db import models
from django.urls import reverse_lazy
from django.forms import DateInput

from dal import autocomplete

from GBEX_bigfiles.fields import ResumableFileField
from GBEX_app.helpers import get_upload_path

from .models import GBEXModelBase, default_order, default_widgets
from .Inventory import Strain

menu_label = "Experiments"


class Fermentation(GBEXModelBase):
	RunDate = models.DateField(null=True, blank=True)
	Strain = models.ForeignKey(Strain, on_delete=models.PROTECT, null=True, blank=True)
	Data_file = ResumableFileField(blank=True, null=True, upload_to=get_upload_path, max_length=500)

	menu_label = menu_label
	order = [*default_order, 'RunDate', 'Strain', 'Data_file']
	symbol = "FE"
	widgets = {
		**default_widgets,
		'Strain': autocomplete.ModelSelect2(url=reverse_lazy('Strain-autocomplete')),
		"RunDate": DateInput(attrs={'data-isdate': "yes"})
	}
	col_display_func_dict = {
		'Data_file': lambda
			item: f"<a href='/downloads/{item.Data_file}'>{str(item.Data_file).split('/')[-1]}</a>",
	}
	col_html_string = ['Data_file', ]
