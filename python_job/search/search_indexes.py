import datetime
from haystack import indexes
from vlance.models import Job



class AddJobPostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    Nganh_Nghe = indexes.CharField(model_attr='Nganh_Nghe')
    Thanh_Pho = indexes.CharField(model_attr='Thanh_Pho')
    date = indexes.DateTimeField(model_attr='created_at')
   # location = indexes.CharField(model_attr='location')

    title = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Job
