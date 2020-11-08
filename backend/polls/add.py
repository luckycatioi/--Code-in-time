from polls.models import Choice,People
for i in range(1,11):
    Choice.objects.create(Choice_id=i)