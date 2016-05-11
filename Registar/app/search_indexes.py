import datetime
from haystack import indexes
from app.models import Firma

class FirmaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    naziv = indexes.CharField(model_attr="naziv")
    id = indexes.CharField(model_attr="id")

    def get_model(self):
        return Firma